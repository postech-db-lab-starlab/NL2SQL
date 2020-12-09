import os
import re
import sys
from antlr4 import *
if __name__ == '__main__':
    from g4.SelectSQLLexer import SelectSQLLexer
    from g4.SelectSQLParser import SelectSQLParser
    from g4.SelectSQLParserListener import SelectSQLParserListener
else:
    from parser.g4.SelectSQLLexer import SelectSQLLexer
    from parser.g4.SelectSQLParser import SelectSQLParser
    from parser.g4.SelectSQLParserListener import SelectSQLParserListener

# This class defines a complete listener for a parse tree produced by SelectSQLParser.
class MyListener(SelectSQLParserListener):
    def __init__(self):
        # self.table_dict = {}
        # self.pretty = []  # (text, need_to_change)
        self.root = None
        # self.ctx_dict = {}

    def enterRoot(self, ctx:SelectSQLParser.RootContext):
        self.root = ctx
        pass




table_index = 0
column_index = 0

def resetName():
    global table_index
    global column_index
    table_index = 0
    column_index = 0


def getTableName():
    global table_index
    name = '_t{}'.format(table_index)
    table_index += 1
    return name

def getColumnName():
    global column_index
    name = '_c{}'.format(column_index)
    column_index += 1
    return name


subqueryContext = (SelectSQLParser.SimpleSelectContext,
                   SelectSQLParser.ParenthesisSelectContext,
                   SelectSQLParser.UnionSelectContext,
                   SelectSQLParser.UnionParenthesisSelectContext,)

