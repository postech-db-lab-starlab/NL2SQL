import re
from parser.db2_opt_parser import alias_sql


def remove_selectivity_token(tokens):
    prev_token = None
    new_tokens = []
    for token in tokens:
        is_selectivity_token = False
        try:
            _ = float(token)
            if prev_token.upper() == 'SELECTIVITY':
                is_selectivity_token = True
        except:
            pass

        # if is_selectivity_token:
        #     print(prev_token, token)
        #     print(is_selectivity_token)
        if is_selectivity_token:
            prev_token = None
        else:
            if prev_token is not None:
                new_tokens.append(prev_token)
            if token[0] == token[-1] == '"':
                token = token[1:-1]
            prev_token = token
    new_tokens.append(prev_token)
    return new_tokens


def scan(token, state):
    if not token:
        return state
    if token == '(':
        state[0] += 1
    elif token == ')':
        state[0] -= 1
        assert(state[0] >= 0)
    elif token == 'FROM' and state[0] == 0:
        assert(state[1] is None)
        state[1] = 'FROM'
    elif token == 'WHERE' and state[0] == 0:
        assert(state[1] == 'FROM')
        state[1] = 'WHERE'
    elif token in ('MIN', 'MAX', 'COUNT', 'SUM', 'AVG') and state[1] == 'FROM':
        # if token: print(token, state[1])
        state[2] = True
    elif token in ('MIN', 'MAX', 'AVG') and state[1] == 'WHERE':
        # if token: print(token, state[1])
        state[2] = True
    elif token in ('IN'):
        # if token: print(token, state[1])
        state[2] = True
    return state



def rewrite_sql(sql):
    error_msg = "SELECT CLIENT APPLNAME, CLIENT ACCTNG FROM (SELECT 'Y' FROM (VALUES 1) AS Q1 ) AS Q2"
    if sql.strip() == error_msg:
        return ''

    # HJKIM. => DB2 SCHEMA name
    #sql = sql.replace('HJKIM.', '')
    sql = sql.replace('BHSO.', '')
    sql = sql.replace('"', '')
    exponent_re = r"[-+][0-9]+\.[0-9]+[eE][-+]?[0-9]+"
    exponent_numbers = re.findall(exponent_re, sql)
    for num in exponent_numbers:
        sql = sql.replace(num, str(float(num)))
    sql_trans = sql.replace('(', ' ( ')
    sql_trans = sql_trans.replace(')', ' ) ')
    tokens = sql_trans.split(' ')
    tokens = [t for t in tokens if t != '']
    state = [0, None, False]  # [paren count, seen from/where, cosette available]

    # print(tokens)
    tokens = remove_selectivity_token(tokens)
    for token in tokens:
        state = scan(token, state)

    assert(state[0] == 0)
    cosette_able = not state[2]

    if 'SELECT NULL FROM (VALUES' in sql:
        sql = ''
    else:
        sql = ' '.join(tokens)
    # if not cosette_able \
    #         or 'SELECT NULL FROM' in sql \
    #         or 'ORDER BY' in sql \
    #         or 'IS NOT NULL' in sql:
    #     sql = ''
    # if '$' in sql:
    #     print('ERROR')
    #     print(sql)
    #sql = sql.replace('FETCH FIRST 1 ROWS ONLY', 'LIMIT 1')
    #sql = sql.replace('FETCH FIRST 2 ROWS ONLY', 'LIMIT 2')
    #sql = sql.replace('FETCH FIRST 3 ROWS ONLY', 'LIMIT 3')
    sql = re.sub('\$C([0-9])', 'DB2_TMP_COL\\1', sql)
    sql = re.sub('FETCH FIRST ([0-9]+) ROWS ONLY', 'LIMIT \\1', sql)
    return sql


