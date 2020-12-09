import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
from os import listdir
from os.path import isfile, join
from collections import defaultdict
import itertools
from canonicaliser_after_alias import *
import signal
import MySQLdb
from contextlib import closing
import re


HOST = 'localhost'
USER = 'root'
PASSWD = 'root'


def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    class TimeoutError(Exception):
        pass

    def handler(signum, frame):
        raise TimeoutError()

    # set the timeout handler
    signal.signal(signal.SIGALRM, handler) 
    signal.alarm(timeout_duration)
    try:
        result = func(*args, **kwargs)
    except TimeoutError as exc:
        result = default
    finally:
        signal.alarm(0)
        return result


def get_table_alias(query):
    tokens = query.split()
    aliases = set([t.split('.')[0] for t in tokens 
                   if 'alias' in t and not t.startswith('DERIVED')])
    aliases = [t.split('alias') for t in aliases]
    d = defaultdict(lambda: [])
    for table, idx in aliases:
        d[table].append(idx)
    return d


def get_permutation_maps(dic):
    new_dic = {}
    for table in dic:
        l = dic[table]
        if len(l) == 1:
            continue
        from_names = [table + 'alias' + x for x in l]
        permutations = list(itertools.permutations(from_names))
        new_dic[table] = [{from_names[i]: n for i, n in enumerate(p)}
                          for p in permutations]
    return new_dic


def replace_names(query, dic, form='__{}__'):
    for key in dic:
        query = query.replace(key, form.format(key))
    for key, val in dic.items():
        query = query.replace(form.format(key), val)
    return query


def get_alias_permutation_set(query):
    table_alias_dict = get_table_alias(query)
    table_alias_dict = get_permutation_maps(table_alias_dict)
    queries = [query]
    for replace_list in table_alias_dict.values():
        new_queries = []
        for query in queries:
            for replace_dic in replace_list:
                new_queries.append(replace_names(query, replace_dic))
        queries = new_queries
    return queries


def normalize(query):
    new_qry = order_query(query, set())
    #print('norm: {}\n  ->\n{}\n'.format(query, new_qry))
    query = new_qry.lower().strip()
    #query = query.replace(' ', '')
    query = query.replace('"', "'")
    query = query.replace('==', '=')
    if len(query) > 0 and query[-1] == ';':
        query = query[:-1].strip()
    for agg in ['count', 'avg', 'min', 'max', 'sum']:
        pat = re.compile(r'{}\( *(.*?) *\) *'.format(agg))
        query = pat.sub('{}(\\1) '.format(agg), query)
    query = re.sub(r' *, *', ', ', query)
    query = query.replace("count(*)", "count(1)")
    return query


def is_equal_query(q1, q2, schema):
    q1 = normalize(q1)
    norm_q2 = normalize(q2)
    if q1 == norm_q2:
        return 1
    else:
        print(q1, norm_q2)
    alias_q2 = get_alias_permutation_set(q2)
    for query in alias_q2:
        if q1 == normalize(query):
            return 1
        #print(q1)
        #print(normalize(new_qry))
    return 0
    #'''


def add_data(info, sql, gold_dict, gen_dict):
    db_name, idx, category, sys, sql_type, sql_pretty = info.strip(' \n\r').split('\t')
    if db_name.endswith('-s'):
        db_name = db_name[:-2]
    sql = sql.strip()
    key = '\t'.join([db_name, idx])
    if sql_type == 'gen_sql':
        gen_dict[sys, category][key] = (sql, sql_pretty)
    elif sql_type == 'gold_sql':
        gold_dict[key] = (sql, sql_pretty)
    else:
        raise ValueError


def get_generated_queries(cur, dataset, system, category):
    sql = '''
    SELECT Q.query_index, R.gen_sql, Q.nl
    FROM query Q, query_split S, experiment_info E, query_result R
    WHERE Q.query_id=R.query_id AND Q.query_id=S.query_id
      AND E.experiment_id=R.experiment_id AND E.experiment_id=R.experiment_id
      AND E.test_data="{dataset}"
      AND S.split="test"
      AND S.category="{category}"
      AND E.system="{system}"
      AND REPLACE(E.test_data, '-s', '')=Q.db
    '''.format(system=system, category=category, dataset=dataset)
    cur.execute(sql)
    rows = cur.fetchall()
    gen_queries = {}
    questions = {}
    dbname = dataset
    if dataset.endswith('-s'):
        dbname = dbname[:-2]
    for idx, gen_sql, nl in rows:
        key = '\t'.join([dbname, str(idx)])
        gen_queries[key] = gen_sql
        questions[key] = nl
    return gen_queries, questions


