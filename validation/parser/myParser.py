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

    # # Enter a parse tree produced by SelectSQLParser#simpleSelect.
    # def enterSimpleSelect(self, ctx:SelectSQLParser.SimpleSelectContext):
    #     # print('ENTER: SimpleSelect ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     # self.ctx_dict
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#simpleSelect.
    # def exitSimpleSelect(self, ctx:SelectSQLParser.SimpleSelectContext):
    #     # print('EXIT:  SimpleSelect ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#parenthesisSelect.
    # def enterParenthesisSelect(self, ctx:SelectSQLParser.ParenthesisSelectContext):
    #     # print('ENTER: ParenthesisSelect ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#parenthesisSelect.
    # def exitParenthesisSelect(self, ctx:SelectSQLParser.ParenthesisSelectContext):
    #     # print('EXIT:  ParenthesisSelect ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#unionSelect.
    # def enterUnionSelect(self, ctx:SelectSQLParser.UnionSelectContext):
    #     # print('ENTER: UnionSelect ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#unionSelect.
    # def exitUnionSelect(self, ctx:SelectSQLParser.UnionSelectContext):
    #     # print('EXIT:  UnionSelect ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#unionParenthesisSelect.
    # def enterUnionParenthesisSelect(self, ctx:SelectSQLParser.UnionParenthesisSelectContext):
    #     # print('ENTER: UnionParenthesisSelect ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#unionParenthesisSelect.
    # def exitUnionParenthesisSelect(self, ctx:SelectSQLParser.UnionParenthesisSelectContext):
    #     # print('EXIT:  UnionParenthesisSelect ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#orderByClause.
    # def enterOrderByClause(self, ctx:SelectSQLParser.OrderByClauseContext):
    #     # print('ENTER: OrderByClause ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#orderByClause.
    # def exitOrderByClause(self, ctx:SelectSQLParser.OrderByClauseContext):
    #     # print('EXIT:  OrderByClause ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#orderByExpression.
    # def enterOrderByExpression(self, ctx:SelectSQLParser.OrderByExpressionContext):
    #     # print('ENTER: OrderByExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#orderByExpression.
    # def exitOrderByExpression(self, ctx:SelectSQLParser.OrderByExpressionContext):
    #     # print('EXIT:  OrderByExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#tableSources.
    # def enterTableSources(self, ctx:SelectSQLParser.TableSourcesContext):
    #     # print('ENTER: TableSources ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#tableSources.
    # def exitTableSources(self, ctx:SelectSQLParser.TableSourcesContext):
    #     # print('EXIT:  TableSources ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#tableSourceBase.
    # def enterTableSourceBase(self, ctx:SelectSQLParser.TableSourceBaseContext):
    #     # print('ENTER: TableSourceBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#tableSourceBase.
    # def exitTableSourceBase(self, ctx:SelectSQLParser.TableSourceBaseContext):
    #     # print('EXIT:  TableSourceBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#tableSourceNested.
    # def enterTableSourceNested(self, ctx:SelectSQLParser.TableSourceNestedContext):
    #     # print('ENTER: TableSourceNested ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#tableSourceNested.
    # def exitTableSourceNested(self, ctx:SelectSQLParser.TableSourceNestedContext):
    #     # print('EXIT:  TableSourceNested ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#atomTableItem.
    # def enterAtomTableItem(self, ctx:SelectSQLParser.AtomTableItemContext):
    #     print('ENTER: AtomTableItem ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#atomTableItem.
    # def exitAtomTableItem(self, ctx:SelectSQLParser.AtomTableItemContext):
    #     print('EXIT:  AtomTableItem ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#subqueryTableItem.
    # def enterSubqueryTableItem(self, ctx:SelectSQLParser.SubqueryTableItemContext):
    #     print('ENTER: SubqueryTableItem ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#subqueryTableItem.
    # def exitSubqueryTableItem(self, ctx:SelectSQLParser.SubqueryTableItemContext):
    #     print('EXIT:  SubqueryTableItem ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#tableSourcesItem.
    # def enterTableSourcesItem(self, ctx:SelectSQLParser.TableSourcesItemContext):
    #     # print('ENTER: TableSourcesItem ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#tableSourcesItem.
    # def exitTableSourcesItem(self, ctx:SelectSQLParser.TableSourcesItemContext):
    #     # print('EXIT:  TableSourcesItem ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#indexHint.
    # def enterIndexHint(self, ctx:SelectSQLParser.IndexHintContext):
    #     # print('ENTER: IndexHint ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#indexHint.
    # def exitIndexHint(self, ctx:SelectSQLParser.IndexHintContext):
    #     # print('EXIT:  IndexHint ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#indexHintType.
    # def enterIndexHintType(self, ctx:SelectSQLParser.IndexHintTypeContext):
    #     # print('ENTER: IndexHintType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#indexHintType.
    # def exitIndexHintType(self, ctx:SelectSQLParser.IndexHintTypeContext):
    #     # print('EXIT:  IndexHintType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#innerJoin.
    # def enterInnerJoin(self, ctx:SelectSQLParser.InnerJoinContext):
    #     # print('ENTER: InnerJoin ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#innerJoin.
    # def exitInnerJoin(self, ctx:SelectSQLParser.InnerJoinContext):
    #     # print('EXIT:  InnerJoin ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#straightJoin.
    # def enterStraightJoin(self, ctx:SelectSQLParser.StraightJoinContext):
    #     # print('ENTER: StraightJoin ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#straightJoin.
    # def exitStraightJoin(self, ctx:SelectSQLParser.StraightJoinContext):
    #     # print('EXIT:  StraightJoin ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#outerJoin.
    # def enterOuterJoin(self, ctx:SelectSQLParser.OuterJoinContext):
    #     # print('ENTER: OuterJoin ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#outerJoin.
    # def exitOuterJoin(self, ctx:SelectSQLParser.OuterJoinContext):
    #     # print('EXIT:  OuterJoin ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#naturalJoin.
    # def enterNaturalJoin(self, ctx:SelectSQLParser.NaturalJoinContext):
    #     # print('ENTER: NaturalJoin ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#naturalJoin.
    # def exitNaturalJoin(self, ctx:SelectSQLParser.NaturalJoinContext):
    #     # print('EXIT:  NaturalJoin ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#queryExpression.
    # def enterQueryExpression(self, ctx:SelectSQLParser.QueryExpressionContext):
    #     print('ENTER: QueryExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     # self.pretty.append(('(', False))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#queryExpression.
    # def exitQueryExpression(self, ctx:SelectSQLParser.QueryExpressionContext):
    #     print('EXIT:  QueryExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     # self.pretty.append((')', False))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#querySpecification.
    # def enterQuerySpecification(self, ctx:SelectSQLParser.QuerySpecificationContext):
    #     print('ENTER: QuerySpecification ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#querySpecification.
    # def exitQuerySpecification(self, ctx:SelectSQLParser.QuerySpecificationContext):
    #     print('EXIT:  QuerySpecification ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#unionParenthesis.
    # def enterUnionParenthesis(self, ctx:SelectSQLParser.UnionParenthesisContext):
    #     # print('ENTER: UnionParenthesis ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#unionParenthesis.
    # def exitUnionParenthesis(self, ctx:SelectSQLParser.UnionParenthesisContext):
    #     # print('EXIT:  UnionParenthesis ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#unionStatement.
    # def enterUnionStatement(self, ctx:SelectSQLParser.UnionStatementContext):
    #     # print('ENTER: UnionStatement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#unionStatement.
    # def exitUnionStatement(self, ctx:SelectSQLParser.UnionStatementContext):
    #     # print('EXIT:  UnionStatement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#selectSpec.
    # def enterSelectSpec(self, ctx:SelectSQLParser.SelectSpecContext):
    #     # print('ENTER: SelectSpec ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#selectSpec.
    # def exitSelectSpec(self, ctx:SelectSQLParser.SelectSpecContext):
    #     # print('EXIT:  SelectSpec ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#selectElements.
    # def enterSelectElements(self, ctx:SelectSQLParser.SelectElementsContext):
    #     # print('ENTER: SelectElements ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#selectElements.
    # def exitSelectElements(self, ctx:SelectSQLParser.SelectElementsContext):
    #     # print('EXIT:  SelectElements ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#selectStarElement.
    # def enterSelectStarElement(self, ctx:SelectSQLParser.SelectStarElementContext):
    #     print('ENTER: SelectStarElement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#selectStarElement.
    # def exitSelectStarElement(self, ctx:SelectSQLParser.SelectStarElementContext):
    #     print('EXIT:  SelectStarElement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#selectColumnElement.
    # def enterSelectColumnElement(self, ctx:SelectSQLParser.SelectColumnElementContext):
    #     print('ENTER: SelectColumnElement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#selectColumnElement.
    # def exitSelectColumnElement(self, ctx:SelectSQLParser.SelectColumnElementContext):
    #     print('EXIT:  SelectColumnElement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#selectFunctionElement.
    # def enterSelectFunctionElement(self, ctx:SelectSQLParser.SelectFunctionElementContext):
    #     print('ENTER: SelectFunctionElement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#selectFunctionElement.
    # def exitSelectFunctionElement(self, ctx:SelectSQLParser.SelectFunctionElementContext):
    #     print('EXIT:  SelectFunctionElement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#selectExpressionElement.
    # def enterSelectExpressionElement(self, ctx:SelectSQLParser.SelectExpressionElementContext):
    #     print('ENTER: SelectExpressionElement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#selectExpressionElement.
    # def exitSelectExpressionElement(self, ctx:SelectSQLParser.SelectExpressionElementContext):
    #     print('EXIT:  SelectExpressionElement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#fromClause.
    # def enterFromClause(self, ctx:SelectSQLParser.FromClauseContext):
    #     # print('ENTER: FromClause ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#fromClause.
    # def exitFromClause(self, ctx:SelectSQLParser.FromClauseContext):
    #     # print('EXIT:  FromClause ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#groupByItem.
    # def enterGroupByItem(self, ctx:SelectSQLParser.GroupByItemContext):
    #     # print('ENTER: GroupByItem ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#groupByItem.
    # def exitGroupByItem(self, ctx:SelectSQLParser.GroupByItemContext):
    #     # print('EXIT:  GroupByItem ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#limitClause.
    # def enterLimitClause(self, ctx:SelectSQLParser.LimitClauseContext):
    #     # print('ENTER: LimitClause ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#limitClause.
    # def exitLimitClause(self, ctx:SelectSQLParser.LimitClauseContext):
    #     # print('EXIT:  LimitClause ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#fullId.
    # def enterFullId(self, ctx:SelectSQLParser.FullIdContext):
    #     # print('ENTER: FullId ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#fullId.
    # def exitFullId(self, ctx:SelectSQLParser.FullIdContext):
    #     # print('EXIT:  FullId ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#tableName.
    # def enterTableName(self, ctx:SelectSQLParser.TableNameContext):
    #     # print('ENTER: TableName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#tableName.
    # def exitTableName(self, ctx:SelectSQLParser.TableNameContext):
    #     # print('EXIT:  TableName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#fullColumnName.
    # def enterFullColumnName(self, ctx:SelectSQLParser.FullColumnNameContext):
    #     print('ENTER: FullColumnName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#fullColumnName.
    # def exitFullColumnName(self, ctx:SelectSQLParser.FullColumnNameContext):
    #     print('EXIT:  FullColumnName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#indexColumnName.
    # def enterIndexColumnName(self, ctx:SelectSQLParser.IndexColumnNameContext):
    #     # print('ENTER: IndexColumnName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#indexColumnName.
    # def exitIndexColumnName(self, ctx:SelectSQLParser.IndexColumnNameContext):
    #     # print('EXIT:  IndexColumnName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#userName.
    # def enterUserName(self, ctx:SelectSQLParser.UserNameContext):
    #     # print('ENTER: UserName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#userName.
    # def exitUserName(self, ctx:SelectSQLParser.UserNameContext):
    #     # print('EXIT:  UserName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#variable.
    # def enterVariable(self, ctx:SelectSQLParser.VariableContext):
    #     # print('ENTER: Variable ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#variable.
    # def exitVariable(self, ctx:SelectSQLParser.VariableContext):
    #     # print('EXIT:  Variable ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#charsetName.
    # def enterCharsetName(self, ctx:SelectSQLParser.CharsetNameContext):
    #     # print('ENTER: CharsetName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#charsetName.
    # def exitCharsetName(self, ctx:SelectSQLParser.CharsetNameContext):
    #     # print('EXIT:  CharsetName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#collationName.
    # def enterCollationName(self, ctx:SelectSQLParser.CollationNameContext):
    #     # print('ENTER: CollationName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#collationName.
    # def exitCollationName(self, ctx:SelectSQLParser.CollationNameContext):
    #     # print('EXIT:  CollationName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#engineName.
    # def enterEngineName(self, ctx:SelectSQLParser.EngineNameContext):
    #     # print('ENTER: EngineName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#engineName.
    # def exitEngineName(self, ctx:SelectSQLParser.EngineNameContext):
    #     # print('EXIT:  EngineName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#uuidSet.
    # def enterUuidSet(self, ctx:SelectSQLParser.UuidSetContext):
    #     # print('ENTER: UuidSet ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#uuidSet.
    # def exitUuidSet(self, ctx:SelectSQLParser.UuidSetContext):
    #     # print('EXIT:  UuidSet ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#xid.
    # def enterXid(self, ctx:SelectSQLParser.XidContext):
    #     # print('ENTER: Xid ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#xid.
    # def exitXid(self, ctx:SelectSQLParser.XidContext):
    #     # print('EXIT:  Xid ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#xuidStringId.
    # def enterXuidStringId(self, ctx:SelectSQLParser.XuidStringIdContext):
    #     # print('ENTER: XuidStringId ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#xuidStringId.
    # def exitXuidStringId(self, ctx:SelectSQLParser.XuidStringIdContext):
    #     # print('EXIT:  XuidStringId ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#authPlugin.
    # def enterAuthPlugin(self, ctx:SelectSQLParser.AuthPluginContext):
    #     # print('ENTER: AuthPlugin ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#authPlugin.
    # def exitAuthPlugin(self, ctx:SelectSQLParser.AuthPluginContext):
    #     # print('EXIT:  AuthPlugin ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#uid.
    # def enterUid(self, ctx:SelectSQLParser.UidContext):
    #     # print('ENTER: Uid ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#uid.
    # def exitUid(self, ctx:SelectSQLParser.UidContext):
    #     # print('EXIT:  Uid ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#simpleId.
    # def enterSimpleId(self, ctx:SelectSQLParser.SimpleIdContext):
    #     # print('ENTER: SimpleId ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#simpleId.
    # def exitSimpleId(self, ctx:SelectSQLParser.SimpleIdContext):
    #     # print('EXIT:  SimpleId ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#dottedId.
    # def enterDottedId(self, ctx:SelectSQLParser.DottedIdContext):
    #     # print('ENTER: DottedId ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#dottedId.
    # def exitDottedId(self, ctx:SelectSQLParser.DottedIdContext):
    #     # print('EXIT:  DottedId ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#decimalLiteral.
    # def enterDecimalLiteral(self, ctx:SelectSQLParser.DecimalLiteralContext):
    #     # print('ENTER: DecimalLiteral ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#decimalLiteral.
    # def exitDecimalLiteral(self, ctx:SelectSQLParser.DecimalLiteralContext):
    #     # print('EXIT:  DecimalLiteral ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#fileSizeLiteral.
    # def enterFileSizeLiteral(self, ctx:SelectSQLParser.FileSizeLiteralContext):
    #     # print('ENTER: FileSizeLiteral ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#fileSizeLiteral.
    # def exitFileSizeLiteral(self, ctx:SelectSQLParser.FileSizeLiteralContext):
    #     # print('EXIT:  FileSizeLiteral ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#stringLiteral.
    # def enterStringLiteral(self, ctx:SelectSQLParser.StringLiteralContext):
    #     # print('ENTER: StringLiteral ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#stringLiteral.
    # def exitStringLiteral(self, ctx:SelectSQLParser.StringLiteralContext):
    #     # print('EXIT:  StringLiteral ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#booleanLiteral.
    # def enterBooleanLiteral(self, ctx:SelectSQLParser.BooleanLiteralContext):
    #     # print('ENTER: BooleanLiteral ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#booleanLiteral.
    # def exitBooleanLiteral(self, ctx:SelectSQLParser.BooleanLiteralContext):
    #     # print('EXIT:  BooleanLiteral ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#hexadecimalLiteral.
    # def enterHexadecimalLiteral(self, ctx:SelectSQLParser.HexadecimalLiteralContext):
    #     # print('ENTER: HexadecimalLiteral ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#hexadecimalLiteral.
    # def exitHexadecimalLiteral(self, ctx:SelectSQLParser.HexadecimalLiteralContext):
    #     # print('EXIT:  HexadecimalLiteral ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#nullNotnull.
    # def enterNullNotnull(self, ctx:SelectSQLParser.NullNotnullContext):
    #     # print('ENTER: NullNotnull ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#nullNotnull.
    # def exitNullNotnull(self, ctx:SelectSQLParser.NullNotnullContext):
    #     # print('EXIT:  NullNotnull ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#constant.
    # def enterConstant(self, ctx:SelectSQLParser.ConstantContext):
    #     # print('ENTER: Constant ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#constant.
    # def exitConstant(self, ctx:SelectSQLParser.ConstantContext):
    #     # print('EXIT:  Constant ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#intervalType.
    # def enterIntervalType(self, ctx:SelectSQLParser.IntervalTypeContext):
    #     # print('ENTER: IntervalType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#intervalType.
    # def exitIntervalType(self, ctx:SelectSQLParser.IntervalTypeContext):
    #     # print('EXIT:  IntervalType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#stringDataType.
    # def enterStringDataType(self, ctx:SelectSQLParser.StringDataTypeContext):
    #     # print('ENTER: StringDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#stringDataType.
    # def exitStringDataType(self, ctx:SelectSQLParser.StringDataTypeContext):
    #     # print('EXIT:  StringDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#dimensionDataType.
    # def enterDimensionDataType(self, ctx:SelectSQLParser.DimensionDataTypeContext):
    #     # print('ENTER: DimensionDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#dimensionDataType.
    # def exitDimensionDataType(self, ctx:SelectSQLParser.DimensionDataTypeContext):
    #     # print('EXIT:  DimensionDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#simpleDataType.
    # def enterSimpleDataType(self, ctx:SelectSQLParser.SimpleDataTypeContext):
    #     # print('ENTER: SimpleDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#simpleDataType.
    # def exitSimpleDataType(self, ctx:SelectSQLParser.SimpleDataTypeContext):
    #     # print('EXIT:  SimpleDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#collectionDataType.
    # def enterCollectionDataType(self, ctx:SelectSQLParser.CollectionDataTypeContext):
    #     # print('ENTER: CollectionDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#collectionDataType.
    # def exitCollectionDataType(self, ctx:SelectSQLParser.CollectionDataTypeContext):
    #     # print('EXIT:  CollectionDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#spatialDataType.
    # def enterSpatialDataType(self, ctx:SelectSQLParser.SpatialDataTypeContext):
    #     # print('ENTER: SpatialDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#spatialDataType.
    # def exitSpatialDataType(self, ctx:SelectSQLParser.SpatialDataTypeContext):
    #     # print('EXIT:  SpatialDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#convertedDataType.
    # def enterConvertedDataType(self, ctx:SelectSQLParser.ConvertedDataTypeContext):
    #     # print('ENTER: ConvertedDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#convertedDataType.
    # def exitConvertedDataType(self, ctx:SelectSQLParser.ConvertedDataTypeContext):
    #     # print('EXIT:  ConvertedDataType ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#lengthOneDimension.
    # def enterLengthOneDimension(self, ctx:SelectSQLParser.LengthOneDimensionContext):
    #     # print('ENTER: LengthOneDimension ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#lengthOneDimension.
    # def exitLengthOneDimension(self, ctx:SelectSQLParser.LengthOneDimensionContext):
    #     # print('EXIT:  LengthOneDimension ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#lengthTwoDimension.
    # def enterLengthTwoDimension(self, ctx:SelectSQLParser.LengthTwoDimensionContext):
    #     # print('ENTER: LengthTwoDimension ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#lengthTwoDimension.
    # def exitLengthTwoDimension(self, ctx:SelectSQLParser.LengthTwoDimensionContext):
    #     # print('EXIT:  LengthTwoDimension ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#lengthTwoOptionalDimension.
    # def enterLengthTwoOptionalDimension(self, ctx:SelectSQLParser.LengthTwoOptionalDimensionContext):
    #     # print('ENTER: LengthTwoOptionalDimension ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#lengthTwoOptionalDimension.
    # def exitLengthTwoOptionalDimension(self, ctx:SelectSQLParser.LengthTwoOptionalDimensionContext):
    #     # print('EXIT:  LengthTwoOptionalDimension ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#uidList.
    # def enterUidList(self, ctx:SelectSQLParser.UidListContext):
    #     # print('ENTER: UidList ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#uidList.
    # def exitUidList(self, ctx:SelectSQLParser.UidListContext):
    #     # print('EXIT:  UidList ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#tables.
    # def enterTables(self, ctx:SelectSQLParser.TablesContext):
    #     # print('ENTER: Tables ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#tables.
    # def exitTables(self, ctx:SelectSQLParser.TablesContext):
    #     # print('EXIT:  Tables ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#indexColumnNames.
    # def enterIndexColumnNames(self, ctx:SelectSQLParser.IndexColumnNamesContext):
    #     # print('ENTER: IndexColumnNames ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#indexColumnNames.
    # def exitIndexColumnNames(self, ctx:SelectSQLParser.IndexColumnNamesContext):
    #     # print('EXIT:  IndexColumnNames ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#expressions.
    # def enterExpressions(self, ctx:SelectSQLParser.ExpressionsContext):
    #     # print('ENTER: Expressions ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#expressions.
    # def exitExpressions(self, ctx:SelectSQLParser.ExpressionsContext):
    #     # print('EXIT:  Expressions ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#expressionsWithDefaults.
    # def enterExpressionsWithDefaults(self, ctx:SelectSQLParser.ExpressionsWithDefaultsContext):
    #     # print('ENTER: ExpressionsWithDefaults ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#expressionsWithDefaults.
    # def exitExpressionsWithDefaults(self, ctx:SelectSQLParser.ExpressionsWithDefaultsContext):
    #     # print('EXIT:  ExpressionsWithDefaults ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#constants.
    # def enterConstants(self, ctx:SelectSQLParser.ConstantsContext):
    #     # print('ENTER: Constants ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#constants.
    # def exitConstants(self, ctx:SelectSQLParser.ConstantsContext):
    #     # print('EXIT:  Constants ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#simpleStrings.
    # def enterSimpleStrings(self, ctx:SelectSQLParser.SimpleStringsContext):
    #     # print('ENTER: SimpleStrings ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#simpleStrings.
    # def exitSimpleStrings(self, ctx:SelectSQLParser.SimpleStringsContext):
    #     # print('EXIT:  SimpleStrings ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#userVariables.
    # def enterUserVariables(self, ctx:SelectSQLParser.UserVariablesContext):
    #     # print('ENTER: UserVariables ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#userVariables.
    # def exitUserVariables(self, ctx:SelectSQLParser.UserVariablesContext):
    #     # print('EXIT:  UserVariables ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#defaultValue.
    # def enterDefaultValue(self, ctx:SelectSQLParser.DefaultValueContext):
    #     # print('ENTER: DefaultValue ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#defaultValue.
    # def exitDefaultValue(self, ctx:SelectSQLParser.DefaultValueContext):
    #     # print('EXIT:  DefaultValue ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#currentTimestamp.
    # def enterCurrentTimestamp(self, ctx:SelectSQLParser.CurrentTimestampContext):
    #     # print('ENTER: CurrentTimestamp ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#currentTimestamp.
    # def exitCurrentTimestamp(self, ctx:SelectSQLParser.CurrentTimestampContext):
    #     # print('EXIT:  CurrentTimestamp ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#expressionOrDefault.
    # def enterExpressionOrDefault(self, ctx:SelectSQLParser.ExpressionOrDefaultContext):
    #     # print('ENTER: ExpressionOrDefault ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#expressionOrDefault.
    # def exitExpressionOrDefault(self, ctx:SelectSQLParser.ExpressionOrDefaultContext):
    #     # print('EXIT:  ExpressionOrDefault ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#ifExists.
    # def enterIfExists(self, ctx:SelectSQLParser.IfExistsContext):
    #     # print('ENTER: IfExists ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#ifExists.
    # def exitIfExists(self, ctx:SelectSQLParser.IfExistsContext):
    #     # print('EXIT:  IfExists ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#ifNotExists.
    # def enterIfNotExists(self, ctx:SelectSQLParser.IfNotExistsContext):
    #     # print('ENTER: IfNotExists ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#ifNotExists.
    # def exitIfNotExists(self, ctx:SelectSQLParser.IfNotExistsContext):
    #     # print('EXIT:  IfNotExists ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#specificFunctionCall.
    # def enterSpecificFunctionCall(self, ctx:SelectSQLParser.SpecificFunctionCallContext):
    #     # print('ENTER: SpecificFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#specificFunctionCall.
    # def exitSpecificFunctionCall(self, ctx:SelectSQLParser.SpecificFunctionCallContext):
    #     # print('EXIT:  SpecificFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#aggregateFunctionCall.
    # def enterAggregateFunctionCall(self, ctx:SelectSQLParser.AggregateFunctionCallContext):
    #     # print('ENTER: AggregateFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#aggregateFunctionCall.
    # def exitAggregateFunctionCall(self, ctx:SelectSQLParser.AggregateFunctionCallContext):
    #     # print('EXIT:  AggregateFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#scalarFunctionCall.
    # def enterScalarFunctionCall(self, ctx:SelectSQLParser.ScalarFunctionCallContext):
    #     # print('ENTER: ScalarFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#scalarFunctionCall.
    # def exitScalarFunctionCall(self, ctx:SelectSQLParser.ScalarFunctionCallContext):
    #     # print('EXIT:  ScalarFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#udfFunctionCall.
    # def enterUdfFunctionCall(self, ctx:SelectSQLParser.UdfFunctionCallContext):
    #     # print('ENTER: UdfFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#udfFunctionCall.
    # def exitUdfFunctionCall(self, ctx:SelectSQLParser.UdfFunctionCallContext):
    #     # print('EXIT:  UdfFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#passwordFunctionCall.
    # def enterPasswordFunctionCall(self, ctx:SelectSQLParser.PasswordFunctionCallContext):
    #     # print('ENTER: PasswordFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#passwordFunctionCall.
    # def exitPasswordFunctionCall(self, ctx:SelectSQLParser.PasswordFunctionCallContext):
    #     # print('EXIT:  PasswordFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#simpleFunctionCall.
    # def enterSimpleFunctionCall(self, ctx:SelectSQLParser.SimpleFunctionCallContext):
    #     # print('ENTER: SimpleFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#simpleFunctionCall.
    # def exitSimpleFunctionCall(self, ctx:SelectSQLParser.SimpleFunctionCallContext):
    #     # print('EXIT:  SimpleFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#dataTypeFunctionCall.
    # def enterDataTypeFunctionCall(self, ctx:SelectSQLParser.DataTypeFunctionCallContext):
    #     # print('ENTER: DataTypeFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#dataTypeFunctionCall.
    # def exitDataTypeFunctionCall(self, ctx:SelectSQLParser.DataTypeFunctionCallContext):
    #     # print('EXIT:  DataTypeFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#valuesFunctionCall.
    # def enterValuesFunctionCall(self, ctx:SelectSQLParser.ValuesFunctionCallContext):
    #     # print('ENTER: ValuesFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#valuesFunctionCall.
    # def exitValuesFunctionCall(self, ctx:SelectSQLParser.ValuesFunctionCallContext):
    #     # print('EXIT:  ValuesFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#caseFunctionCall.
    # def enterCaseFunctionCall(self, ctx:SelectSQLParser.CaseFunctionCallContext):
    #     # print('ENTER: CaseFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#caseFunctionCall.
    # def exitCaseFunctionCall(self, ctx:SelectSQLParser.CaseFunctionCallContext):
    #     # print('EXIT:  CaseFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#charFunctionCall.
    # def enterCharFunctionCall(self, ctx:SelectSQLParser.CharFunctionCallContext):
    #     # print('ENTER: CharFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#charFunctionCall.
    # def exitCharFunctionCall(self, ctx:SelectSQLParser.CharFunctionCallContext):
    #     # print('EXIT:  CharFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#positionFunctionCall.
    # def enterPositionFunctionCall(self, ctx:SelectSQLParser.PositionFunctionCallContext):
    #     # print('ENTER: PositionFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#positionFunctionCall.
    # def exitPositionFunctionCall(self, ctx:SelectSQLParser.PositionFunctionCallContext):
    #     # print('EXIT:  PositionFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#substrFunctionCall.
    # def enterSubstrFunctionCall(self, ctx:SelectSQLParser.SubstrFunctionCallContext):
    #     # print('ENTER: SubstrFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#substrFunctionCall.
    # def exitSubstrFunctionCall(self, ctx:SelectSQLParser.SubstrFunctionCallContext):
    #     # print('EXIT:  SubstrFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#trimFunctionCall.
    # def enterTrimFunctionCall(self, ctx:SelectSQLParser.TrimFunctionCallContext):
    #     # print('ENTER: TrimFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#trimFunctionCall.
    # def exitTrimFunctionCall(self, ctx:SelectSQLParser.TrimFunctionCallContext):
    #     # print('EXIT:  TrimFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#weightFunctionCall.
    # def enterWeightFunctionCall(self, ctx:SelectSQLParser.WeightFunctionCallContext):
    #     # print('ENTER: WeightFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#weightFunctionCall.
    # def exitWeightFunctionCall(self, ctx:SelectSQLParser.WeightFunctionCallContext):
    #     # print('EXIT:  WeightFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#extractFunctionCall.
    # def enterExtractFunctionCall(self, ctx:SelectSQLParser.ExtractFunctionCallContext):
    #     # print('ENTER: ExtractFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#extractFunctionCall.
    # def exitExtractFunctionCall(self, ctx:SelectSQLParser.ExtractFunctionCallContext):
    #     # print('EXIT:  ExtractFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#getFormatFunctionCall.
    # def enterGetFormatFunctionCall(self, ctx:SelectSQLParser.GetFormatFunctionCallContext):
    #     # print('ENTER: GetFormatFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#getFormatFunctionCall.
    # def exitGetFormatFunctionCall(self, ctx:SelectSQLParser.GetFormatFunctionCallContext):
    #     # print('EXIT:  GetFormatFunctionCall ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#caseFuncAlternative.
    # def enterCaseFuncAlternative(self, ctx:SelectSQLParser.CaseFuncAlternativeContext):
    #     # print('ENTER: CaseFuncAlternative ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#caseFuncAlternative.
    # def exitCaseFuncAlternative(self, ctx:SelectSQLParser.CaseFuncAlternativeContext):
    #     # print('EXIT:  CaseFuncAlternative ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#levelWeightList.
    # def enterLevelWeightList(self, ctx:SelectSQLParser.LevelWeightListContext):
    #     # print('ENTER: LevelWeightList ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#levelWeightList.
    # def exitLevelWeightList(self, ctx:SelectSQLParser.LevelWeightListContext):
    #     # print('EXIT:  LevelWeightList ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#levelWeightRange.
    # def enterLevelWeightRange(self, ctx:SelectSQLParser.LevelWeightRangeContext):
    #     # print('ENTER: LevelWeightRange ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#levelWeightRange.
    # def exitLevelWeightRange(self, ctx:SelectSQLParser.LevelWeightRangeContext):
    #     # print('EXIT:  LevelWeightRange ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#levelInWeightListElement.
    # def enterLevelInWeightListElement(self, ctx:SelectSQLParser.LevelInWeightListElementContext):
    #     # print('ENTER: LevelInWeightListElement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#levelInWeightListElement.
    # def exitLevelInWeightListElement(self, ctx:SelectSQLParser.LevelInWeightListElementContext):
    #     # print('EXIT:  LevelInWeightListElement ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#aggregateWindowedFunction.
    # def enterAggregateWindowedFunction(self, ctx:SelectSQLParser.AggregateWindowedFunctionContext):
    #     # print('ENTER: AggregateWindowedFunction ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#aggregateWindowedFunction.
    # def exitAggregateWindowedFunction(self, ctx:SelectSQLParser.AggregateWindowedFunctionContext):
    #     # print('EXIT:  AggregateWindowedFunction ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#scalarFunctionName.
    # def enterScalarFunctionName(self, ctx:SelectSQLParser.ScalarFunctionNameContext):
    #     # print('ENTER: ScalarFunctionName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#scalarFunctionName.
    # def exitScalarFunctionName(self, ctx:SelectSQLParser.ScalarFunctionNameContext):
    #     # print('EXIT:  ScalarFunctionName ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#passwordFunctionClause.
    # def enterPasswordFunctionClause(self, ctx:SelectSQLParser.PasswordFunctionClauseContext):
    #     # print('ENTER: PasswordFunctionClause ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#passwordFunctionClause.
    # def exitPasswordFunctionClause(self, ctx:SelectSQLParser.PasswordFunctionClauseContext):
    #     # print('EXIT:  PasswordFunctionClause ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#functionArgs.
    # def enterFunctionArgs(self, ctx:SelectSQLParser.FunctionArgsContext):
    #     # print('ENTER: FunctionArgs ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#functionArgs.
    # def exitFunctionArgs(self, ctx:SelectSQLParser.FunctionArgsContext):
    #     # print('EXIT:  FunctionArgs ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#functionArg.
    # def enterFunctionArg(self, ctx:SelectSQLParser.FunctionArgContext):
    #     # print('ENTER: FunctionArg ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#functionArg.
    # def exitFunctionArg(self, ctx:SelectSQLParser.FunctionArgContext):
    #     # print('EXIT:  FunctionArg ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#isExpression.
    # def enterIsExpression(self, ctx:SelectSQLParser.IsExpressionContext):
    #     # print('ENTER: IsExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#isExpression.
    # def exitIsExpression(self, ctx:SelectSQLParser.IsExpressionContext):
    #     # print('EXIT:  IsExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#notExpression.
    # def enterNotExpression(self, ctx:SelectSQLParser.NotExpressionContext):
    #     # print('ENTER: NotExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#notExpression.
    # def exitNotExpression(self, ctx:SelectSQLParser.NotExpressionContext):
    #     # print('EXIT:  NotExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#logicalExpression.
    # def enterLogicalExpression(self, ctx:SelectSQLParser.LogicalExpressionContext):
    #     # print('ENTER: LogicalExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#logicalExpression.
    # def exitLogicalExpression(self, ctx:SelectSQLParser.LogicalExpressionContext):
    #     # print('EXIT:  LogicalExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#predicateExpression.
    # def enterPredicateExpression(self, ctx:SelectSQLParser.PredicateExpressionContext):
    #     # print('ENTER: PredicateExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#predicateExpression.
    # def exitPredicateExpression(self, ctx:SelectSQLParser.PredicateExpressionContext):
    #     # print('EXIT:  PredicateExpression ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#soundsLikePredicate.
    # def enterSoundsLikePredicate(self, ctx:SelectSQLParser.SoundsLikePredicateContext):
    #     # print('ENTER: SoundsLikePredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#soundsLikePredicate.
    # def exitSoundsLikePredicate(self, ctx:SelectSQLParser.SoundsLikePredicateContext):
    #     # print('EXIT:  SoundsLikePredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#expressionAtomPredicate.
    # def enterExpressionAtomPredicate(self, ctx:SelectSQLParser.ExpressionAtomPredicateContext):
    #     # print('ENTER: ExpressionAtomPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#expressionAtomPredicate.
    # def exitExpressionAtomPredicate(self, ctx:SelectSQLParser.ExpressionAtomPredicateContext):
    #     # print('EXIT:  ExpressionAtomPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#inPredicate.
    # def enterInPredicate(self, ctx:SelectSQLParser.InPredicateContext):
    #     # print('ENTER: InPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#inPredicate.
    # def exitInPredicate(self, ctx:SelectSQLParser.InPredicateContext):
    #     # print('EXIT:  InPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#subqueryComparasionPredicate.
    # def enterSubqueryComparasionPredicate(self, ctx:SelectSQLParser.SubqueryComparasionPredicateContext):
    #     # print('ENTER: SubqueryComparasionPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#subqueryComparasionPredicate.
    # def exitSubqueryComparasionPredicate(self, ctx:SelectSQLParser.SubqueryComparasionPredicateContext):
    #     # print('EXIT:  SubqueryComparasionPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#betweenPredicate.
    # def enterBetweenPredicate(self, ctx:SelectSQLParser.BetweenPredicateContext):
    #     # print('ENTER: BetweenPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#betweenPredicate.
    # def exitBetweenPredicate(self, ctx:SelectSQLParser.BetweenPredicateContext):
    #     # print('EXIT:  BetweenPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#binaryComparasionPredicate.
    # def enterBinaryComparasionPredicate(self, ctx:SelectSQLParser.BinaryComparasionPredicateContext):
    #     # print('ENTER: BinaryComparasionPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#binaryComparasionPredicate.
    # def exitBinaryComparasionPredicate(self, ctx:SelectSQLParser.BinaryComparasionPredicateContext):
    #     # print('EXIT:  BinaryComparasionPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#isNullPredicate.
    # def enterIsNullPredicate(self, ctx:SelectSQLParser.IsNullPredicateContext):
    #     # print('ENTER: IsNullPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#isNullPredicate.
    # def exitIsNullPredicate(self, ctx:SelectSQLParser.IsNullPredicateContext):
    #     # print('EXIT:  IsNullPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#likePredicate.
    # def enterLikePredicate(self, ctx:SelectSQLParser.LikePredicateContext):
    #     # print('ENTER: LikePredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#likePredicate.
    # def exitLikePredicate(self, ctx:SelectSQLParser.LikePredicateContext):
    #     # print('EXIT:  LikePredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#regexpPredicate.
    # def enterRegexpPredicate(self, ctx:SelectSQLParser.RegexpPredicateContext):
    #     # print('ENTER: RegexpPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#regexpPredicate.
    # def exitRegexpPredicate(self, ctx:SelectSQLParser.RegexpPredicateContext):
    #     # print('EXIT:  RegexpPredicate ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#unaryExpressionAtom.
    # def enterUnaryExpressionAtom(self, ctx:SelectSQLParser.UnaryExpressionAtomContext):
    #     # print('ENTER: UnaryExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#unaryExpressionAtom.
    # def exitUnaryExpressionAtom(self, ctx:SelectSQLParser.UnaryExpressionAtomContext):
    #     # print('EXIT:  UnaryExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#collateExpressionAtom.
    # def enterCollateExpressionAtom(self, ctx:SelectSQLParser.CollateExpressionAtomContext):
    #     # print('ENTER: CollateExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#collateExpressionAtom.
    # def exitCollateExpressionAtom(self, ctx:SelectSQLParser.CollateExpressionAtomContext):
    #     # print('EXIT:  CollateExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#subqueryExpessionAtom.
    # def enterSubqueryExpessionAtom(self, ctx:SelectSQLParser.SubqueryExpessionAtomContext):
    #     # print('ENTER: SubqueryExpessionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#subqueryExpessionAtom.
    # def exitSubqueryExpessionAtom(self, ctx:SelectSQLParser.SubqueryExpessionAtomContext):
    #     # print('EXIT:  SubqueryExpessionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#nestedExpressionAtom.
    # def enterNestedExpressionAtom(self, ctx:SelectSQLParser.NestedExpressionAtomContext):
    #     # print('ENTER: NestedExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#nestedExpressionAtom.
    # def exitNestedExpressionAtom(self, ctx:SelectSQLParser.NestedExpressionAtomContext):
    #     # print('EXIT:  NestedExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#nestedRowExpressionAtom.
    # def enterNestedRowExpressionAtom(self, ctx:SelectSQLParser.NestedRowExpressionAtomContext):
    #     # print('ENTER: NestedRowExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#nestedRowExpressionAtom.
    # def exitNestedRowExpressionAtom(self, ctx:SelectSQLParser.NestedRowExpressionAtomContext):
    #     # print('EXIT:  NestedRowExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#mathExpressionAtom.
    # def enterMathExpressionAtom(self, ctx:SelectSQLParser.MathExpressionAtomContext):
    #     # print('ENTER: MathExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#mathExpressionAtom.
    # def exitMathExpressionAtom(self, ctx:SelectSQLParser.MathExpressionAtomContext):
    #     # print('EXIT:  MathExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#intervalExpressionAtom.
    # def enterIntervalExpressionAtom(self, ctx:SelectSQLParser.IntervalExpressionAtomContext):
    #     # print('ENTER: IntervalExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#intervalExpressionAtom.
    # def exitIntervalExpressionAtom(self, ctx:SelectSQLParser.IntervalExpressionAtomContext):
    #     # print('EXIT:  IntervalExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#existsExpessionAtom.
    # def enterExistsExpessionAtom(self, ctx:SelectSQLParser.ExistsExpessionAtomContext):
    #     # print('ENTER: ExistsExpessionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#existsExpessionAtom.
    # def exitExistsExpessionAtom(self, ctx:SelectSQLParser.ExistsExpessionAtomContext):
    #     # print('EXIT:  ExistsExpessionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#constantExpressionAtom.
    # def enterConstantExpressionAtom(self, ctx:SelectSQLParser.ConstantExpressionAtomContext):
    #     # print('ENTER: ConstantExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#constantExpressionAtom.
    # def exitConstantExpressionAtom(self, ctx:SelectSQLParser.ConstantExpressionAtomContext):
    #     # print('EXIT:  ConstantExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#functionCallExpressionAtom.
    # def enterFunctionCallExpressionAtom(self, ctx:SelectSQLParser.FunctionCallExpressionAtomContext):
    #     # print('ENTER: FunctionCallExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#functionCallExpressionAtom.
    # def exitFunctionCallExpressionAtom(self, ctx:SelectSQLParser.FunctionCallExpressionAtomContext):
    #     # print('EXIT:  FunctionCallExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#binaryExpressionAtom.
    # def enterBinaryExpressionAtom(self, ctx:SelectSQLParser.BinaryExpressionAtomContext):
    #     # print('ENTER: BinaryExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#binaryExpressionAtom.
    # def exitBinaryExpressionAtom(self, ctx:SelectSQLParser.BinaryExpressionAtomContext):
    #     # print('EXIT:  BinaryExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#fullColumnNameExpressionAtom.
    # def enterFullColumnNameExpressionAtom(self, ctx:SelectSQLParser.FullColumnNameExpressionAtomContext):
    #     # print('ENTER: FullColumnNameExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#fullColumnNameExpressionAtom.
    # def exitFullColumnNameExpressionAtom(self, ctx:SelectSQLParser.FullColumnNameExpressionAtomContext):
    #     # print('EXIT:  FullColumnNameExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#bitExpressionAtom.
    # def enterBitExpressionAtom(self, ctx:SelectSQLParser.BitExpressionAtomContext):
    #     # print('ENTER: BitExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#bitExpressionAtom.
    # def exitBitExpressionAtom(self, ctx:SelectSQLParser.BitExpressionAtomContext):
    #     # print('EXIT:  BitExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#variableExpressionAtom.
    # def enterVariableExpressionAtom(self, ctx:SelectSQLParser.VariableExpressionAtomContext):
    #     # print('ENTER: VariableExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#variableExpressionAtom.
    # def exitVariableExpressionAtom(self, ctx:SelectSQLParser.VariableExpressionAtomContext):
    #     # print('EXIT:  VariableExpressionAtom ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#unaryOperator.
    # def enterUnaryOperator(self, ctx:SelectSQLParser.UnaryOperatorContext):
    #     # print('ENTER: UnaryOperator ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#unaryOperator.
    # def exitUnaryOperator(self, ctx:SelectSQLParser.UnaryOperatorContext):
    #     # print('EXIT:  UnaryOperator ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#comparisonOperator.
    # def enterComparisonOperator(self, ctx:SelectSQLParser.ComparisonOperatorContext):
    #     # print('ENTER: ComparisonOperator ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#comparisonOperator.
    # def exitComparisonOperator(self, ctx:SelectSQLParser.ComparisonOperatorContext):
    #     # print('EXIT:  ComparisonOperator ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#logicalOperator.
    # def enterLogicalOperator(self, ctx:SelectSQLParser.LogicalOperatorContext):
    #     # print('ENTER: LogicalOperator ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#logicalOperator.
    # def exitLogicalOperator(self, ctx:SelectSQLParser.LogicalOperatorContext):
    #     # print('EXIT:  LogicalOperator ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#bitOperator.
    # def enterBitOperator(self, ctx:SelectSQLParser.BitOperatorContext):
    #     # print('ENTER: BitOperator ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#bitOperator.
    # def exitBitOperator(self, ctx:SelectSQLParser.BitOperatorContext):
    #     # print('EXIT:  BitOperator ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#mathOperator.
    # def enterMathOperator(self, ctx:SelectSQLParser.MathOperatorContext):
    #     # print('ENTER: MathOperator ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#mathOperator.
    # def exitMathOperator(self, ctx:SelectSQLParser.MathOperatorContext):
    #     # print('EXIT:  MathOperator ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#charsetNameBase.
    # def enterCharsetNameBase(self, ctx:SelectSQLParser.CharsetNameBaseContext):
    #     # print('ENTER: CharsetNameBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#charsetNameBase.
    # def exitCharsetNameBase(self, ctx:SelectSQLParser.CharsetNameBaseContext):
    #     # print('EXIT:  CharsetNameBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#transactionLevelBase.
    # def enterTransactionLevelBase(self, ctx:SelectSQLParser.TransactionLevelBaseContext):
    #     # print('ENTER: TransactionLevelBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#transactionLevelBase.
    # def exitTransactionLevelBase(self, ctx:SelectSQLParser.TransactionLevelBaseContext):
    #     # print('EXIT:  TransactionLevelBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#privilegesBase.
    # def enterPrivilegesBase(self, ctx:SelectSQLParser.PrivilegesBaseContext):
    #     # print('ENTER: PrivilegesBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#privilegesBase.
    # def exitPrivilegesBase(self, ctx:SelectSQLParser.PrivilegesBaseContext):
    #     # print('EXIT:  PrivilegesBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#intervalTypeBase.
    # def enterIntervalTypeBase(self, ctx:SelectSQLParser.IntervalTypeBaseContext):
    #     # print('ENTER: IntervalTypeBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#intervalTypeBase.
    # def exitIntervalTypeBase(self, ctx:SelectSQLParser.IntervalTypeBaseContext):
    #     # print('EXIT:  IntervalTypeBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#dataTypeBase.
    # def enterDataTypeBase(self, ctx:SelectSQLParser.DataTypeBaseContext):
    #     # print('ENTER: DataTypeBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#dataTypeBase.
    # def exitDataTypeBase(self, ctx:SelectSQLParser.DataTypeBaseContext):
    #     # print('EXIT:  DataTypeBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#keywordsCanBeId.
    # def enterKeywordsCanBeId(self, ctx:SelectSQLParser.KeywordsCanBeIdContext):
    #     # print('ENTER: KeywordsCanBeId ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#keywordsCanBeId.
    # def exitKeywordsCanBeId(self, ctx:SelectSQLParser.KeywordsCanBeIdContext):
    #     # print('EXIT:  KeywordsCanBeId ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass


    # # Enter a parse tree produced by SelectSQLParser#functionNameBase.
    # def enterFunctionNameBase(self, ctx:SelectSQLParser.FunctionNameBaseContext):
    #     # print('ENTER: FunctionNameBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass

    # # Exit a parse tree produced by SelectSQLParser#functionNameBase.
    # def exitFunctionNameBase(self, ctx:SelectSQLParser.FunctionNameBaseContext):
    #     # print('EXIT:  FunctionNameBase ({}, {})'.format(ctx.getText(), ctx.getChildCount()))
    #     pass



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


