

def compute_accuracy_cosette(dbconn, experiment_id, target_query_ids=None, restore_prev=True, ignore_distinct=False):
    num_computed = 0

    # select non-computed results
    compute_results = True
    print_log_message(
        'INFO', ['compute_accuracy_cosette', 'start selecting (query_id, cosette_execution_result_id) pairs'])
    try:
        with closing(dbconn.cursor()) as cu:
            cu.execute('''USE benchmark''')

            # select (experiment_id, query_id) pairs to compute the accuracy
            if target_query_ids:
                select_results = []
                for target_query_id in target_query_ids:
                    cu.execute('''
                        SELECT qr.query_id,
                               a.cosette_execution_result_id
                        FROM   query_result qr
                        JOIN   accuracy a
                        ON     qr.query_id=a.query_id AND qr.experiment_id=a.experiment_id
                        JOIN   query q ON qr.query_id=q.query_id
                        JOIN   experiment_info E ON E.experiment_id=qr.experiment_id
                        JOIN   sql_execution_result SER_gold ON SER_gold.sql_execution_result_id=q.sql_execution_result_id
                        JOIN   sql_execution_result SER_gen ON SER_gen.sql_execution_result_id=qr.sql_execution_result_id
                        WHERE  qr.experiment_id=%d and (a.accurate_ex=1 OR a.accurate_ex_tmp_data=1 OR SER_gold.errno = -1 OR SER_gen.errno = -1) AND SER_gold.errno <= 0 AND SER_gen.errno <=0 AND qr.query_id=%d
                        ''' % (experiment_id, target_query_id))
                    select_results.extend(list(cu.fetchall()))
            else:
                cu.execute('''
                    SELECT qr.query_id,
                           a.cosette_execution_result_id
                    FROM   query_result qr
                    JOIN   accuracy a ON qr.query_id=a.query_id AND qr.experiment_id=a.experiment_id
                    JOIN   query q ON qr.query_id=q.query_id
                    WHERE  qr.experiment_id=%d
                    ''' % (experiment_id))
                # JOIN   experiment_info E ON E.experiment_id=qr.experiment_id
                # JOIN   sql_execution_result SER_gold ON SER_gold.sql_execution_result_id=q.sql_execution_result_id
                # JOIN   sql_execution_result SER_gen ON SER_gen.sql_execution_result_id=qr.sql_execution_result_id
                # WHERE  qr.experiment_id=%d and (a.accurate_ex=1 OR a.accurate_ex_tmp_data=1 OR SER_gold.errno = -1 OR SER_gen.errno = -1) AND SER_gold.errno <= 0 AND SER_gen.errno <=0
                select_results = cu.fetchall()
    except MySQLdb.Error as e:
        print_log_message(
            'ERROR',
            ['compute_accuracy_cosette', 'selecting (query_id, cosette_execution_result_id) pairs failed', str(e)])
        compute_results = False
        select_results = []
    print_log_message('INFO',
                      ['compute_accuracy_cosette', 'selecting (query_id, cosette_execution_result_id) pairs done',
                       str(
                           len(select_results)) + ' query/queries found', str(select_results)])

    # compute the results
    if compute_results:
        print_log_message('INFO', ['compute_accuracy_cosette', 'start executing Cosette'])
        try:
            for select_result in select_results:
                query_id = select_result[0]
                prev_cosette_execution_result_id = select_result[1]
                if prev_cosette_execution_result_id and not restore_prev:
                    continue
                dbconn.begin()

                with closing(dbconn.cursor()) as cu:
                    cu.execute('''USE benchmark''')

                    # select db and queries
                    cu.execute('''
                        SELECT query.db,
                               query_result.db_suffix,
                               query.gold_sql_cosette,
                               query.gold_sql_cosette_rename,
                               query_result.gen_sql_cosette,
                               query_result.gen_sql_execute,
                               query.gold_sql_execute
                        FROM   query, query_result
                        WHERE  query.query_id=query_result.query_id
                           AND query_result.experiment_id=%d
                           AND query_result.query_id=%d
                        ''' % (experiment_id, query_id))
                    if cu.rowcount == 0:
                        raise Exception('query not found: (%d, %d)' % (experiment_id, query_id))
                    elif cu.rowcount > 1:
                        raise Exception('unexcpeted rows: (%d, %d)' % (experiment_id, query_id))
                    select_result = cu.fetchone()
                    db = select_result[0]
                    db_suffix = select_result[1]
                    gold_sql_cosette = select_result[2]
                    gold_sql_cosette_rename = select_result[3]
                    gen_sql_cosette = select_result[4]
                    gen_sql_execute = select_result[5]
                    gold_sql_execute = select_result[6]
                    if is_IRNet == True:
                        print_log_message('INFO', ['compute_accuracy_cosette', 'IRNet cannot generate DISTINCT',
                                                   str((experiment_id, query_id)), ])
                        p = re.compile(" *distinct *", re.I)
                        gold_sql_cosette = p.sub(r' ', gold_sql_cosette)
                        gold_sql_cosette_rename = p.sub(r' ', gold_sql_cosette_rename)
                        gen_sql_cosette = p.sub(r' ', gen_sql_cosette)

                    print_log_message('INFO', ['compute_accuracy_cosette', 'SQLs to execute',
                                               str((experiment_id, query_id)),
                                               gold_sql_cosette_rename if db_suffix else gold_sql_cosette,
                                               gen_sql_cosette
                                               ])

                    # execute SQLs through dummy DB
                    if db_suffix and db != "wikisql":
                        db = db + '_' + db_suffix

                    if db == "wikisql":
                        dummydb = db
                    else:
                        dummydb = db + '_dummy'
                    if db.lower().startswith('wikitablequestionsnull'):
                        dummydb = 'wikitablequestions_rename_dummy'

                    try:
                        cu.execute('''USE ''' + dummydb.replace('-', ''))
                        if db_suffix:
                            cu.execute(gold_sql_cosette_rename)
                        else:
                            cu.execute(gold_sql_execute)
                        errno_gold = 0
                    except MySQLdb.Error as e:
                        errno_gold = e.args[0]
                        # raise Exception('gold query error: (%s, %s)' % (gold_sql_execute, e.args[1]))
                    try:
                        cu.execute('''USE ''' + dummydb.replace('-', ''))
                        cu.execute(gen_sql_execute)
                        errno_gen = 0
                    except MySQLdb.Error as e:
                        errno_gen = e.args[0]
                    cu.execute('''USE benchmark''')
                    if errno_gold != 0:
                        cos_output = 'Invalid gold SQL'
                        cos_result = 'Invalid gold SQL'
                    elif errno_gen != 0:
                        cos_output = 'Invalid generated SQL'
                        cos_result = 'Invalid generated SQL'
                    valid_sqls = errno_gold == 0 and errno_gen == 0

                    print_log_message(
                        'INFO', ['compute_accuracy_cosette', 'executing SQLs over dummy DBs done',
                                 str((experiment_id, query_id)),
                                 str(errno_gold),
                                 str(errno_gen)
                                 ])

                    # run Cosette
                    # if valid_sqls:
                    if True:  # Don't care whether the execution raised error or not
                        d = {
                            # [2018.8.14] Cosette cannot handle double quotation mark
                            # [2018.8.14] Cosette also cannot handle quotation mark in value
                            'gold_sql': gold_sql_cosette_rename.strip().replace('"',
                                                                                "'") if db_suffix or db == "wikisql" else gold_sql_cosette.decode(
                                'ascii', 'ignore').replace('"', "'"),
                            'gen_sql': gen_sql_cosette.strip().decode('ascii', 'ignore').replace('"', "'")}
                        print_log_message('INFO', ['compute_accuracy_cosette', 'executing Cosette start',
                                                   str((experiment_id, query_id)),
                                                   str(d['gold_sql']), str(d['gen_sql'])
                                                   ])
                        # TODO: delete me when the issue solved
                        if db == 'mas_rename':
                            print('mas_rename not found: (%d, %d)' % (experiment_id, query_id))
                            continue

                        try:
                            with open('./cosette_template/' + db + '.template.cos') as f:
                                template_string = f.read()
                            templates = template_string.split('\n')
                            templates_need = []
                            for tem in templates:
                                if tem.startswith('schema '):
                                    schema_name = tem.split('schema schema_')[1].split('(')[0]
                                    if schema_name in d["gold_sql"].lower() or schema_name in d["gen_sql"].lower():
                                        templates_need.append(tem)
                                elif tem.startswith('table '):
                                    table_name = tem.split('table ')[1].split('(')[0]
                                    if table_name in d["gold_sql"].lower() or table_name in d["gen_sql"].lower():
                                        templates_need.append(tem)
                                else:
                                    templates_need.append(tem)
                            template_string = '\n'.join(templates_need)
                        except IOError:
                            raise Exception(db + '.template.cos doesn\'t exist')
                        # except Exception:
                        #    raise Exception(db + '\'s running cosette fail: Another exception')

                        try:
                            cos_source = Template(template_string).substitute(d)
                            print(cos_source)
                            # cos_output = solver.solve(cos_source, cos_folder="./Cosette")
                            cos_output = requests.post("https://demo.cosette.cs.washington.edu/solve",
                                                       data={"api_key": COSETTE_API_KEY, "query": cos_source},
                                                       verify=False).text
                            cos_result = json.loads(cos_output)['result']
                        except UnicodeDecodeError:
                            cos_output = 'Cosette UnicodeDecodeError'
                            cos_result = 'Cosette UnicodeDecodeError'
                            print_log_message('INFO',
                                              ['compute_accuracy_cosette', 'executing Cosette UnicodeDecodeError',
                                               str((experiment_id, query_id)),
                                               cos_output
                                               ])
                        except Exception:
                            cos_output = 'Cosette Server Error'
                            cos_result = 'Cosette Server Error'
                            print_log_message('INFO', ['compute_accuracy_cosette', 'executing Cosette Server Error',
                                                       str((experiment_id, query_id)),
                                                       cos_output
                                                       ])
                        else:
                            print_log_message('INFO', ['compute_accuracy_cosette', 'executing Cosette done',
                                                       str((experiment_id, query_id)),
                                                       cos_output
                                                       ])

                    # delete previous cosette execution result
                    if prev_cosette_execution_result_id:
                        cu.execute('''
                           DELETE FROM cosette_execution_result
                           WHERE  cosette_execution_result_id=%d
                           ''' % (prev_cosette_execution_result_id))

                    # insert (cos_output, cos_result) to cosette_execution_result, and get
                    # cosette_execution_result_id
                    cu.execute('''
                        INSERT INTO cosette_execution_result (result, output)
                        VALUES ("%s", "%s")
                        ''' % (cos_result, cos_output.replace('\\', '\\\\').replace('"', '\\"')))
                    cosette_execution_result_id = cu.lastrowid

                    # update the corresponding (accurate_qm_cosette, cosette_execution_result_id) in
                    # accuracy
                    if cos_result == 'EQ':
                        accurate_qm_cosette = '1'
                    elif cos_result == 'NEQ':
                        accurate_qm_cosette = '0'
                    else:
                        accurate_qm_cosette = 'NULL'

                    print_log_message('INFO', ['compute_accuracy_cosette', 'accurate_qm_cosette',
                                               str((experiment_id, query_id)),
                                               accurate_qm_cosette
                                               ])
                    cu.execute('''
                        UPDATE accuracy
                        SET accurate_qm_cosette=%s,
                            cosette_execution_result_id=%d
                        WHERE experiment_id=%d
                          AND query_id=%d
                        ''' % (accurate_qm_cosette, cosette_execution_result_id, experiment_id, query_id))
                    if cu.rowcount == 0:
                        cu.execute('''
                            INSERT INTO accuracy (experiment_id, query_id, accurate_qm_cosette, cosette_execution_result_id)
                            VALUES (%d, %d, %s, %d)
                            ''' % (experiment_id, query_id, accurate_qm_cosette, cosette_execution_result_id))
                dbconn.commit()
                print_log_message('INFO', ['compute_accuracy_cosette', 'inserting accurate_qm_cosette done',
                                           str((experiment_id, query_id))
                                           ])
                num_computed += 1
            print_log_message('INFO', ['compute_accuracy_cosette', 'executing Cosette done'])
        except Exception as e:
            print_log_message('ERROR', ['compute_accuracy_cosette', 'executing Cosette failed', str(e)])
            try:
                dbconn.rollback()
            except:
                pass
    print_log_message('INFO', ['compute_accuracy_cosette', 'done',
                               str(num_computed) + ' query/queries computed'
                               ])


