#!/usr/bin/python
# -*- coding: utf-8 -*-
import decimal
import time
import datetime
import simplejson as json
import MySQLdb
import sqlite3
import os
import re
import subprocess
import sys
import traceback
from collections import Counter
from contextlib import closing
from Cosette import solver
from itertools import izip, product, permutations
from string import Template
import argparse
import shutil
import warnings
import csv
import requests

reload(sys)
sys.setdefaultencoding('utf8')

HOST = 'localhost'
USER = 'root'
PASSWD = 'root'

USE_TEST_DATA_GEN = False
TMP_DATA_PATH = None
TMP_DATABASE_NAME = 'databasetmp'
# TIMEOUT = 1000 * 1000
TIMEOUT = 30 * 1000

COSETTE_API_KEY = '87e29bc3086947aac67af14b3df6a1e0'

MYSQL_DUMP_DIR = './dataset/mysql_dump/'
DATABASES = [
    'advising-querysplit',
    'advising-querysplit_rename',
    'advising-questionsplit',
    'advising-questionsplit_rename',
    'atis',
    'atis_rename',
    'geo',
    'geo_rename',
    'imdb',
    'imdb_rename',
    'mas',
    'patients',
    'patients_rename',
    'restaurant',
    'scholar',
    'wikisql',
    'wikitablequestions',
    'yelp',
    'yelp_rename',
]

GOLD_QUERY_DIR = './dataset_todo/gold_queries/'
LOG_DIR = './dataset_todo/logs/'
TEMPLATE_DIR = './cosette_template/'

MESSAGE_HLINE = '--------------------------------------------------------------------------------\n'
MESSAGE_BOLD = '\033[1m'
MESSAGE_RED = '\033[31m'
MESSAGE_GREEN = '\033[32m'
MESSAGE_YELLOW = '\033[33m'
MESSAGE_RESET = '\033[0m'
MESSAGE_DONE = '[' + MESSAGE_BOLD + MESSAGE_GREEN + 'DONE' + MESSAGE_RESET + ']'
MESSAGE_STOPPED = '[' + MESSAGE_BOLD + MESSAGE_YELLOW + 'STOPPED' + MESSAGE_RESET + ']'
MESSAGE_FAILED = '[' + MESSAGE_BOLD + MESSAGE_RED + 'FAILED' + MESSAGE_RESET + ']'

CREATE_BENCHMARK_TABLE_SQLS = None

def get_db_name(dbname):
    if USE_TEST_DATA_GEN:
        return TMP_DATABASE_NAME
    return dbname.replace('-', '')

def get_sqlite3_execute_result(query):
    spider_dbname = []
    query_toks = query.split()
    for idx, tok in enumerate(query_toks):
        if '__' in tok:
            dbname, table_name = tok.split('__')
            spider_dbname.append(dbname)
            query_toks[idx] = table_name
    query = ' '.join(query_toks)
    if len(query_toks) == 0:
        raise Exception("No query exists")
    elif len(spider_dbname) == 0:
        raise Exception("Cannot find spider dbname")
    elif len(set(spider_dbname)) > 1:
        raise Exception("Too many spider dbname")
    spider_dbname = spider_dbname[0]

    sqlite_db_dir = '/mnt/disk1/Benchmark_RA/in_progress/data/spider/origin/database/'
    for dirname in os.listdir(sqlite_db_dir):
        if dirname.lower() == spider_dbname:
            spider_dbname = dirname
            break
    sqlite_db_path = sqlite_db_dir + '{db}/{db}.sqlite'.format(db=spider_dbname)
    conn = sqlite3.connect(sqlite_db_path)
    conn.text_factory = lambda x: str(x).decode('utf8', errors='ignore')
    cu = conn.cursor()
    cu.execute(query)
    output = cu.fetchall()
    conn.close()
    return output

