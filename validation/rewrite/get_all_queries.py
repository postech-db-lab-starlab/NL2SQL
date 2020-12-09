#!/usr/bin/python
# -*- coding: utf-8 -*-

import decimal
import json
import MySQLdb
#import pymysql
import os
import re
import sys
from contextlib import closing

reload(sys)
sys.setdefaultencoding('utf-8')

HOST = 'localhost'
USER = 'root'
PASSWD = 'root'

def read_indices(filename):
    with open(filename) as f:
        lines = [l.strip().split('\t') for l in f]
    index_list = [l[0] for l in lines[1:]]
    return index_list

def main(dbconn, dbname, system_name, category, test_idx, write_file):
    with closing(dbconn.cursor()) as cu, open(write_file, 'w') as f:
        print('{}__{}'.format(dbname, system_name))
        gold_sql_column = "gold_sql_execute"
        #if dbname.startswith('wikitablequestions'):
        if dbname == 'wikitablequestions':
            gold_sql_column = "gold_sql_cosette_rename"
            sql = '''
            SELECT DISTINCT Q.query_index, 
                            E.system, 
                            S.category,
                            R.gen_sql, 
                            Q.{}
            FROM query Q
              JOIN accuracy A ON Q.query_id=A.query_id
              JOIN experiment_info E ON E.experiment_id=A.experiment_id
              JOIN query_result R ON E.experiment_id=R.experiment_id AND Q.query_id=R.query_id
              JOIN query_split S ON Q.query_id=S.query_id
              JOIN sql_execution_result SER_gold ON SER_gold.sql_execution_result_id=Q.sql_execution_result_id
              JOIN sql_execution_result SER_gen ON SER_gen.sql_execution_result_id=R.sql_execution_result_id
            WHERE (S.split='test' OR (S.split='dev' AND Q.db='spider'))
              AND (A.accurate_ex = 1
                   OR SER_gold.errno = -1
                   OR SER_gen.errno = -1)
              AND SER_gold.errno <= 0
              AND SER_gen.errno <= 0
              AND S.category = E.category
              AND S.category = '{}'
              AND E.test_data='{}'
              AND E.system = '{}'
              AND S.query_index IN ({})
              AND REPLACE(E.training_data, '-s', '') = Q.db
              AND REPLACE(E.test_data, '-s', '') = Q.db
            ORDER BY 2, 1'''.format(gold_sql_column, category, dbname, system_name, ','.join(test_idx))
        else:
            sql = '''
            SELECT DISTINCT Q.query_index, 
                            E.system, 
                            S.category,
                            R.gen_sql, 
                            Q.{}
            FROM query Q
              JOIN accuracy A ON Q.query_id=A.query_id
              JOIN experiment_info E ON E.experiment_id=A.experiment_id
              JOIN query_result R ON E.experiment_id=R.experiment_id AND Q.query_id=R.query_id
              JOIN query_split S ON Q.query_id=S.query_id
            WHERE (S.split='test' OR (S.split='dev' AND Q.db='spider'))
              AND S.category = E.category
              AND S.category = '{}'
              AND E.test_data='{}'
              AND E.system = '{}'
              AND S.query_index IN ({})
              AND REPLACE(E.training_data, '-s', '') = Q.db
              AND REPLACE(E.test_data, '-s', '') = Q.db
            ORDER BY 2, 1'''.format(gold_sql_column, category, dbname, system_name, ','.join(test_idx))
            #  AND A.accurate_qm IS NULL
        try:
            # db schemas
            cu.execute('''USE benchmark''')
            cu.execute(sql)
            results = cu.fetchall()

            for result in results:
                idx = str(result[0])
                system_name = result[1]
                category = result[2]
                gen_sql = result[3].strip()
                gold_sql = result[4].strip()
                if gen_sql != gen_sql.replace(") tmp", ") as tmp"):
                    gen_sql = gen_sql.replace(") tmp", ") as tmp")
                    #print(gen_sql)
                if gold_sql != gold_sql.replace(") tmp", ") as tmp"):
                    gold_sql = gold_sql.replace(") tmp", ") as tmp")
                    #print(gold_sql)
                datum = [dbname, idx, category, system_name, 'gen_sql', gen_sql]
                f.write('{}\n'.format('\t'.join(datum)))
                datum = [dbname, idx, category, system_name, 'gold_sql', gold_sql]
                f.write('{}\n'.format('\t'.join(datum)))
        except Exception as e:
            print('ERROR')
            print(repr(e))



if __name__ == '__main__':
    with closing(MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, charset='utf8')) as dbconn:
    #with pymysql.connect(host=HOST, user=USER, passwd=PASSWD) as dbconn:
        write_file = sys.argv[1]
        dbname = sys.argv[2]
        category = sys.argv[3]
        test_file = sys.argv[4]
        system_name = sys.argv[5]
        test_idx = read_indices(test_file)
        main(dbconn, dbname, system_name, category, test_idx, write_file)
