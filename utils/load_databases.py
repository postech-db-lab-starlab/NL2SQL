

def load_mysql_dump(dbconn, dbname, mysqldumpname, mysqldumppath, drop=False):
    try:
        with closing(dbconn.cursor()) as cu:
            # check if db exists
            cu.execute('''SHOW DATABASES LIKE "''' + dbname + '"')
            if cu.rowcount != 0:
                # drop the db
                # cu.execute('DROP DATABASE ' + db)

                # continue if db exists
                if drop:
                    if dbname in DATABASES:
                        raise Exception('You cannot drop ' + dbname)
                    cu.execute('''DROP DATABASE ''' + dbname)
                else:
                    raise Exception(dbname + ' already exists')

            # create db
            cu.execute('''CREATE DATABASE ''' + dbname)

            # load db
            with open(mysqldumppath + mysqldumpname + '.mysqldump') as f:
                subprocess.call(['mysql', '-u', USER, '-p' + PASSWD, '-h', HOST, dbname], stdin=f)
    except Exception as e:
        print
        MESSAGE_FAILED
        print
        MESSAGE_RED + str(e) + MESSAGE_RESET
        return
    print
    MESSAGE_DONE


def load_mysql_dumps_to_tmpdb(dbconn):
    # print_log_message('INFO', ['load_mysql_dumps_to_tmpdb', '[SKIP] create database '+TMP_DATABASE_NAME])
    print_log_message('INFO', ['load_mysql_dumps_to_tmpdb', 'create database ' + TMP_DATABASE_NAME])
    load_mysql_dump(dbconn, TMP_DATABASE_NAME, 'schema', TMP_DATA_PATH, drop=True)


def load_mysql_dumps(dbconn):
    # TODO: outdated, slow
    print
    MESSAGE_HLINE + MESSAGE_BOLD + 'Loading MySQL dump files' + MESSAGE_RESET
    num_loaded = 0
    for db in DATABASES:
        db = db.replace('-', '')
        print
        'Loading ' + db
        load_mysql_dump(dbconn, db, db, MYSQL_DUMP_DIR)
        num_loaded += 1
    print
    MESSAGE_BOLD + 'Loading MySQL dump files' + MESSAGE_RESET,
    print
    '(' + str(num_loaded) + ' file(s) loaded)'