def create_benchmark_db(dbconn):
    print_log_message('INFO', ['create_benchmark_db', 'called'])
    num_created = 0
    if not CREATE_BENCHMARK_TABLE_SQLS:
        print_log_message('ERROR', ['create_benchmark_db', 'SQL does not exist'])
        return

    try:
        with closing(dbconn.cursor()) as cu:
            # cu.execute('''DROP DATABASE IF EXISTS benchmark''')
            cu.execute('''CREATE DATABASE benchmark''')
            cu.execute('''USE benchmark''')
            for sql in CREATE_BENCHMARK_TABLE_SQLS:
                cu.execute(sql)
                num_created += 1
    except Exception as e:
        print_log_message('ERROR', ['create_benchmark_db', str(e)])
        return
    print_log_message('INFO', ['create_benchmark_db', 'done', str(num_created) + ' table(s) created'])

def insert_accuracy(dbconn, filename):
    print_log_message('INFO', ['insert_accuracy', 'start loading ' + filename])
    num_inserted = 0
    num_updated = 0
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
                print("INFO: {}, {}, {}, {}".format(system, training_data, test_data, category))

                # get experiment_id
                cu.execute('''
                    SELECT experiment_id
                    FROM   experiment_info
                    WHERE  system="%s"
                       AND training_data="%s"
                       AND test_data="%s"
                       AND category="%s"
                    ''' % (system, training_data, test_data, category))
                results = cu.fetchall()
                if results:
                    experiment_id = results[0][0]
                else:
                    cu.execute('''
                        INSERT INTO experiment_info (system, training_data, test_data, category)
                        VALUES ("%s", "%s", "%s", "%s")
                        ''' % (system, training_data, test_data, category))
                    experiment_id = cu.lastrowid

                # get column info
                columns = next(f)[:-1].replace('correctness_', 'accurate_').split('\t')[2:]
                print("INFO: {}".format(columns))
                # insert rows
                for line in f:
                    line_split = line[:-1].split('\t')
                    db = line_split[0].lower()
                    if db.endswith('_rename'):
                        db = db.split('_')[0]
                    query_index = line_split[1]
                    accurates = line_split[2:]

                    # get query_id
                    cu.execute('''
                        SELECT query_id
                        FROM   query_split
                        WHERE  db="%s"
                           AND query_index=%s
                           AND category="%s"
                        ''' % (db, query_index, category))
                    results = cu.fetchall()
                    if results:
                        query_id = results[0][0]
                    else:
                        raise Exception(
                            'gold query (' + db + ', ' + query_index + ', ' + category + ') not found')
                    # insert a row into accuracy
                    cu.execute('''
                        SELECT experiment_id
                        FROM   accuracy
                        WHERE  experiment_id=%d AND query_id=%d
                        ''' % (experiment_id, query_id))
                    if cu.rowcount == 0:
                        column_names_str = ''.join(', ' + col for col in columns)
                        accurate_values_str = ''.join(', ' + acc for acc in accurates)
                        cu.execute('''
                            INSERT INTO accuracy (experiment_id, query_id''' + column_names_str + ''')
                            VALUES (''' + str(experiment_id) + ', ' + str(query_id) + accurate_values_str + ')')
                        num_inserted += 1
                    else:
                        sets = ',\n'.join(col + '=' + acc for col, acc in zip(columns, accurates))
                        print("INFO: {}, {}, {}".format(sets, experiment_id, query_id))
                        cu.execute('''
                            UPDATE accuracy
                            SET    ''' + sets + '''
                            WHERE  experiment_id=''' + str(experiment_id) + ''' AND query_id=''' + str(query_id))
                        num_updated += 1

        dbconn.commit()
    except Exception as e:
        print_log_message('ERROR', ['insert_accuracy', 'loading failed', str(e)])
        try:
            dbconn.rollback()
            cu.close()
        except:
            pass
    print_log_message('INFO', ['insert_accuracy', 'done',
                               str(num_inserted) + ' query/queries inserted',
                               str(num_updated) + ' query/queries updated',
                               ])