########### NOT USED
def write_file(rewrite_query_file, info_file, gold_query_file, gen_query_file):
    # f_gold = open(gold_query_file, 'w')
    # f_gen = open(gen_query_file, 'w')
    # header = ['db_name', 'index', 'sql', 'nl', 'sql_cosette', 'sql_cosette_rename', 'sql_execute']
    # f_gold.write('{}\n'.format('\t'.join(header)))
    # header = ['db_name', 'index', 'sql_pretty', 'sql_execute']  # sql_execute = sql_cosette
    # f_gen.write('{}\n'.format('\t'.join(header)))
    with open(rewrite_query_file) as f_q, open(info_file) as f_i:
        gold_queries = {}
        gen_queries = {}
        while True:
            info_line = f_i.readline()
            sql_line = f_q.readline()
            if not sql_line or not info_line:
                assert(not sql_line and not info_line)
                break
            db_name, idx, sys, sql_type, _ = info_line.strip().split('\t')
            sql = sql_line.strip()

            executable_sql = rewrite_sql(sql)
            if executable_sql == '':
                sql_cosette = ''
            else:
                sql_cosette = alias_sql(executable_sql)
                # if '$' in sql_cosette.lower():
                #     print('$', sql_cosette)

            if sql_type == 'gen_sql':
                sys_dic = gen_queries.get(sys, {})
                dic = sys_dic.get(db_name, [])
                dic.append([idx, sql_cosette])
                sys_dic[db_name] = dic
                gen_queries[sys] = sys_dic
                # f_gen.write('{}\t{}\t{}\t{}\n'.format(db_name, idx, sys, sql_cosette))
            elif sql_type == 'gold_sql':
                dic = gold_queries.get(db_name, [])
                dic.append([idx, sql_cosette])
                gold_queries[db_name] = dic
                # f_gold.write('{}\t{}\t{}\n'.format(db_name, idx, sql_cosette))
            else:
                raise ValueError

    # f_gold.close()
    # f_gen.close()
    #'''
    read_gold_query_file = './hjkim/gold_queries/{}.tsv'
    gold_query_file = './db2exfmt/upload_files/{}.tsv'
    for db_name in  gold_queries:
        queries = gold_queries[db_name]
        origin_data = []
        with open(read_gold_query_file.format(db_name)) as f:
            header = f.readline().strip()
            while True:
                line = f.readline()
                if not line: break
                datum = line.strip().split('\t')
                datum[1] = datum[1]
                origin_data.append(datum)
        with open(gold_query_file.format(db_name), 'w') as f:
            f.write('{}\n'.format(header))
            for query in queries:
                for datum in origin_data:
                    if datum[1] == query[0]:
                        datum[4] = query[1]
                        f.write('{}\n'.format('\t'.join(datum)))

    read_gen_query_file = './hjkim/output_finish/{sys}_{db}_{db}_basic.gen_query'
    gen_query_file = './db2exfmt/upload_files/{sys}_{db}_{db}_basic.gen_query'
    for sys in gen_queries:
        sys_dict = gen_queries[sys]
        for db_name in sys_dict:
            queries = sys_dict[db_name]
            origin_data = []
            with open(read_gen_query_file.format(db=db_name, sys=sys)) as f:
                header = f.readline().strip()
                while True:
                    line = f.readline()
                    if not line: break
                    datum = line.strip().split('\t')
                    datum[1] = datum[1]
                    origin_data.append(datum)
            with open(gen_query_file.format(db=db_name, sys=sys), 'w') as f:
                f.write('{}\n'.format(header))
                for query in queries:
                    for datum in origin_data:
                        if datum[1] == query[0]:
                            datum[3] = query[1]
                            f.write('{}\n'.format('\t'.join(datum)))
    #'''



if __name__ == '__main__':
    db_list = ['geo', 'patients', 'mas', 'imdb', 'yelp', 'scholar', 'restaurant', 'atis']
    # db_list = ['test']
    # db_list = ['atis']
    for db in db_list:
        print('\n\n')
        print(db)
        info_file = 'db2exfmt/cosette_errors/{}_cosette_result_index.tsv'.format(db)
        filename = 'db2exfmt/upload_files/{}_db2exfmt_sql.tsv'.format(db)
        gold_query_file = filename.replace('sql', 'gold_sql')
        gen_query_file = filename.replace('sql', 'gen_sql')
        if db == 'restaurant':
            db = 'res'
        rewrite_query_file = 'db2exfmt/db2exfmt_results/{}_cosette_result.sql.rewrite'.format(db)
        write_file(rewrite_query_file, info_file, gold_query_file, gen_query_file)