def traverse(ctx, tableNameDict, columnNameDict):
    child_cnt = ctx.getChildCount()
    if child_cnt == 0:  # At a leaf of parse tree
        text = ctx.getText()
        #if len(text) >= 2 and text[0] == text[-1]:
        #    if text[0] == '"':
        #        text = text[1:-1]
        #        text = text.replace("\\'", "'").replace('\\"', '"')
        #        text = text.replace('"', '\\"').replace('\\"', '"')
        #        text = "'{}'".format(text)
        #else:
        #    text = text.replace('"', "'")
        return [text], tableNameDict, columnNameDict

    tokens = []
    texts = {}
    children = [ctx.getChild(i) for i in range(child_cnt)]

    for idx, child in enumerate(children):
        if isinstance(child, SelectSQLParser.FromClauseContext):
            text, tableNameDict, columnNameDict = traverse(child, tableNameDict, columnNameDict)
            texts[idx] = text

    for idx, child in enumerate(children):
        if texts.get(idx) is not None:
            continue
        table_save = tableNameDict.copy()
        text, tableNameDict, columnNameDict = traverse(child, tableNameDict, columnNameDict)
        texts[idx] = text

    for idx in range(child_cnt):
        tokens.append(texts[idx])

    # Column in Select clause
    if isinstance(ctx, (SelectSQLParser.SelectColumnElementContext,
                        SelectSQLParser.SelectFunctionElementContext)):
        assign_tokens = []

        ### get table_name ###
        if isinstance(ctx, SelectSQLParser.SelectColumnElementContext):
            table_name = tokens[0][0]
        else:
            table_name = tokens[0][2]

        column_name = tokens[-1][-1]
        if column_name[0] == '.':
            column_name = column_name[1:]
        else:
            column_name = ''.join(tokens[-1])
        column_alias = column_name
        if child_cnt == 3:
            pass
        elif child_cnt == 2:
            tokens = [tokens[0], ['AS'], tokens[1]]
        elif child_cnt == 1:
            column_alias = getColumnName()
            tokens = [tokens[0], ['AS'], [column_alias]]
        else:
            raise ValueError  # Impossible parse tree

        ### find original column_name ###
        table_dict = columnNameDict.get(table_name)
        if table_dict is not None and column_name.startswith('_c'):
            for k in table_dict:
                if k.startswith('$c'): pass
                elif table_dict[k] == column_name:
                    column_name = k
                    break

        ### add {column_name: column_alias} in columnNameDict[None] ###
        column_dict = columnNameDict.get(None, {})
        column_dict['$c{}'.format(int( len(column_dict)/2 ))] = column_alias
        column_dict[column_name.lower()] = column_alias
        columnNameDict[None] = column_dict
        tokens = assign_tokens + tokens
    # star(*) in Select clause
    elif isinstance(ctx, SelectSQLParser.SelectStarElementContext):
        print("Fail to column alias becuase of star(*)")
        raise ValueError
    # Any column found -> Need to check table name & column name
    elif isinstance(ctx, SelectSQLParser.FullColumnNameContext):
        if child_cnt == 2:
            assert(len(tokens[0]) == 1)
            table_name = tokens[0][0]
            table_name, _ = tableNameDict[table_name]
            column_name = ''.join(tokens[1])
            assert(column_name[0] == '.')
            column_name = column_name[1:]
            # print(table_name, column_name, columnNameDict)
            column_dict = columnNameDict.get(table_name)
            if column_dict:
                # print(column_dict, table_name, column_name)
                column_name = column_dict[column_name.lower()]
                # print(column_name, column_dict, columnNameDict)
            column_name = '.' + column_name
            tokens = [[table_name], [column_name]]
        elif child_cnt == 1:
            table_name, _ = tableNameDict[None]
            column_dict = columnNameDict.get(table_name)  
            if column_dict and len(tokens) == 1:
                tokens[0][0] = column_dict[norm_column_name(tokens[0][0])]
            tokens = [[table_name], ['.'], tokens[0]]
    # Table in From clause (1 Table Item)
    elif isinstance(ctx, SelectSQLParser.AtomTableItemContext):
        assert(1 <= child_cnt <= 3)
        assert(len(tokens[0]) == 1)
        table_name = tokens[0][0]

        ### Find view maded by db2exfmt & fix to executable query ###
        use_view = False
        for key in tableNameDict.keys():
            t_name, t_tokens = tableNameDict[key]
            # print(table_name, tableNameDict.keys(), t_name, t_tokens)
            if table_name.upper() == t_name.upper():
                tokens[0] = t_tokens
                use_view = True
                break

        if child_cnt == 1:
            table_alias = getTableName()
        else:
            assert(len(tokens[-1]) == 1)
            table_alias = tokens[-1][0]
            table_name = table_alias
        tokens = [tokens[0], ['AS'], [table_alias]]
        if use_view:
            columnNameDict[table_alias] = columnNameDict[t_name]
        tableNameDict[table_name] = table_alias, tokens[0]
        tableNameDict[None] = table_alias, tokens[0]
    # Table in From clause (Subquery as a table)
    elif isinstance(ctx, SelectSQLParser.SubqueryTableItemContext):
        assert(len(tokens[-1]) == 1)
        table_name = tokens[-1][0]
        # print(table_name, columnNameDict)
        tableNameDict[table_name] = table_name, tokens[0]
        tableNameDict[None] = table_name, tokens[0]
        column_dict = columnNameDict.get(None, {})
        columnNameDict[table_name] = column_dict
        columnNameDict[None] = {}
        if tokens[-2][0].upper() == 'AS':
            pass
        else:
            tokens = tokens[:-1] + [['AS']] + tokens[-1:]

    tokens = [x for y in tokens for x in y]

    return tokens, tableNameDict, columnNameDict


def alias_sql(candidate, show=False, silent=False):
    resetName()
    if len(candidate) > 0 and candidate[-1] == ';':
        candidate = candidate[:-1]
    lexer = SelectSQLLexer(InputStream(candidate))
    stream = CommonTokenStream(lexer)
    parser = SelectSQLParser(stream)
    if silent:
        lexer.removeErrorListeners()
        parser.removeErrorListeners()
    recognition_error = False
    printer = MyListener()
    ctx = parser.root()
    walker = ParseTreeWalker()
    walker.walk(printer, ctx)

    if parser.getNumberOfSyntaxErrors() > 0:
        return ''

    try:
        sql, _, _ = traverse(ctx, {}, {})
    except Exception as e:
        print('')
        print(repr(e), 'in Alias')
        print('')
        print(candidate)
        print('')
        return ''
        # raise Exception
    
    if sql[-1] == '<EOF>':
        sql = sql[:-1]

    sql_pretty = ' '.join(sql)
    sql_pretty = sql_pretty.replace('= =', '=')  # error from cludes sqlite3 grammar
    sql_pretty = sql_pretty.replace('< =', '<=')
    sql_pretty = sql_pretty.replace('> =', '>=')
    sql_pretty = sql_pretty.replace('< >', '<>')

    if show:
        print(sql_pretty)

    return sql_pretty

    

if __name__ == '__main__':
    import sys
    print('')
    alias_sql(sys.argv[1], show=True)
    print('')
    print(sys.argv[1])

