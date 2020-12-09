from rewrite_sql import rewrite_sql
#from parser.db2_opt_parser import alias_sql
from parser.myParser import alias_sql
import sys

if __name__ == '__main__':
    before_rewriting_file = None
    if len(sys.argv) == 3:
        db2_rewriting_file = sys.argv[1]
        write_file = sys.argv[2]
    elif len(sys.argv) == 4:
        db2_rewriting_file = sys.argv[1]
        write_file = sys.argv[2]
        before_rewriting_file = sys.argv[3]
    else:
        print("WRONG # of args")
        sys.exit()

    print("\n\nSTART ALIAS")
    print("READ {}".format(db2_rewriting_file))

    origin_queries = []
    if before_rewriting_file is not None:
        with open(before_rewriting_file) as f:
            origin_queries = [l.strip() for l in f]

    error_cnt = 0
    cnt = 0
    print('len origin_queries: {}'.format(len(origin_queries)))
    with open(db2_rewriting_file) as f, open(write_file, 'w') as wf:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                cnt += 1
            query = line.strip()

            try:
                postprocessed_db2exfmt_query = rewrite_sql(query)
            except Exception as e:
                print(repr(e))
                postprocessed_db2exfmt_query = ''

            if postprocessed_db2exfmt_query == '' and len(origin_queries) > 0:
                print('postprocessed_db2exfmt_query EMPTY: {}'.format(cnt))
                postprocessed_db2exfmt_query = origin_queries[cnt-1]

            try:
                alias_query = alias_sql(postprocessed_db2exfmt_query)
            except Exception as e:
                print(repr(e))
                alias_query = postprocessed_db2exfmt_query

            #alias_query = alias_query.replace(' .', '.')
            if alias_query == '':
                error_cnt += 1
            wf.write('{}\n'.format(alias_query))
            print('\n{}\n  =>\n{}\n  =>\n{}\n'.format(query, postprocessed_db2exfmt_query, alias_query))
    print('ERROR: {}'.format(error_cnt))
