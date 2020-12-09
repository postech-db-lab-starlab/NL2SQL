from utils.utils import *

def load_gold_queries(dbconn):
    print_log_message('INFO', ['load_gold_queries', 'called'])
    num_inserted = 0
    num_updated = 0
    for filename in os.listdir(GOLD_QUERY_DIR):
        print_log_message('INFO', ['load_gold_queries', 'start loading ' + filename])
        if not filename.endswith('.tsv'):
            print_log_message('INFO', ['load_gold_queries', filename + ' not ends with \'.tsv\''])
            continue

        num_inserted_tmp = 0
        num_updated_tmp = 0
        try:
            category = filename.split('_')[1]
            if filename.endswith('_test.tsv'):
                split = "test"
            elif filename.endswith('_train.tsv'):
                split = "train"
            elif filename.endswith('_dev.tsv'):
                split = "dev"
            else:
                raise Exception('no split suffix: ' + filename)

            dbconn.begin()
            with closing(dbconn.cursor()) as cu:
                cu.execute('''USE benchmark''')

                with open(GOLD_QUERY_DIR + filename) as f:
                    next(f)  # ignore the first line
                    for line in f:
                        line_split = line.replace("\\", "\\\\").replace('\"', '\\"').split('\t')

                        # check if there are five columns
                        if len(line_split) < 5:
                            raise Exception('invalid line: ' + line)

                        db = line_split[0].lower()
                        query_index = line_split[1]
                        nl = line_split[3]
                        gold_sql = format_sql(line_split[2])
                        gold_sql_cosette = format_sql(line_split[4])
                        gold_sql_cosette_rename = format_sql(line_split[5])
                        gold_sql_execute = format_sql(line_split[6])

                        # insert to query and query_split
                        cu.execute('''
                            SELECT S.query_id,
                                   Q.gold_sql_execute
                            FROM   query_split S,
                                   query Q
                            WHERE  S.db="%s"
                               AND S.query_id=Q.query_id
                               AND S.query_index=%s
                               AND S.category="%s"
                            ''' % (db, query_index, category))
                        if cu.rowcount == 0:
                            cu.execute('''
                                INSERT INTO query (db, query_index, nl, gold_sql, gold_sql_cosette, gold_sql_cosette_rename, gold_sql_execute)
                                VALUES ("%s", %s, "%s", "%s", "%s", "%s", "%s")
                                ''' % (
                            db, query_index, nl, gold_sql, gold_sql_cosette, gold_sql_cosette_rename, gold_sql_execute))
                            query_id = cu.lastrowid

                            cu.execute('''
                                INSERT INTO query_split (query_id, db, query_index, split, is_simple, category)
                                VALUES (%s, "%s", %s, "%s", NULL, "%s")
                                ''' % (query_id, db, query_index, split, category))
                            num_inserted_tmp += 1
                        else:
                            query_id, old_gold_sql_execute = cu.fetchone()
                            #   show='''
                            #       UPDATE query
                            #       SET    db="%s",
                            #              query_index=%s,
                            #              nl="%s",
                            #              gold_sql="%s",
                            #              gold_sql_cosette="%s",
                            #              gold_sql_cosette_rename="%s",
                            #              gold_sql_execute="%s"
                            #       WHERE  query_id=%s''' % (db, query_index, nl, gold_sql, gold_sql_cosette, gold_sql_cosette_rename, gold_sql_execute, query_id)
                            #   print(show)
                            old_gold_sql_execute = old_gold_sql_execute.replace("\\", "\\\\").replace('\"', '\\"')
                            if old_gold_sql_execute.strip() == gold_sql_execute.strip():
                                cu.execute('''
                                    UPDATE query
                                    SET    db="%s",
                                           query_index=%s,
                                           nl="%s",
                                           gold_sql="%s",
                                           gold_sql_cosette="%s",
                                           gold_sql_cosette_rename="%s",
                                           gold_sql_execute="%s"
                                    WHERE  query_id=%s
                                    ''' % (db, query_index, nl, gold_sql, gold_sql_cosette, gold_sql_cosette_rename,
                                           gold_sql_execute, query_id))
                            else:
                                cu.execute('''
                                    UPDATE query
                                    SET    db="%s",
                                           query_index=%s,
                                           nl="%s",
                                           gold_sql="%s",
                                           gold_sql_cosette="%s",
                                           gold_sql_cosette_rename="%s",
                                           gold_sql_execute="%s",
                                           sql_execution_result_id=null
                                    WHERE  query_id=%s
                                    ''' % (db, query_index, nl, gold_sql, gold_sql_cosette, gold_sql_cosette_rename,
                                           gold_sql_execute, query_id))

                            # cu.execute('''
                            #    UPDATE query_split
                            #    SET    db="%s",
                            #           query_index=%s,
                            #           split="%s",
                            #           is_simple=NULL,
                            #           category="%s"
                            #    WHERE  query_id=%s
                            #    ''' % (db, query_index, split, category, query_id))
                            num_updated_tmp += 1

            dbconn.commit()
        except Exception as e:
            print_log_message(
                'ERROR', ['load_gold_queries', 'loading ' + filename + ' failed', str(e)])
            try:
                dbconn.rollback()
            except:
                pass
            continue
        print_log_message('INFO', ['load_gold_queries', 'loading ' + filename + ' done',
                                   str(num_inserted_tmp) + ' query/queries inserted',
                                   str(num_updated_tmp) + ' query/queries updated',
                                   ])
        num_inserted += num_inserted_tmp
        num_updated += num_updated_tmp
    print_log_message('INFO', ['load_gold_queries', 'loading done',
                               str(num_inserted) + ' query/queries inserted',
                               str(num_updated) + ' query/queries updated',
                               ])