def write_file(rewrite_query_file, info_file, schema_filename, dataset, acc_name='accurate_qm_db2'):
    schema = read_schema(schema_filename)

    ### read new queries ###
    gen_queries = defaultdict(lambda: {})
    gold_queries = {}
    with open(rewrite_query_file) as f_q, open(info_file) as f_i:
        is_written = False
        while True:
            info_line = f_i.readline()
            query_line = f_q.readline()
            if not query_line or not info_line:
                assert(not is_written or \
                        (not query_line and not info_line))
                break
            add_data(info_line, query_line, gold_queries, gen_queries)
            is_written = True

    ### Do string match -> write results file ###
    write_result_form = './results/{sys}_{db}_{db}_{category}.results'
    write_files = []
    with closing(MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, charset='utf8')) as conn, \
            closing(conn.cursor()) as cur:
        cur.execute("use benchmark")
        for sys, category in gen_queries:
            gen_execute_queries, nl_questions = get_generated_queries(cur, dataset, sys, category)
            names = {'db': dataset, 'sys': sys, 'category': category}
            write_result_file = write_result_form.format(**names)
            system_gen_queries = gen_queries[sys, category]
            write_files.append(write_result_file)
            with open(write_result_file, 'w') as f_result:
                f_result.write('{}\n'.format('\t'.join(['db_name', 'index', acc_name])))
                keys = list(system_gen_queries.keys())
                keys.sort(key=lambda v: int(v.split('\t')[1]))
                for key in keys:
                    _, idx = key.split('\t')
                    sql_cosette, gen_pretty = system_gen_queries[key]
                    #if category == 'novalue':
                    #    sql_cosette = sql_cosette.replace("'1'", "1")
                    #    gen_pretty = gen_pretty.replace("'1'", "1")
                    try:
                        gold_query, gold_pretty = gold_queries[key]
                    except Exception as e:
                        print(repr(e))
                        print('ERROR', dataset, idx)
                    if sql_cosette == '' or gold_query == '':
                        sql_cosette = gen_pretty
                        gold_query = gold_pretty
                    acc_qm = timeout(is_equal_query, args=(sql_cosette, gold_query, schema), timeout_duration=30, default=0)
                    if acc_qm:
                        print(acc_qm, dataset, sql_cosette, gen_pretty, gold_query, gold_pretty)
                        f_result.write('{}\t{}\t{}\n'.format(dataset, idx, str(acc_qm)))
    return write_files


#def get_gold_filenames(dbname, dataset):
#    gold_form = '../data/{db}/{dataset}_{category}_{mode}.tsv'
#    names = {'db': dbname, 'dataset': dataset}
#    files = []
#    for cat in ['basic', 'canonicalize', 'seen', 'novalue', 'distinct']:
#        names['category'] = cat
#        for mode in ['train', 'dev', 'test']:
#            names['mode'] = mode
#            files.append((gold_form.format(**names), cat))
#    return files



if __name__ == '__main__':
    info_dir = './queries/'
    query_dir = './canonicalized_files/'
    info_form = './queries/{system}_{db}_queries_index.tsv'
    query_form = './canonicalized_files/{system}_{db}_canonicalized.sql'

    info_files = [join(info_dir, f) for f in listdir(info_dir) if isfile(join(info_dir, f))]
    info_files = [f for f in info_files if f.endswith('_index.tsv')]

    query_files = [join(query_dir, f) for f in listdir(query_dir)]

    system = sys.argv[1]
    db_name = sys.argv[2]
    schema_filename = sys.argv[3]
    info_file = info_form.format(system=system, db=db_name)
    query_file = query_form.format(system=system, db=db_name)
    dataset = db_name
    if db_name.endswith('-s'):
        db_name = db_name[:-2]
    if db_name.startswith('advising'):
        db_name = 'advising'
    #gold_query_files = get_gold_filenames(db_name, dataset)
    if info_file in info_files \
            and query_file in query_files:
        accuracy_filenames = write_file(query_file, info_file, schema_filename, dataset)
        print('Done string match comparing with DB2: {}'.format(accuracy_filenames))
    else:
        print("No file(s)")
        print(info_file, query_file)
        print('')