def norm_column_name(cname):
    cname = cname.upper()
    if len(cname.split('`')) == 3:
        cname = cname.split('`')[1]
    elif len(cname) > 2:
        cname = cname.split('.')[-1]
    return cname



subqueryContext = (SelectSQLParser.SimpleSelectContext,
                   SelectSQLParser.ParenthesisSelectContext,
                   SelectSQLParser.UnionSelectContext,
                   SelectSQLParser.UnionParenthesisSelectContext,)

def traverse(ctx, tableNameDict, columnNameDict):
    AGG_COLUMN_DICT = True  # any non-string value
    child_cnt = ctx.getChildCount()
    if child_cnt == 0:  # At a leaf of parse tree
        text = ctx.getText()
        #if len(text) >= 2 and text[0] == text[-1]:
        #    if text[0] == '"':
        #        text = text[1:-1]
        #        text = text.replace("\\'", "'").replace('\\"', '"')
        #        text = "'{}'".format(text)
        #else:
        #    text = text.replace('"', "'")
        #if text == '==': text = '='
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
        # column_save = columnNameDict.copy()
        text, tableNameDict, columnNameDict = traverse(child, tableNameDict, columnNameDict)
        # print(ctx.getText(), columnNameDict, column_save)
        if isinstance(child, (SelectSQLParser.QuerySpecificationContext,
                              SelectSQLParser.QueryExpressionContext)):
            tableNameDict = table_save
            # columnNameDict = column_save
        texts[idx] = text

    for idx in range(child_cnt):
        tokens.append(texts[idx])

    # Column in Select clause
    if isinstance(ctx, (SelectSQLParser.SelectColumnElementContext,
                        SelectSQLParser.SelectFunctionElementContext)):
        assign_tokens = []
        if isinstance(ctx, SelectSQLParser.SelectExpressionElementContext):
            if child_cnt >= 3 and tokens[1][0] == ':=':
                assign_tokens = tokens[:2]
                tokens = tokens[2:]
                child_cnt -= 2
        column_name = tokens[-1][-1]
        is_agg = (len(tokens) > 1 and '(' in tokens[0] and ')' in tokens[0])
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
        if not is_agg:
            column_dict = columnNameDict.get(None, {})
            column_dict[norm_column_name(column_name)] = norm_column_name(column_alias)
            columnNameDict[None] = column_dict
        else:
            column_dict = columnNameDict.get(AGG_COLUMN_DICT, {})
            column_dict[norm_column_name(column_name)] = norm_column_name(column_alias)
            columnNameDict[AGG_COLUMN_DICT] = column_dict
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
            table_name = tableNameDict[table_name]
            column_name = ''.join(tokens[1])
            assert(column_name[0] == '.')
            column_name = column_name[1:]
            # print(table_name, column_name, columnNameDict)
            column_dict = columnNameDict.get(table_name)
            if column_dict:
                column_name = column_dict[norm_column_name(column_name)]
            column_name = '.' + column_name
            tokens = [[table_name], [column_name]]
        elif child_cnt == 1:
            table_name = tableNameDict[None]
            column_dict = columnNameDict.get(table_name)
            if column_dict and len(tokens) == 1:
                #print(collumnNameDict)
                #print(column_dict)
                tokens[0][0] = column_dict[norm_column_name(tokens[0][0])]
            column_dict = columnNameDict.get(AGG_COLUMN_DICT)
            if column_dict and len(tokens) == 1 and column_dict.get(norm_column_name(tokens[0][0])) is not None:
                pass
            else:
                tokens = [[table_name], ['.'], tokens[0]]
    # Table in From clause (1 Table Item)
    elif isinstance(ctx, SelectSQLParser.AtomTableItemContext):
        assert(1 <= child_cnt <= 3)
        assert(len(tokens[0]) == 1)
        table_name = tokens[0][0]
        if child_cnt == 1:
            table_alias = getTableName()
        else:
            assert(len(tokens[-1]) == 1)
            table_alias = tokens[-1][0]
            table_name = table_alias
        tokens = [tokens[0], ['AS'], [table_alias]]
        tableNameDict[table_name] = table_alias
        tableNameDict[None] = table_alias
    # Table in From clause (Subquery as a table)
    elif isinstance(ctx, SelectSQLParser.SubqueryTableItemContext):
        assert(len(tokens[-1]) == 1)
        table_name = tokens[-1][0]
        # print(table_name, columnNameDict)
        tableNameDict[table_name] = table_name
        tableNameDict[None] = table_name
        column_dict = columnNameDict.get(None, {})
        added_column_dict = columnNameDict.get(AGG_COLUMN_DICT, {})
        column_list = list(column_dict.items()) + list(added_column_dict.items())
        columnNameDict[table_name] = dict(column_list)
        columnNameDict[None] = {}
        columnNameDict[AGG_COLUMN_DICT] = {}
        if tokens[-2][0].upper() == 'AS':
            pass
        else:
            tokens = tokens[:-1] + [['AS']] + tokens[-1:]

    tokens = [x for y in tokens for x in y]

    return tokens, tableNameDict, columnNameDict