def insert_from_local_file(dbconn, command, dbname):
    with closing(dbconn.cursor()) as cu:
        print_log_message('INFO', ['compute_accuracy_ex', command])
        while 1:
            cu.execute(command)
            cu.execute("show warnings")
            warnings = cu.fetchall()

            # handle foreign key exception
            foreign_keys = {}
            need_to_solve_foreign_key = False
            for msg in warnings:
                print_log_message('INFO', ['compute_accuracy_ex', 'WARNING {}'.format(msg[2])])
                if msg[2].find('Cannot add or update') is not -1 and msg[2].find('REFERENCES') is not -1:
                    foreign_tablename = msg[2][msg[2].find('REFERENCES') + 11:msg[2].find('(') - 1]
                    foreign_schema = msg[2][msg[2].find('REFERENCES') + 11:]
                    foreign_tablename = foreign_schema[1:foreign_schema.find('(')].strip()[:-1]
                    foreign_columnname = foreign_schema[
                                         foreign_schema.find('(') + 2:foreign_schema.find(')') - 1].strip()
                    my_columnname = msg[2][msg[2].find('FOREIGN KEY') + 14:].split(')')[0][:-1]

                    if foreign_tablename in foreign_keys or foreign_columnname.replace(' ', '').find("`,") is not -1:
                        print_log_message('INFO', ['compute_accuracy_ex',
                                                   'WARNING {}, {} - Multiple foreign keys from one table currently not supported'.format(
                                                       foreign_tablename, foreign_columnname)])
                        need_to_solve_foreign_key = False
                        break
                    keyMap = [my_columnname, foreign_columnname]
                    foreign_keys[foreign_tablename] = keyMap
                    need_to_solve_foreign_key = True
            if not need_to_solve_foreign_key:
                break
            else:
                for table, [my_column, foreign_column] in foreign_keys.items():
                    # GET VALUES from tsv file
                    filename = command[:command.find("tsv") + 3]
                    filename = filename[filename.find("INFILE") + 8:]
                    my_column_list = command[command.find("\\n") + 5:].strip()[:-2].lower().split(',')
                    my_index = my_column_list.index(my_column.lower())
                    with open(filename) as tsvfile:
                        tsvreader = csv.reader(tsvfile, delimiter="\t")
                        valueSet = set()
                        for line in tsvreader:
                            try:
                                valueSet.add(int(line[my_index]))
                            except:
                                raise Exception("String key currently not supported")
                    for value in valueSet:
                        cu.execute('''USE ''' + dbname)
                        cu.execute('''
                      INSERT INTO %s (%s)
                      VALUES (%d) ''' % (table, foreign_column, value))
                        print('''
                      INSERT INTO %s (%s)
                      VALUES (%d) ''' % (table, foreign_column, value))