def generate_cosette_template(dbconn):
    print(MESSAGE_HLINE + MESSAGE_BOLD + 'Generating Cosette templates' + MESSAGE_RESET)
    num_created = 0
    try:
        cu = dbconn.cursor()
        for db in DATABASES:
            filename = db + '.template.cos'
            print('Generating ' + filename)
            with open(TEMPLATE_DIR + filename, 'w') as f:
                schemas = ''
                tables = ''

                cu.execute('USE ' + db.replace('-', ''))
                cu.execute('SHOW TABLES')
                result_tables = cu.fetchall()
                for result_table in result_tables:
                    table = result_table[0]
                    cu.execute('DESC ' + table)
                    field_results = cu.fetchall()

                    fields = []
                    for field_result in field_results:
                        field_name = field_result[0].lower()
                        field_type = field_result[1].lower()
                        if 'int' in field_type:
                            field_type = 'int'
                        elif 'varchar' in field_type:
                            field_type = 'text'
                        elif 'text' in field_type:
                            field_type = 'text'
                        # TODO: verify
                        elif 'decimal' in field_type:
                            field_type = 'int'
                        elif 'double' in field_type:
                            field_type = 'int'
                        elif 'float' in field_type:
                            field_type = 'int'
                        else:
                            field_type = 'int'

                        fields.append((field_name, field_type))

                    schema = 'schema schema_' + table + '('
                    for (field_name, field_type) in fields:
                        schema += field_name + ':' + field_type + ', '
                    schema = schema[:-2] + ');\n'
                    schemas += schema
                    tables += 'table ' + table + '(schema_' + table + ');\n'

                f.write(schemas + '\n')
                f.write(tables + '\n')
                f.write('query q1 \n')
                f.write('`${gold_sql}`;\n\n')
                f.write('query q2 \n')
                f.write('`${gen_sql}`;\n\n')
                f.write('verify q1 q2;')
            print(MESSAGE_DONE)
            num_created += 1
        cu.close()
    except Exception(e):
        print('Creating benchmark database ' + MESSAGE_FAILED)
        print(MESSAGE_RED + str(e) + MESSAGE_RESET)
        return
    print(MESSAGE_BOLD + 'Creating benchmark database' + MESSAGE_RESET)
    print('(' + str(num_created) + ' template(s) created)')