def alias_sql(candidate, show=False):
    resetName()
    if len(candidate) > 0 and candidate[-1] == ';':
        candidate = candidate[:-1]
    lexer = SelectSQLLexer(InputStream(candidate))
    stream = CommonTokenStream(lexer)
    parser = SelectSQLParser(stream)
    recognition_error = False
    printer = MyListener()
    ctx = parser.root()
    #print("!!", candidate)
    #print(ctx)
    walker = ParseTreeWalker()
    walker.walk(printer, ctx)

    if parser.getNumberOfSyntaxErrors() > 0:
        return ''

    sql, _, _ = traverse(ctx, {}, {})
    #try:
    #    sql, _, _ = traverse(ctx, {}, {})
    #except Exception as e:
    #    print('')
    #    print(repr(e), 'in Alias')
    #    print('')
    #    print(candidate)
    #    print('')
    #    return ''
    #    # raise Exception
    
    if sql[-1] == '<EOF>':
        sql = sql[:-1]

    sql_pretty = ' '.join(sql)
    sql_pretty = sql_pretty.replace('= =', '=')  # error from cludes sqlite3 grammar
    # sql_pretty = sql_pretty.replace(' .', '.').replace('. ', '.')
    # sql_pretty = sql_pretty.replace(' ,', ',')
    if show:
        print(sys.argv[1])
        print('')
        print(sql_pretty)

    return sql_pretty

    

if __name__ == '__main__':
    import sys
    print('')
    alias_sql(sys.argv[1], show=True)
    print('')

