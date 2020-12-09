
def load_generated_queries(dbconn, filename):
    print_log_message('INFO', ['load_generated_queries', 'start loading ' + filename])
    num_inserted = 0
    num_updated = 0
    query_ids = []
    try:
        dbconn.begin()
        with closing(dbconn.cursor()) as cu:
            cu.execute('''USE benchmark''')
            with open(filename) as f:
                filename = filename.split('/')[-1]
                filename_split = filename.replace('.', '_').split('_')
                system = filename_split[0]
                training_data = filename_split[1]
                test_data = filename_split[2]
                category = filename_split[3]

                # insert (system, training_data, test_data, category) to experiment_info,
                # and get experiment_id
                cu.execute('''
                    SELECT experiment_id
                    FROM   experiment_info
                    WHERE  system="%s"
                       AND training_data="%s"
                       AND test_data="%s"
                       AND category="%s"
                    ''' % (system, training_data, test_data, category))
                if cu.rowcount == 0:
                    cu.execute('''
                        INSERT INTO experiment_info (system, training_data, test_data, category)
                        VALUES ("%s", "%s", "%s", "%s")
                        ''' % (system, training_data, test_data, category))
                    experiment_id = cu.lastrowid
                else:
                    experiment_id = cu.fetchone()[0]

                next(f)  # ignore the first line
                for line in f:
                    line_split = line.replace('\\', '\\\\').replace('"', '\\"').split('\t')

                    db = line_split[0].lower()
                    if db.endswith('_rename'):
                        db, db_suffix = db.split('_')
                    else:
                        db_suffix = ''
                    query_index = line_split[1]
                    gen_sql = format_sql(line_split[2] if len(line_split) >= 3 else '')
                    gen_sql_execute = format_sql(line_split[3] if len(line_split) >= 4 else '')
                    gen_sql_cosette = format_sql(
                        line_split[4] if len(line_split) >= 5 else gen_sql_execute)

                    # get query_id
                    cu.execute('''
                        SELECT query_id
                        FROM   query_split
                        WHERE  db="%s"
                           AND query_index=%s
                           AND category="%s"
                        ''' % (db, query_index, category))
                    if cu.rowcount == 0:
                        raise Exception('gold query (' + db + ', ' + query_index + ', ' + category + ') not found')
                    else:
                        query_id = cu.fetchone()[0]

                    # insert (experiment_id, query_id, gen_sql, gen_sql_execute, db_suffix) to
                    # query_result
                    cu.execute('''
                        SELECT *
                        FROM   query_result
                        WHERE  experiment_id=%s
                           AND query_id=%s
                        ''' % (experiment_id, query_id))
                    if cu.rowcount == 0:
                        cu.execute('''
                            INSERT INTO query_result (experiment_id, query_id, gen_sql, gen_sql_execute, gen_sql_cosette, db_suffix)
                            VALUES (%s, %s, "%s", "%s", "%s", "%s")
                            ''' % (experiment_id, query_id, gen_sql, gen_sql_execute, gen_sql_cosette, db_suffix))
                        num_inserted += 1
                    else:
                        cu.execute('''
                            UPDATE query_result
                            SET    gen_sql="%s",
                                   gen_sql_execute="%s",
                                   gen_sql_cosette="%s",
                                   db_suffix="%s"
                            WHERE  experiment_id=%s
                               AND query_id=%s
                            ''' % (gen_sql, gen_sql_execute, gen_sql_cosette, db_suffix, experiment_id, query_id))
                        num_updated += 1
                    query_ids.append(query_id)
        dbconn.commit()
    except Exception as e:
        print_log_message('ERROR', ['load_generated_queries', 'loading failed', str(e)])
        try:
            dbconn.rollback()
        except:
            pass
    print_log_message('INFO', ['load_generated_queries', 'done',
                               str(num_inserted) + ' query/queries inserted',
                               str(num_updated) + ' query/queries updated',
                               ])
    return experiment_id, system, query_ids
