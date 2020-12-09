import sys
import re
#from parser.db2_opt_parser import alias_sql
from parser.myParser import alias_sql


#def replace_quote(query):
#    in_quote = ''
#    tmp_query = []
#    pos = 0
#    while pos < len(query):
#        char = query[pos]
#        pos += 1
#        if char in ["'", '"']:
#            if in_quote == '' or in_quote == char:
#                in_quote = '' if in_quote == char else char
#                tmp_query.append("'")
#            else:
#                tmp_query.append('"')
#        else:
#            tmp_query.append(char)
#    return ''.join(tmp_query)           


def change_to_db2_sql(sql, db2):
    #sql = replace_quote(sql)
    sql = sql.replace('"', "'")
    if sql[:-1] == ';':
        sql = sql[:-1]
    if db2 is True and 'limit' in sql.lower():
        p = re.compile(r"limit ([0-9]+)")
        sql = p.sub('fetch first \\1 rows only', sql.lower())
    sql = sql.replace('`', '"').upper()
    p = re.compile(r" _C([0-9]+)")
    sql = p.sub(' COLUMN_ALIAS_DB2_\\1', sql)
    p = re.compile(r" _T([0-9]+)")
    sql = p.sub(' TABLE_ALIAS_DB2_\\1', sql)

    sql = sql.replace("DENNY'S", "DENNYS")
    return sql


def get_sql(filename, write, idx, db2=True):
    with open(filename, encoding='utf-8') as f, open(write, 'w') as wf:
        while True:
            line = f.readline()
            if not line: break
            sql = line.strip(' \n\r').split('\t')[idx]
            if idx > 0:
                sql = sql.replace('FROM(SELECT', 'FROM ( SELECT')
                #sql = alias_sql(sql)
            sql = change_to_db2_sql(sql, db2=db2)
            wf.write('{}\n'.format(sql))


if __name__ == '__main__':
    filename = sys.argv[1]
    write_filename = sys.argv[2]
    idx = 0
    if len(sys.argv) >= 4:
        idx = int(sys.argv[3])
    is_db2 = True
    if len(sys.argv) >= 5:
        is_db2 = False
    get_sql(filename, write_filename, idx, db2=is_db2)