def compute_accuracy_ex(dbconn, experiment_id, target_query_ids=None, restore_prev=False, is_IRNet=False):
    num_computed = 0

    # select non-computed results
    compute_results = True
    print_log_message('INFO', ['compute_accuracy_ex', 'start selecting query_id\'s'])
    try:
        with closing(dbconn.cursor()) as cu:
            cu.execute('''USE benchmark''')

            # select (experiment_id, query_id) pairs to compute the accuracy
            if target_query_ids:
                select_results = [(query_id,) for query_id in target_query_ids]
            else:
                cu.execute('''
                    SELECT qr.query_id
                    FROM   query_result qr
                    WHERE  qr.experiment_id=%d
                    ''' % (experiment_id))
                select_results = cu.fetchall()
    except MySQLdb.Error as e:
        print_log_message('ERROR', ['compute_accuracy_ex', 'selecting query_id\'s failed', str(e)])
        compute_results = False
        select_results = []
    print_log_message(
        'INFO',
        ['compute_accuracy_ex', 'selecting query_id\'s done', str(len(select_results)) + ' query/queries found'])

    # compute the results
    if compute_results:
        print_log_message('INFO', ['compute_accuracy_ex', 'start executing SQLs'])
        print
        'Computing results'
        try:
            is_first_tmp_execute = True
            for select_result in select_results:
                query_id = select_result[0]
                if USE_TEST_DATA_GEN:
                    current_insert_dir = TMP_DATA_PATH + "Q" + str(query_id)
                    if not os.path.isdir(current_insert_dir):
                        print_log_message('INFO',
                                          ['compute_accuracy_ex', 'Directory {} DOES NOT EXIST'.format(query_id)])
                        continue
                    else:
                        if os.path.isdir('./tmp'):
                            shutil.rmtree('./tmp')
                        shutil.copytree(current_insert_dir, './tmp')

                        current_insert_file = "./tmp/INSERTQUERY.sql"
                        if not os.path.exists(current_insert_file):
                            print_log_message('INFO', ['compute_accuracy_ex',
                                                       'File {} DOES NOT EXIST'.format(current_insert_file)])
                            continue

                        # load tmp db
                        # if is_first_tmp_execute or 'wikitablequestions' not in TMP_DATA_PATH:
                        if is_first_tmp_execute or ('wiki' not in TMP_DATA_PATH and 'spider' not in TMP_DATA_PATH):
                            is_first_tmp_execute = False
                            load_mysql_dumps_to_tmpdb(dbconn)

                        # insert rows
                        for line in open(current_insert_file):
                            insert_from_local_file(dbconn, line.strip(), TMP_DATABASE_NAME)

                dbconn.begin()

                with closing(dbconn.cursor()) as cu:
                    cu.execute('''USE benchmark''')

                    # select db and queries
                    cu.execute('''
                        SELECT query.db,
                               query_result.db_suffix,
                               query.gold_sql_execute,
                               query_result.gen_sql_execute,
                               query.sql_execution_result_id,
                               query_result.sql_execution_result_id,
                               query.sql_execution_result_id_tmp_data,
                               query_result.sql_execution_result_id_tmp_data
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
                    gold_sql_execute = select_result[2]
                    gen_sql_execute = select_result[3]
                    gold_sql_execution_result_id = select_result[4]
                    gen_sql_execution_result_id = select_result[5]
                    gold_sql_execution_result_id_tmp_data = select_result[6]
                    gen_sql_execution_result_id_tmp_data = select_result[7]

                    # time limit
                    if db.startswith('spider'):
                        gold_sql_execute = gold_sql_execute.encode('utf8')
                        gen_sql_execute = gen_sql_execute.encode('utf8')
                    else:
                        gold_sql_execute = re.sub(
                            '(SELECT |select )', 'SELECT /*+ MAX_EXECUTION_TIME(' + str(TIMEOUT) + ') */ ',
                            gold_sql_execute, count=1)
                        gen_sql_execute = re.sub(
                            '(SELECT |select )', 'SELECT /*+ MAX_EXECUTION_TIME(' + str(TIMEOUT) + ') */ ',
                            gen_sql_execute, count=1)

                    if is_IRNet == True:
                        p = re.compile(" *distinct *", re.I)
                        gold_sql_execute = p.sub(r' ', gold_sql_execute)
                        gen_sql_execute = p.sub(r' ', gen_sql_execute)
                    print_log_message('INFO', ['compute_accuracy_ex', 'SQLs to execute',
                                               str((experiment_id, query_id)),
                                               gold_sql_execute.encode('utf8'),
                                               gen_sql_execute.encode('utf8')
                                               ])

                    gold_output_too_large = False
                    gold_errno = 0
                    if gold_sql_execution_result_id and not USE_TEST_DATA_GEN:
                        # retrieve the gold query execution result
                        cu.execute('''USE benchmark''')
                        cu.execute('''
                            SELECT output,
                                   errno
                            FROM   sql_execution_result
                            WHERE  sql_execution_result_id=%d
                            ''' % (gold_sql_execution_result_id,))
                        gold_output_json, gold_errno = cu.fetchone()
                        gold_output_too_large = gold_output_json == 'Too large'
                        if not gold_output_too_large:
                            try:
                                gold_output = json.loads(
                                    gold_output_json, use_decimal=True, encoding='utf-8')
                            except:
                                gold_errno = 1000
                    if (
                    not gold_sql_execution_result_id) or USE_TEST_DATA_GEN or gold_output_too_large or gold_errno != 0 or gold_output == [] or gold_output == [
                        [0]] or restore_prev:
                        # execute the gold query
                        gold_output_too_large = False
                        if db.startswith('spider'):
                            gold_output = get_sqlite3_execute_result(gold_sql_execute)
                            gold_rowcount = len(gold_output)
                            if gold_rowcount > 500:
                                gold_output_too_large = True
                            gold_output_json = json.dumps(
                                gold_output, use_decimal=True, encoding='utf-8', default=str)
                            gold_errno = 0
                        else:
                            # if db.lower().startswith('wikitablequestionsnull'):
                            #    db = 'wikitablequestionsnull_rename'
                            try:
                                cu.execute('''USE ''' + get_db_name(db))
                                cu.execute("SET NAMES utf8")
                                cu.execute("SET collation_connection = 'utf8_general_ci'")
                                cu.execute(gold_sql_execute)
                                gold_output = cu.fetchall()
                                gold_rowcount = cu.rowcount
                                if gold_rowcount > 500:
                                    gold_output_too_large = True
                                gold_output_json = json.dumps(
                                    gold_output, use_decimal=True, encoding='utf-8', default=str)
                                gold_errno = 0
                            except MySQLdb.Error as e:
                                gold_rowcount = 0
                                gold_errno = e.args[0]
                                gold_output = e.args[1]
                                gold_output_json = json.dumps(
                                    gold_output, use_decimal=True, encoding='utf-8', default=str)
                            if gold_errno == 1065:
                                print_log_message('INFO', ['compute_accraucy_ex', 'executing gold SQL wrong',
                                                           str(gold_sql_execute)])
                    print_log_message('INFO', ['compute_accuracy_ex',
                                               'executing gold SQL done against {}'.format(get_db_name(db)),
                                               str((experiment_id, query_id)),
                                               str(gold_errno)
                                               ])

                    # renamed DB
                    if db_suffix:
                        db_rename = db + '_' + db_suffix
                    else:
                        db_rename = db
                    if db.lower().startswith('wikitablequestionsnull'):
                        db_rename = 'wikitablequestionsnull_rename'

                    gen_errno = 0
                    gen_output_too_large = False
                    if gen_sql_execution_result_id and not USE_TEST_DATA_GEN:
                        # retrieve the gen query execution result
                        cu.execute('''USE benchmark''')
                        cu.execute('''
                            SELECT output,
                                   errno
                            FROM   sql_execution_result
                            WHERE  sql_execution_result_id=%d
                            ''' % (gen_sql_execution_result_id,))
                        gen_output_json, gen_errno = cu.fetchone()
                        gen_output_too_large = gen_output_json == 'Too large'
                        if not gen_output_too_large:
                            try:
                                gen_output = json.loads(
                                    gen_output_json, use_decimal=True, encoding='utf-8')
                            except:
                                gen_errno = 1000
                    if (
                    not gen_sql_execution_result_id) or USE_TEST_DATA_GEN or gen_output_too_large or gen_errno != 0 or gen_output == [] or gen_output == [
                        [0]] or restore_prev:
                        # execute generated query
                        gen_output_too_large = False
                        if db.startswith('spider'):
                            try:
                                gen_output = get_sqlite3_execute_result(gen_sql_execute)
                                gen_rowcount = len(gen_output)
                                if gen_rowcount > 500:
                                    gen_output_too_large = True
                                gen_output_json = json.dumps(
                                    gen_output, use_decimal=True, encoding='utf-8', default=str)
                                gen_errno = 0
                            # except sqlite3.ProgrammingError as e:
                            except Exception as e:
                                # print(type(e))
                                # print(e)
                                gen_rowcount = 0
                                gen_errno = 9999
                                gen_output = e.args[0]
                                gen_output_json = json.dumps(
                                    gen_output, use_decimal=True, encoding='utf-8', default=str)
                        else:
                            try:
                                cu.execute('''USE ''' + get_db_name(db_rename))
                                cu.execute("SET NAMES utf8")
                                cu.execute("SET collation_connection = 'utf8_general_ci'")
                                cu.execute(gen_sql_execute)
                                gen_rowcount = cu.rowcount
                                if gen_rowcount > 500:
                                    gen_output_too_large = True
                                gen_output = cu.fetchall()
                                gen_output_json = json.dumps(
                                    gen_output, use_decimal=True, encoding='utf-8', default=str)
                                gen_errno = 0
                            except MySQLdb.Error as e:
                                gen_rowcount = 0
                                gen_errno = e.args[0]
                                gen_output = e.args[1]
                                gen_output_json = json.dumps(
                                    gen_output, use_decimal=True, encoding='utf-8', default=str)

                    print_log_message(
                        'INFO', ['compute_accuracy_ex',
                                 'executing generated SQL done against {}'.format(get_db_name(db_rename)),
                                 str((experiment_id, query_id)),
                                 str((experiment_id, query_id)),
                                 str(gen_errno)
                                 ])

                    # check if the run failed
                    sql_error = gold_errno != 0 or gen_errno != 0

                    # check 'ORDER BY'
                    ordered_result = any('order by' in sql.lower()
                                         for sql in [gold_sql_execute, gen_sql_execute])

                    # format output
                    def lower_str(row):
                        return [v.lower() if isinstance(v, unicode) or isinstance(v, str) else v for v in row]

                    def pack_column(table, col_index):
                        return zip(*table)[col_index]

                    gold_output = tuple(tuple(lower_str(row)) for row in gold_output)
                    gen_output = tuple(tuple(lower_str(row)) for row in gen_output)

                    # compute accurate_ex
                    if gold_errno != 0 and gen_errno <= 0:
                        accurate_ex = 'NULL'  # wrong gold SQL
                    elif gen_errno > 0:
                        accurate_ex = '0'  # wrong generated SQL
                    elif len(gold_output) == 0 and len(gen_output) == 0:
                        accurate_ex = '1'  # empty results
                    elif len(gold_output) == 0 or len(gen_output) == 0:
                        accurate_ex = '0'  # wrong execution results
                    elif ordered_result:
                        print_log_message(
                            'INFO', ['compute_accuracy_ex', 'SQLs contain \'order by\'',
                                     str((experiment_id, query_id))
                                     ])
                        gold_cols = tuple(tuple(pack_column(gold_output, i) for i in range(len(gold_output[0]))))
                        gen_cols = tuple(tuple(pack_column(gen_output, i) for i in range(len(gen_output[0]))))
                        print('{}, {}'.format(Counter(gold_cols), Counter(gen_cols)))
                        accurate_ex = '1' if Counter(gold_cols) == Counter(gen_cols) else '0'

                    # accurate_ex = '1' if gold_output == gen_output else '0'  # compare results as sequence
                    else:
                        # print('{}\n\n{}'.format(gold_output, gen_output))
                        gold_cols = tuple(pack_column(gold_output, i) for i in range(len(gold_output[0])))
                        gen_cols = tuple(pack_column(gen_output, i) for i in range(len(gen_output[0])))
                        if len(gold_cols) != len(gen_cols) or len(gold_output) != len(gen_output):
                            accurate_ex = '0'
                        elif len(gold_cols) == 0:
                            accurate_ex = '1'
                        else:
                            row_maps = [[] for i in range(len(gold_cols))]
                            for i in range(len(gen_cols)):
                                for j in range(len(gold_cols)):
                                    if Counter(gen_cols[i]) == Counter(gold_cols[j]):
                                        row_maps[j].append(i)
                            permus = [permu for permu in
                                      permutations([i for i in range(len(gold_cols))], len(gold_cols))]
                            mappings = list(mapping for mapping in product(*row_maps) if mapping in permus)
                            accurate_ex = '0'
                            for mapping in mappings:
                                gen_cols_permus = tuple(gen_cols[i] for i in mapping)
                                gen_output_permus = tuple(
                                    pack_column(gen_cols_permus, i) for i in range(len(gen_cols_permus[0])))
                                if Counter(gen_output_permus) == Counter(gold_output):
                                    accurate_ex = '1'
                                    break

                                    #   accurate_ex = '1' if Counter(gold_output) == Counter(
                    #       gen_output) else '0'  # compare results as bag

                    print_log_message('INFO', ['compute_accuracy_ex', 'accurate_ex',
                                               str((experiment_id, query_id)),
                                               accurate_ex
                                               ])
                    accurate_ex_col_name = "accurate_ex"
                    sql_execution_result_id_col_name = "sql_execution_result_id"
                    if USE_TEST_DATA_GEN:
                        accurate_ex_col_name = "accurate_ex_tmp_data"
                        sql_execution_result_id_col_name = "sql_execution_result_id_tmp_data"

                    # update accuracy
                    cu.execute('''USE benchmark''')
                    cu.execute('''
                        SELECT * FROM accuracy
                        WHERE  experiment_id=%d
                           AND query_id=%d
                        ''' % (experiment_id, query_id))

                    if cu.rowcount == 0:
                        cu.execute('''
                            INSERT INTO accuracy (experiment_id, query_id, %s)
                            VALUES (%d, %d, %s)
                            ''' % (accurate_ex_col_name, experiment_id, query_id, accurate_ex))
                    else:
                        cu.execute('''
                        UPDATE accuracy
                        SET    %s=%s
                        WHERE  experiment_id=%d
                           AND query_id=%d
                        ''' % (accurate_ex_col_name, accurate_ex, experiment_id, query_id))

                    print_log_message(
                        'INFO', ['compute_accuracy_ex', 'updating accuracy_ex done',
                                 str((experiment_id, query_id))
                                 ])
                    # delete previous gold sql execution result
                    if gold_sql_execution_result_id and not USE_TEST_DATA_GEN:
                        cu.execute('''
                           DELETE FROM sql_execution_result
                           WHERE  sql_execution_result_id=%d
                           ''' % (gold_sql_execution_result_id,))
                    if gold_sql_execution_result_id_tmp_data and USE_TEST_DATA_GEN:
                        cu.execute('''
                           DELETE FROM sql_execution_result
                           WHERE  sql_execution_result_id=%d
                           ''' % (gold_sql_execution_result_id_tmp_data,))

                    # insert (gold_output, gold_errno) to sql_execution_result, and get
                    # sql_execution_result_id
                    if gold_output_too_large:
                        gold_output_json = "Too large"
                    cu.execute('''
                        INSERT INTO sql_execution_result (output, errno)
                        VALUES ("%s", %d)
                        ''' % (gold_output_json.replace('\\', '\\\\').replace('"', '\\"'), gold_errno))
                    gold_sql_execution_result_id = cu.lastrowid

                    # update the corresponding executed_result_id in query_result
                    cu.execute('''
                        UPDATE query
                        SET %s=%d
                        WHERE query_id=%d
                        ''' % (sql_execution_result_id_col_name, gold_sql_execution_result_id, query_id))

                    # delete previous generated sql execution result
                    if gen_sql_execution_result_id and not USE_TEST_DATA_GEN:
                        cu.execute('''
                           DELETE FROM sql_execution_result
                           WHERE  sql_execution_result_id=%d
                           ''' % (gen_sql_execution_result_id,))

                    if gen_sql_execution_result_id_tmp_data and USE_TEST_DATA_GEN:
                        cu.execute('''
                           DELETE FROM sql_execution_result
                           WHERE  sql_execution_result_id=%d
                           ''' % (gen_sql_execution_result_id_tmp_data,))

                    # insert (gen_output, gen_errno) to sql_execution_result, and get
                    # sql_execution_result_id
                    if gen_output_too_large:
                        gen_output_json = "Too large"
                    cu.execute('''
                        INSERT INTO sql_execution_result (output, errno)
                        VALUES ("%s", %d)
                        ''' % (gen_output_json.replace('\\', '\\\\').replace('"', '\\"'), gen_errno))
                    gen_sql_execution_result_id = cu.lastrowid

                    # update the corresponding executed_result_id in query_result
                    cu.execute('''
                        UPDATE query_result
                        SET %s=%d
                        WHERE experiment_id=%d AND query_id=%d
                        ''' % (sql_execution_result_id_col_name, gen_sql_execution_result_id, experiment_id, query_id))

                    dbconn.commit()
                    print_log_message('INFO', ['compute_accuracy_ex', 'inserting SQL results done',
                                               str((experiment_id, query_id))
                                               ])
                    num_computed += 1
            print_log_message('INFO', ['compute_accuracy_ex', 'executing SQLs done'])
        except Exception as e:
            print_log_message('ERROR', ['compute_accuracy_ex', 'executing SQLs failed', str(e)])
            try:
                dbconn.rollback()
            except:
                pass
    print_log_message('INFO', ['compute_accuracy_ex', 'done',
                               str(num_computed) + ' query/queries computed'
                               ])

