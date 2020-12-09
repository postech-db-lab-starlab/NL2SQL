import sys
#import MySQLdb
from contextlib import closing
from warnings import filterwarnings

from canonicaliser_after_alias import *

from parser.add_as_parser import alias_sql
#from parser.myParser import alias_sql


INVALID_SQL = '__INVALID_SQL__'
NOT_IN_DB = '__TABLE_NOT_IN_DB__'
#db_connected = False
HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'


def normalize(query):
    query = query.lower()
    query = query.replace(' ', '')
    query = query.replace('"', "'")
    query = query.replace('==', '=')
    query = query.replace(';', '')
    query = query.replace('count(*)', 'count(1)')
    return query


def has_unknown(query):
    if '< unk >' in query:
        return 1
    return 0


def remove_quote_in_constant(query):
    quote_marks = ('"', "'", '`')
    ret = ''
    in_quote = None
    prev = None
    for char in query:
        if in_quote is None:
            if char in quote_marks:
                in_quote = char
        else:
            if char == in_quote:
                if prev == '\\':
                    ret = ret[:-1]
                    char = ''
                else:
                    in_quote = None
            elif char in quote_marks:
                continue
        ret += char
        prev = char
    if in_quote is not None:
        ret = INVALID_SQL
    return ret


#def valid_sql(query, db='wikisql'):
#    global db_connected
#    if db_connected == False:
#        print("CONNECT TO DB")
#        db_connected = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD)
#    cursor = db_connected.cursor()
#    cursor.execute('use {}'.format(db))
#    valid = True
#    try:
#        cursor.execute(query)
#    except MySQLdb.Error as e:
#        valid = INVALID_SQL
#        if e.args[0] == 1146:
#            valid = NOT_IN_DB
#        else:
#            print(e.args[1])
#    except:
#        valid = INVALID_SQL
#    cursor.close()
#    return valid
#
#
#def close_db():
#    global db_connected
#    if db_connected:
#        db_connected.close()



def get_tables(query):
    tokens = query.split()
    tables = [t.split('.')[0] for t in tokens if t.startswith('TABLE_')]
    tables = list(set(tables))
    return tables


def get_dummy_schema(tables):
    tables = [table.upper() for table in tables]
    columns = ['COL{}'.format(i) for i in range(100)]
    schema = ({table: set(columns) for table in tables},
               set(columns + tables))
    return schema


def norm(query, gen=True):
    e = ''
    query = query.replace("\\'", '')
    query = query.replace('\\"', '')
    #query = remove_quote_in_constant(query)
    #if query == INVALID_SQL:
    #    return query
    #if gen and has_unknown(query):
    #    return INVALID_SQL
    #if query.strip()[-1] != ';':
    #    query += ' ;'

    #valid = valid_sql(query)
    #if valid in (INVALID_SQL, NOT_IN_DB):
    #    return valid
    #print('\n{}'.format(gen))
    #print(query)
    query = alias_sql(query, silent=True)
    #query = alias_sql(query)
    #print(query)
    #print('\n\n')
    query = query.replace('. ', '.').replace(' .', '.')
    tables = get_tables(query)
    schema = get_dummy_schema(tables)
    query = standardise_blank_spaces(query)
    try:
        query = capitalise(query, set())
    except AssertionError:
        print('\nAssertionError')
        print(gen, query)
        return INVALID_SQL
    query = standardise_aliases(query, schema)
    query = order_query(query, set())

    try:
        query = make_canonical(query, schema, set(), set())
    except Exception as e:
        print(gen, query)
        query = INVALID_SQL
    query = normalize(query)
    return query, e
    


def string_match(gen_qry, gold_qry):
    same = -1
    text = "ERROR"
    try:
        e2 = None
        e1 = None
        q1, e1 = norm(gen_qry, gen=True)
        #print('q2')
        #print(gold_qry)
        q2, e2 = norm(gold_qry, gen=False)
        #print(q2)
        assert(q2 != INVALID_SQL)
        same = int(q1 == q2 and q1 not in (INVALID_SQL, NOT_IN_DB))
        text = "SAME" if same else "WRONG"
    except AssertionError:
        print('ERROR GOLD: {}'.format(gold_qry))
        print('ERROR GEN: {}'.format(gen_qry))
        print("AssertionError")
        print(e1, e2)
        #assert(False)
    except Exception as e:
        print('ERROR GOLD: {}'.format(gold_qry))
        print('ERROR GEN: {}'.format(gen_qry))
        print(repr(e))
    #print('GEN: {}'.format(gen_qry))
    #print('GOLD: {}'.format(gold_qry))
    #print("    {}".format(text))
    return same


def read_tsv(filename, idx=0, header=True):
    value_list = []
    with open(filename) as f:
        if header:
            _ = f.readline()
        while True:
            line = f.readline()
            if not line: break
            row = line.strip()
            value_list.append(row.split('\t')[idx])
    return value_list


def evaluate(gen_filename, gold_filename, write_filename):
    gen_queries = read_tsv(gen_filename, header=False)
    gold_queries = read_tsv(gold_filename, idx=5)
    indices = read_tsv(gold_filename, idx=1)
    print(len(gen_queries), len(gold_queries), len(indices))
    assert(len(gen_queries) == len(gold_queries))
    assert(len(indices) == len(gold_queries))
    #gen_queries = gen_queries[-20:]
    #gold_queries = gold_queries[-20:]
    #indices = indices[-20:]
    cnt = 0
    correct = 0
    err = 0
    err_list = []
    filterwarnings("ignore")
    with open(write_filename, 'w') as wf:
        header = ['db_name', 'index', 'accurate_qm']
        wf.write('{}\n'.format('\t'.join(header)))
        for idx, gen_qry, gold_qry in zip(
                indices, gen_queries, gold_queries):
            #print('\nindex: {}'.format(idx))
            acc_qm = string_match(gen_qry, gold_qry)
            row = ['wikisql', idx, str(acc_qm)]
            wf.write('{}\n'.format('\t'.join(row)))
            cnt += 1
            if acc_qm == -1:
                err += 1
                err_list.append(idx)
            else:
                correct += acc_qm
    print("CORRECT: {} / {}".format(correct, cnt))
    print("ERROR: {}".format(err))
    print(err_list)
    #close_db()


if __name__ == '__main__':
    gen_filename = sys.argv[1]
    gold_filename = sys.argv[2]
    write_filename = sys.argv[3]
    evaluate(gen_filename, gold_filename, write_filename)


