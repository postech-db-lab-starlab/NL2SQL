from os import listdir
from os.path import isfile, join
import sys
from collections import defaultdict
import itertools
import signal
import pymysql


def fill_null(cur, systemname, dbname, category, is_test=False):
    sql = '''
    UPDATE accuracy
    SET accurate_qm_db2 = NULL
    WHERE experiment_id IN
        (SELECT experiment_id
         FROM experiment_info
         WHERE system='{system}'
            AND training_data='{db}'
            AND test_data='{db}'
            AND category='{category}')
      AND query_id IN
        (SELECT query_id
         FROM query_split
         WHERE db='{db}'
            AND split='test'
            AND category='{category}')
    '''.format(system=systemname, db=dbname, category=category)
    if is_test:
        print(sql)
    else:
        cur.execute(sql)


def update_accuracy(cur, filename, info):
    with open(filename) as f:
        header = f.readline().strip()
        lines = [l.strip().split('\t') for l in f]
    ox_dic = {'O': 1, 'X': 0, '1': 1, '0': 0}
    acc_db2 = {int(l[1]): int(ox_dic[l[2]]) for l in lines}
    
    cnt = 0
    info = info.copy()
    print("UPDATE {} items".format(len(acc_db2)))
    for key, val in acc_db2.items():
        info['idx'] = key
        info['val'] = val
        sql = '''
        UPDATE accuracy
        SET accurate_qm_db2={val}
        WHERE query_id=(SELECT Q.query_id
                        FROM query Q,
                             query_split S
                        WHERE Q.query_id=S.query_id
                          AND S.category="{category}"
                          AND Q.db="{dbname}"
                          AND Q.query_index={idx})
          AND experiment_id=(SELECT E.experiment_id
                             FROM experiment_info E
                             WHERE E.system="{system}"
                               AND E.training_data="{dbname}"
                               AND E.test_data="{dbname}"
                               AND E.category="{category}")
        '''.format(**info)
        cur.execute(sql)
        cnt += 1
        print(info)
        print(sql)
    print('UPDATE {} queries'.format(cnt))
    

def create_accuracy_files(filename, systemname, dbname, category):
    username = 'root'
    passwd = 'root'
    
    conn = pymysql.connect(user=username, passwd=passwd, db='benchmark', charset='utf8')
    with conn:
        cur = conn.cursor()
        #for training_dbname, dbname, system, category in rows:
        info = {'dbname': dbname, 'system': systemname, 'category': category}

        # Remove previous comparing results (i.e. acc_db2)
        fill_null(cur, systemname, dbname, category, is_test=False)

        # Update new comparing results
        update_accuracy(cur, filename, info)

        conn.commit()


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Need 4 arguments')
        sys.exit(1)
    filename = sys.argv[1]
    systemname = sys.argv[2]
    dbname = sys.argv[3]
    category = sys.argv[4]
    create_accuracy_files(filename, systemname, dbname, category)

