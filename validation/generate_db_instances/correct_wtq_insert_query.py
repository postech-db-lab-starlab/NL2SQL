import sys
import MySQLdb
import codecs

def get_table_name(qry):
    head, tail = qry.split('databasetmp.')
    table_name = tail.split()[0]
    return table_name


def make_insert_query(table):
    conn = MySQLdb.connect(user='root', passwd='root', use_unicode=True, charset="utf8")
    cu = conn.cursor()
    cu.execute('use information_schema')
    cu.execute("select column_name from columns where table_schema = 'wikitablequestions' and table_name = '{}';".format(table))
    columns = cu.fetchall()
    qry = u"LOAD DATA LOCAL INFILE \"tmp/{}.tsv\" INTO TABLE databasetmp.{} FIELDS TERMINATED BY '\\t' LINES TERMINATED BY '\\n' ({});\n".format(table, table, u','.join([u"`{}`".format(col[0]) for col in columns]))
    return qry


if __name__ == '__main__':
    fname = sys.argv[1]
    f = codecs.open(fname, 'r', 'utf-8')
    lines = [l.strip() for l in f]
    f.close()

    f = codecs.open(fname, 'w', 'utf-8')
    for line in lines:
        table = get_table_name(line)
        qry = make_insert_query(table)
        f.write(qry)
    f.close()