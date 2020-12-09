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

def print_log_message(level, messages):
    timestamp = str(datetime.datetime.now())
    print(timestamp + '\t' + level + '\t' + '\t'.join(messages))

def format_sql(sql):
    # aggregate functions
    agg_funcs = ['MAX', 'MIN', 'COUNT', 'AVG', 'SUM', 'max', 'min', 'count', 'avg', 'sum']
    for func in agg_funcs:
        sql = sql.replace(func + ' (', func + '(')

    # inequalities
    sql = sql.replace('< >', '<>')
    sql = sql.replace('> =', '>=')
    sql = sql.replace('< =', '<=')

    return sql

def load_logs(dbconn):
    print(MESSAGE_HLINE + MESSAGE_BOLD + 'Loading log files' + MESSAGE_RESET)
    num_loaded = 0
    for filename in os.listdir(LOG_DIR):
        if not filename.endswith('.log'):
            continue

        print('Loading ' + filename)
        is_loaded = False
        try:
            dbconn.begin()
            with closing(dbconn.cursor()) as cu:
                cu.execute('''USE benchmark''')

                filename_split = filename.replace('.', '_').split('_')
                system = filename_split[0]
                training_data = filename_split[1]
                test_data = filename_split[2]
                category = filename_split[3]

                # insert (system, training_data, test_data, category) to experiment_info, and get
                # experiment_id
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

                # insert (experiment_id, log_path) to query_result
                cu.execute('''
                    SELECT experiment_id
                    FROM   log
                    WHERE  experiment_id=%s
                    ''' % (experiment_id))
                if cu.rowcount == 0:
                    cu.execute('''
                        INSERT INTO log (experiment_id, log_path)
                        VALUES (%s, "%s")
                        ''' % (experiment_id, LOG_DIR + filename))
                    is_loaded = True
                else:
                    cu.execute(
                        '''
                        UPDATE log
                        SET    log_path="%s"
                        WHERE  experiment_id=%s
                        ''' % (LOG_DIR + filename, experiment_id))
                    is_loaded = True
            dbconn.commit()
        except Exception as e:
            print(MESSAGE_FAILED)
            print(MESSAGE_RED + str(e) + MESSAGE_RESET)
            try:
                dbconn.rollback()
            except:
                pass
            continue
        print(MESSAGE_DONE)
        num_loaded += 1 if is_loaded else 0
    print(MESSAGE_BOLD + 'Loading log files' + MESSAGE_RESET)
    print('(' + str(num_loaded) + ' file(s) loaded)')

