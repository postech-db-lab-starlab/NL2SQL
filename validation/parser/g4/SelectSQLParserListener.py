# Generated from g4/SelectSQLParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SelectSQLParser import SelectSQLParser
else:
    from SelectSQLParser import SelectSQLParser

# This class defines a complete listener for a parse tree produced by SelectSQLParser.
class SelectSQLParserListener(ParseTreeListener):

    # Enter a parse tree produced by SelectSQLParser#root.
    def enterRoot(self, ctx:SelectSQLParser.RootContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#root.
    def exitRoot(self, ctx:SelectSQLParser.RootContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#simpleSelect.
    def enterSimpleSelect(self, ctx:SelectSQLParser.SimpleSelectContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#simpleSelect.
    def exitSimpleSelect(self, ctx:SelectSQLParser.SimpleSelectContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#parenthesisSelect.
    def enterParenthesisSelect(self, ctx:SelectSQLParser.ParenthesisSelectContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#parenthesisSelect.
    def exitParenthesisSelect(self, ctx:SelectSQLParser.ParenthesisSelectContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#unionSelect.
    def enterUnionSelect(self, ctx:SelectSQLParser.UnionSelectContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#unionSelect.
    def exitUnionSelect(self, ctx:SelectSQLParser.UnionSelectContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#unionParenthesisSelect.
    def enterUnionParenthesisSelect(self, ctx:SelectSQLParser.UnionParenthesisSelectContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#unionParenthesisSelect.
    def exitUnionParenthesisSelect(self, ctx:SelectSQLParser.UnionParenthesisSelectContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#orderByClause.
    def enterOrderByClause(self, ctx:SelectSQLParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#orderByClause.
    def exitOrderByClause(self, ctx:SelectSQLParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#orderByExpression.
    def enterOrderByExpression(self, ctx:SelectSQLParser.OrderByExpressionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#orderByExpression.
    def exitOrderByExpression(self, ctx:SelectSQLParser.OrderByExpressionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#tableSources.
    def enterTableSources(self, ctx:SelectSQLParser.TableSourcesContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#tableSources.
    def exitTableSources(self, ctx:SelectSQLParser.TableSourcesContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#tableSourceBase.
    def enterTableSourceBase(self, ctx:SelectSQLParser.TableSourceBaseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#tableSourceBase.
    def exitTableSourceBase(self, ctx:SelectSQLParser.TableSourceBaseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#tableSourceNested.
    def enterTableSourceNested(self, ctx:SelectSQLParser.TableSourceNestedContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#tableSourceNested.
    def exitTableSourceNested(self, ctx:SelectSQLParser.TableSourceNestedContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#atomTableItem.
    def enterAtomTableItem(self, ctx:SelectSQLParser.AtomTableItemContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#atomTableItem.
    def exitAtomTableItem(self, ctx:SelectSQLParser.AtomTableItemContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#subqueryTableItem.
    def enterSubqueryTableItem(self, ctx:SelectSQLParser.SubqueryTableItemContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#subqueryTableItem.
    def exitSubqueryTableItem(self, ctx:SelectSQLParser.SubqueryTableItemContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#tableSourcesItem.
    def enterTableSourcesItem(self, ctx:SelectSQLParser.TableSourcesItemContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#tableSourcesItem.
    def exitTableSourcesItem(self, ctx:SelectSQLParser.TableSourcesItemContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#indexHint.
    def enterIndexHint(self, ctx:SelectSQLParser.IndexHintContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#indexHint.
    def exitIndexHint(self, ctx:SelectSQLParser.IndexHintContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#indexHintType.
    def enterIndexHintType(self, ctx:SelectSQLParser.IndexHintTypeContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#indexHintType.
    def exitIndexHintType(self, ctx:SelectSQLParser.IndexHintTypeContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#innerJoin.
    def enterInnerJoin(self, ctx:SelectSQLParser.InnerJoinContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#innerJoin.
    def exitInnerJoin(self, ctx:SelectSQLParser.InnerJoinContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#straightJoin.
    def enterStraightJoin(self, ctx:SelectSQLParser.StraightJoinContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#straightJoin.
    def exitStraightJoin(self, ctx:SelectSQLParser.StraightJoinContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#outerJoin.
    def enterOuterJoin(self, ctx:SelectSQLParser.OuterJoinContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#outerJoin.
    def exitOuterJoin(self, ctx:SelectSQLParser.OuterJoinContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#naturalJoin.
    def enterNaturalJoin(self, ctx:SelectSQLParser.NaturalJoinContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#naturalJoin.
    def exitNaturalJoin(self, ctx:SelectSQLParser.NaturalJoinContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#queryExpression.
    def enterQueryExpression(self, ctx:SelectSQLParser.QueryExpressionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#queryExpression.
    def exitQueryExpression(self, ctx:SelectSQLParser.QueryExpressionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#querySpecification.
    def enterQuerySpecification(self, ctx:SelectSQLParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#querySpecification.
    def exitQuerySpecification(self, ctx:SelectSQLParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#unionParenthesis.
    def enterUnionParenthesis(self, ctx:SelectSQLParser.UnionParenthesisContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#unionParenthesis.
    def exitUnionParenthesis(self, ctx:SelectSQLParser.UnionParenthesisContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#unionStatement.
    def enterUnionStatement(self, ctx:SelectSQLParser.UnionStatementContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#unionStatement.
    def exitUnionStatement(self, ctx:SelectSQLParser.UnionStatementContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#selectSpec.
    def enterSelectSpec(self, ctx:SelectSQLParser.SelectSpecContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#selectSpec.
    def exitSelectSpec(self, ctx:SelectSQLParser.SelectSpecContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#selectElements.
    def enterSelectElements(self, ctx:SelectSQLParser.SelectElementsContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#selectElements.
    def exitSelectElements(self, ctx:SelectSQLParser.SelectElementsContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#selectStarElement.
    def enterSelectStarElement(self, ctx:SelectSQLParser.SelectStarElementContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#selectStarElement.
    def exitSelectStarElement(self, ctx:SelectSQLParser.SelectStarElementContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#selectColumnElement.
    def enterSelectColumnElement(self, ctx:SelectSQLParser.SelectColumnElementContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#selectColumnElement.
    def exitSelectColumnElement(self, ctx:SelectSQLParser.SelectColumnElementContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#selectFunctionElement.
    def enterSelectFunctionElement(self, ctx:SelectSQLParser.SelectFunctionElementContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#selectFunctionElement.
    def exitSelectFunctionElement(self, ctx:SelectSQLParser.SelectFunctionElementContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#selectExpressionElement.
    def enterSelectExpressionElement(self, ctx:SelectSQLParser.SelectExpressionElementContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#selectExpressionElement.
    def exitSelectExpressionElement(self, ctx:SelectSQLParser.SelectExpressionElementContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#fromClause.
    def enterFromClause(self, ctx:SelectSQLParser.FromClauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#fromClause.
    def exitFromClause(self, ctx:SelectSQLParser.FromClauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#groupByItem.
    def enterGroupByItem(self, ctx:SelectSQLParser.GroupByItemContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#groupByItem.
    def exitGroupByItem(self, ctx:SelectSQLParser.GroupByItemContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#limitClause.
    def enterLimitClause(self, ctx:SelectSQLParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#limitClause.
    def exitLimitClause(self, ctx:SelectSQLParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#fullId.
    def enterFullId(self, ctx:SelectSQLParser.FullIdContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#fullId.
    def exitFullId(self, ctx:SelectSQLParser.FullIdContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#tableName.
    def enterTableName(self, ctx:SelectSQLParser.TableNameContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#tableName.
    def exitTableName(self, ctx:SelectSQLParser.TableNameContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#fullColumnName.
    def enterFullColumnName(self, ctx:SelectSQLParser.FullColumnNameContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#fullColumnName.
    def exitFullColumnName(self, ctx:SelectSQLParser.FullColumnNameContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#indexColumnName.
    def enterIndexColumnName(self, ctx:SelectSQLParser.IndexColumnNameContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#indexColumnName.
    def exitIndexColumnName(self, ctx:SelectSQLParser.IndexColumnNameContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#userName.
    def enterUserName(self, ctx:SelectSQLParser.UserNameContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#userName.
    def exitUserName(self, ctx:SelectSQLParser.UserNameContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#variable.
    def enterVariable(self, ctx:SelectSQLParser.VariableContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#variable.
    def exitVariable(self, ctx:SelectSQLParser.VariableContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#charsetName.
    def enterCharsetName(self, ctx:SelectSQLParser.CharsetNameContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#charsetName.
    def exitCharsetName(self, ctx:SelectSQLParser.CharsetNameContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#collationName.
    def enterCollationName(self, ctx:SelectSQLParser.CollationNameContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#collationName.
    def exitCollationName(self, ctx:SelectSQLParser.CollationNameContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#engineName.
    def enterEngineName(self, ctx:SelectSQLParser.EngineNameContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#engineName.
    def exitEngineName(self, ctx:SelectSQLParser.EngineNameContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#uuidSet.
    def enterUuidSet(self, ctx:SelectSQLParser.UuidSetContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#uuidSet.
    def exitUuidSet(self, ctx:SelectSQLParser.UuidSetContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#xid.
    def enterXid(self, ctx:SelectSQLParser.XidContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#xid.
    def exitXid(self, ctx:SelectSQLParser.XidContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#xuidStringId.
    def enterXuidStringId(self, ctx:SelectSQLParser.XuidStringIdContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#xuidStringId.
    def exitXuidStringId(self, ctx:SelectSQLParser.XuidStringIdContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#authPlugin.
    def enterAuthPlugin(self, ctx:SelectSQLParser.AuthPluginContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#authPlugin.
    def exitAuthPlugin(self, ctx:SelectSQLParser.AuthPluginContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#uid.
    def enterUid(self, ctx:SelectSQLParser.UidContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#uid.
    def exitUid(self, ctx:SelectSQLParser.UidContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#simpleId.
    def enterSimpleId(self, ctx:SelectSQLParser.SimpleIdContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#simpleId.
    def exitSimpleId(self, ctx:SelectSQLParser.SimpleIdContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#dottedId.
    def enterDottedId(self, ctx:SelectSQLParser.DottedIdContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#dottedId.
    def exitDottedId(self, ctx:SelectSQLParser.DottedIdContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:SelectSQLParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:SelectSQLParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#fileSizeLiteral.
    def enterFileSizeLiteral(self, ctx:SelectSQLParser.FileSizeLiteralContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#fileSizeLiteral.
    def exitFileSizeLiteral(self, ctx:SelectSQLParser.FileSizeLiteralContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#stringLiteral.
    def enterStringLiteral(self, ctx:SelectSQLParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#stringLiteral.
    def exitStringLiteral(self, ctx:SelectSQLParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SelectSQLParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SelectSQLParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#hexadecimalLiteral.
    def enterHexadecimalLiteral(self, ctx:SelectSQLParser.HexadecimalLiteralContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#hexadecimalLiteral.
    def exitHexadecimalLiteral(self, ctx:SelectSQLParser.HexadecimalLiteralContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#nullNotnull.
    def enterNullNotnull(self, ctx:SelectSQLParser.NullNotnullContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#nullNotnull.
    def exitNullNotnull(self, ctx:SelectSQLParser.NullNotnullContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#constant.
    def enterConstant(self, ctx:SelectSQLParser.ConstantContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#constant.
    def exitConstant(self, ctx:SelectSQLParser.ConstantContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#intervalType.
    def enterIntervalType(self, ctx:SelectSQLParser.IntervalTypeContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#intervalType.
    def exitIntervalType(self, ctx:SelectSQLParser.IntervalTypeContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#stringDataType.
    def enterStringDataType(self, ctx:SelectSQLParser.StringDataTypeContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#stringDataType.
    def exitStringDataType(self, ctx:SelectSQLParser.StringDataTypeContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#dimensionDataType.
    def enterDimensionDataType(self, ctx:SelectSQLParser.DimensionDataTypeContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#dimensionDataType.
    def exitDimensionDataType(self, ctx:SelectSQLParser.DimensionDataTypeContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#simpleDataType.
    def enterSimpleDataType(self, ctx:SelectSQLParser.SimpleDataTypeContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#simpleDataType.
    def exitSimpleDataType(self, ctx:SelectSQLParser.SimpleDataTypeContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#collectionDataType.
    def enterCollectionDataType(self, ctx:SelectSQLParser.CollectionDataTypeContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#collectionDataType.
    def exitCollectionDataType(self, ctx:SelectSQLParser.CollectionDataTypeContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#spatialDataType.
    def enterSpatialDataType(self, ctx:SelectSQLParser.SpatialDataTypeContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#spatialDataType.
    def exitSpatialDataType(self, ctx:SelectSQLParser.SpatialDataTypeContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#convertedDataType.
    def enterConvertedDataType(self, ctx:SelectSQLParser.ConvertedDataTypeContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#convertedDataType.
    def exitConvertedDataType(self, ctx:SelectSQLParser.ConvertedDataTypeContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#lengthOneDimension.
    def enterLengthOneDimension(self, ctx:SelectSQLParser.LengthOneDimensionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#lengthOneDimension.
    def exitLengthOneDimension(self, ctx:SelectSQLParser.LengthOneDimensionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#lengthTwoDimension.
    def enterLengthTwoDimension(self, ctx:SelectSQLParser.LengthTwoDimensionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#lengthTwoDimension.
    def exitLengthTwoDimension(self, ctx:SelectSQLParser.LengthTwoDimensionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#lengthTwoOptionalDimension.
    def enterLengthTwoOptionalDimension(self, ctx:SelectSQLParser.LengthTwoOptionalDimensionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#lengthTwoOptionalDimension.
    def exitLengthTwoOptionalDimension(self, ctx:SelectSQLParser.LengthTwoOptionalDimensionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#uidList.
    def enterUidList(self, ctx:SelectSQLParser.UidListContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#uidList.
    def exitUidList(self, ctx:SelectSQLParser.UidListContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#tables.
    def enterTables(self, ctx:SelectSQLParser.TablesContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#tables.
    def exitTables(self, ctx:SelectSQLParser.TablesContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#indexColumnNames.
    def enterIndexColumnNames(self, ctx:SelectSQLParser.IndexColumnNamesContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#indexColumnNames.
    def exitIndexColumnNames(self, ctx:SelectSQLParser.IndexColumnNamesContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#expressions.
    def enterExpressions(self, ctx:SelectSQLParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#expressions.
    def exitExpressions(self, ctx:SelectSQLParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#expressionsWithDefaults.
    def enterExpressionsWithDefaults(self, ctx:SelectSQLParser.ExpressionsWithDefaultsContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#expressionsWithDefaults.
    def exitExpressionsWithDefaults(self, ctx:SelectSQLParser.ExpressionsWithDefaultsContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#constants.
    def enterConstants(self, ctx:SelectSQLParser.ConstantsContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#constants.
    def exitConstants(self, ctx:SelectSQLParser.ConstantsContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#simpleStrings.
    def enterSimpleStrings(self, ctx:SelectSQLParser.SimpleStringsContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#simpleStrings.
    def exitSimpleStrings(self, ctx:SelectSQLParser.SimpleStringsContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#userVariables.
    def enterUserVariables(self, ctx:SelectSQLParser.UserVariablesContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#userVariables.
    def exitUserVariables(self, ctx:SelectSQLParser.UserVariablesContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#defaultValue.
    def enterDefaultValue(self, ctx:SelectSQLParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#defaultValue.
    def exitDefaultValue(self, ctx:SelectSQLParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#currentTimestamp.
    def enterCurrentTimestamp(self, ctx:SelectSQLParser.CurrentTimestampContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#currentTimestamp.
    def exitCurrentTimestamp(self, ctx:SelectSQLParser.CurrentTimestampContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#expressionOrDefault.
    def enterExpressionOrDefault(self, ctx:SelectSQLParser.ExpressionOrDefaultContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#expressionOrDefault.
    def exitExpressionOrDefault(self, ctx:SelectSQLParser.ExpressionOrDefaultContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#ifExists.
    def enterIfExists(self, ctx:SelectSQLParser.IfExistsContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#ifExists.
    def exitIfExists(self, ctx:SelectSQLParser.IfExistsContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#ifNotExists.
    def enterIfNotExists(self, ctx:SelectSQLParser.IfNotExistsContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#ifNotExists.
    def exitIfNotExists(self, ctx:SelectSQLParser.IfNotExistsContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#specificFunctionCall.
    def enterSpecificFunctionCall(self, ctx:SelectSQLParser.SpecificFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#specificFunctionCall.
    def exitSpecificFunctionCall(self, ctx:SelectSQLParser.SpecificFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#aggregateFunctionCall.
    def enterAggregateFunctionCall(self, ctx:SelectSQLParser.AggregateFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#aggregateFunctionCall.
    def exitAggregateFunctionCall(self, ctx:SelectSQLParser.AggregateFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#scalarFunctionCall.
    def enterScalarFunctionCall(self, ctx:SelectSQLParser.ScalarFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#scalarFunctionCall.
    def exitScalarFunctionCall(self, ctx:SelectSQLParser.ScalarFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#udfFunctionCall.
    def enterUdfFunctionCall(self, ctx:SelectSQLParser.UdfFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#udfFunctionCall.
    def exitUdfFunctionCall(self, ctx:SelectSQLParser.UdfFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#passwordFunctionCall.
    def enterPasswordFunctionCall(self, ctx:SelectSQLParser.PasswordFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#passwordFunctionCall.
    def exitPasswordFunctionCall(self, ctx:SelectSQLParser.PasswordFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#simpleFunctionCall.
    def enterSimpleFunctionCall(self, ctx:SelectSQLParser.SimpleFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#simpleFunctionCall.
    def exitSimpleFunctionCall(self, ctx:SelectSQLParser.SimpleFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#dataTypeFunctionCall.
    def enterDataTypeFunctionCall(self, ctx:SelectSQLParser.DataTypeFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#dataTypeFunctionCall.
    def exitDataTypeFunctionCall(self, ctx:SelectSQLParser.DataTypeFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#valuesFunctionCall.
    def enterValuesFunctionCall(self, ctx:SelectSQLParser.ValuesFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#valuesFunctionCall.
    def exitValuesFunctionCall(self, ctx:SelectSQLParser.ValuesFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#caseFunctionCall.
    def enterCaseFunctionCall(self, ctx:SelectSQLParser.CaseFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#caseFunctionCall.
    def exitCaseFunctionCall(self, ctx:SelectSQLParser.CaseFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#charFunctionCall.
    def enterCharFunctionCall(self, ctx:SelectSQLParser.CharFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#charFunctionCall.
    def exitCharFunctionCall(self, ctx:SelectSQLParser.CharFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#positionFunctionCall.
    def enterPositionFunctionCall(self, ctx:SelectSQLParser.PositionFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#positionFunctionCall.
    def exitPositionFunctionCall(self, ctx:SelectSQLParser.PositionFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#substrFunctionCall.
    def enterSubstrFunctionCall(self, ctx:SelectSQLParser.SubstrFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#substrFunctionCall.
    def exitSubstrFunctionCall(self, ctx:SelectSQLParser.SubstrFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#trimFunctionCall.
    def enterTrimFunctionCall(self, ctx:SelectSQLParser.TrimFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#trimFunctionCall.
    def exitTrimFunctionCall(self, ctx:SelectSQLParser.TrimFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#weightFunctionCall.
    def enterWeightFunctionCall(self, ctx:SelectSQLParser.WeightFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#weightFunctionCall.
    def exitWeightFunctionCall(self, ctx:SelectSQLParser.WeightFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#extractFunctionCall.
    def enterExtractFunctionCall(self, ctx:SelectSQLParser.ExtractFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#extractFunctionCall.
    def exitExtractFunctionCall(self, ctx:SelectSQLParser.ExtractFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#getFormatFunctionCall.
    def enterGetFormatFunctionCall(self, ctx:SelectSQLParser.GetFormatFunctionCallContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#getFormatFunctionCall.
    def exitGetFormatFunctionCall(self, ctx:SelectSQLParser.GetFormatFunctionCallContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#caseFuncAlternative.
    def enterCaseFuncAlternative(self, ctx:SelectSQLParser.CaseFuncAlternativeContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#caseFuncAlternative.
    def exitCaseFuncAlternative(self, ctx:SelectSQLParser.CaseFuncAlternativeContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#levelWeightList.
    def enterLevelWeightList(self, ctx:SelectSQLParser.LevelWeightListContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#levelWeightList.
    def exitLevelWeightList(self, ctx:SelectSQLParser.LevelWeightListContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#levelWeightRange.
    def enterLevelWeightRange(self, ctx:SelectSQLParser.LevelWeightRangeContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#levelWeightRange.
    def exitLevelWeightRange(self, ctx:SelectSQLParser.LevelWeightRangeContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#levelInWeightListElement.
    def enterLevelInWeightListElement(self, ctx:SelectSQLParser.LevelInWeightListElementContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#levelInWeightListElement.
    def exitLevelInWeightListElement(self, ctx:SelectSQLParser.LevelInWeightListElementContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#aggregateWindowedFunction.
    def enterAggregateWindowedFunction(self, ctx:SelectSQLParser.AggregateWindowedFunctionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#aggregateWindowedFunction.
    def exitAggregateWindowedFunction(self, ctx:SelectSQLParser.AggregateWindowedFunctionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#scalarFunctionName.
    def enterScalarFunctionName(self, ctx:SelectSQLParser.ScalarFunctionNameContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#scalarFunctionName.
    def exitScalarFunctionName(self, ctx:SelectSQLParser.ScalarFunctionNameContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#passwordFunctionClause.
    def enterPasswordFunctionClause(self, ctx:SelectSQLParser.PasswordFunctionClauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#passwordFunctionClause.
    def exitPasswordFunctionClause(self, ctx:SelectSQLParser.PasswordFunctionClauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#functionArgs.
    def enterFunctionArgs(self, ctx:SelectSQLParser.FunctionArgsContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#functionArgs.
    def exitFunctionArgs(self, ctx:SelectSQLParser.FunctionArgsContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#functionArg.
    def enterFunctionArg(self, ctx:SelectSQLParser.FunctionArgContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#functionArg.
    def exitFunctionArg(self, ctx:SelectSQLParser.FunctionArgContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#isExpression.
    def enterIsExpression(self, ctx:SelectSQLParser.IsExpressionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#isExpression.
    def exitIsExpression(self, ctx:SelectSQLParser.IsExpressionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#notExpression.
    def enterNotExpression(self, ctx:SelectSQLParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#notExpression.
    def exitNotExpression(self, ctx:SelectSQLParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#logicalExpression.
    def enterLogicalExpression(self, ctx:SelectSQLParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#logicalExpression.
    def exitLogicalExpression(self, ctx:SelectSQLParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#predicateExpression.
    def enterPredicateExpression(self, ctx:SelectSQLParser.PredicateExpressionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#predicateExpression.
    def exitPredicateExpression(self, ctx:SelectSQLParser.PredicateExpressionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#soundsLikePredicate.
    def enterSoundsLikePredicate(self, ctx:SelectSQLParser.SoundsLikePredicateContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#soundsLikePredicate.
    def exitSoundsLikePredicate(self, ctx:SelectSQLParser.SoundsLikePredicateContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#expressionAtomPredicate.
    def enterExpressionAtomPredicate(self, ctx:SelectSQLParser.ExpressionAtomPredicateContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#expressionAtomPredicate.
    def exitExpressionAtomPredicate(self, ctx:SelectSQLParser.ExpressionAtomPredicateContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#inPredicate.
    def enterInPredicate(self, ctx:SelectSQLParser.InPredicateContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#inPredicate.
    def exitInPredicate(self, ctx:SelectSQLParser.InPredicateContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#subqueryComparasionPredicate.
    def enterSubqueryComparasionPredicate(self, ctx:SelectSQLParser.SubqueryComparasionPredicateContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#subqueryComparasionPredicate.
    def exitSubqueryComparasionPredicate(self, ctx:SelectSQLParser.SubqueryComparasionPredicateContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#betweenPredicate.
    def enterBetweenPredicate(self, ctx:SelectSQLParser.BetweenPredicateContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#betweenPredicate.
    def exitBetweenPredicate(self, ctx:SelectSQLParser.BetweenPredicateContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#binaryComparasionPredicate.
    def enterBinaryComparasionPredicate(self, ctx:SelectSQLParser.BinaryComparasionPredicateContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#binaryComparasionPredicate.
    def exitBinaryComparasionPredicate(self, ctx:SelectSQLParser.BinaryComparasionPredicateContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#isNullPredicate.
    def enterIsNullPredicate(self, ctx:SelectSQLParser.IsNullPredicateContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#isNullPredicate.
    def exitIsNullPredicate(self, ctx:SelectSQLParser.IsNullPredicateContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#likePredicate.
    def enterLikePredicate(self, ctx:SelectSQLParser.LikePredicateContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#likePredicate.
    def exitLikePredicate(self, ctx:SelectSQLParser.LikePredicateContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#regexpPredicate.
    def enterRegexpPredicate(self, ctx:SelectSQLParser.RegexpPredicateContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#regexpPredicate.
    def exitRegexpPredicate(self, ctx:SelectSQLParser.RegexpPredicateContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#unaryExpressionAtom.
    def enterUnaryExpressionAtom(self, ctx:SelectSQLParser.UnaryExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#unaryExpressionAtom.
    def exitUnaryExpressionAtom(self, ctx:SelectSQLParser.UnaryExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#collateExpressionAtom.
    def enterCollateExpressionAtom(self, ctx:SelectSQLParser.CollateExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#collateExpressionAtom.
    def exitCollateExpressionAtom(self, ctx:SelectSQLParser.CollateExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#subqueryExpessionAtom.
    def enterSubqueryExpessionAtom(self, ctx:SelectSQLParser.SubqueryExpessionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#subqueryExpessionAtom.
    def exitSubqueryExpessionAtom(self, ctx:SelectSQLParser.SubqueryExpessionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#nestedExpressionAtom.
    def enterNestedExpressionAtom(self, ctx:SelectSQLParser.NestedExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#nestedExpressionAtom.
    def exitNestedExpressionAtom(self, ctx:SelectSQLParser.NestedExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#nestedRowExpressionAtom.
    def enterNestedRowExpressionAtom(self, ctx:SelectSQLParser.NestedRowExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#nestedRowExpressionAtom.
    def exitNestedRowExpressionAtom(self, ctx:SelectSQLParser.NestedRowExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#mathExpressionAtom.
    def enterMathExpressionAtom(self, ctx:SelectSQLParser.MathExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#mathExpressionAtom.
    def exitMathExpressionAtom(self, ctx:SelectSQLParser.MathExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#intervalExpressionAtom.
    def enterIntervalExpressionAtom(self, ctx:SelectSQLParser.IntervalExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#intervalExpressionAtom.
    def exitIntervalExpressionAtom(self, ctx:SelectSQLParser.IntervalExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#existsExpessionAtom.
    def enterExistsExpessionAtom(self, ctx:SelectSQLParser.ExistsExpessionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#existsExpessionAtom.
    def exitExistsExpessionAtom(self, ctx:SelectSQLParser.ExistsExpessionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#constantExpressionAtom.
    def enterConstantExpressionAtom(self, ctx:SelectSQLParser.ConstantExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#constantExpressionAtom.
    def exitConstantExpressionAtom(self, ctx:SelectSQLParser.ConstantExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#functionCallExpressionAtom.
    def enterFunctionCallExpressionAtom(self, ctx:SelectSQLParser.FunctionCallExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#functionCallExpressionAtom.
    def exitFunctionCallExpressionAtom(self, ctx:SelectSQLParser.FunctionCallExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#binaryExpressionAtom.
    def enterBinaryExpressionAtom(self, ctx:SelectSQLParser.BinaryExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#binaryExpressionAtom.
    def exitBinaryExpressionAtom(self, ctx:SelectSQLParser.BinaryExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#fullColumnNameExpressionAtom.
    def enterFullColumnNameExpressionAtom(self, ctx:SelectSQLParser.FullColumnNameExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#fullColumnNameExpressionAtom.
    def exitFullColumnNameExpressionAtom(self, ctx:SelectSQLParser.FullColumnNameExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#bitExpressionAtom.
    def enterBitExpressionAtom(self, ctx:SelectSQLParser.BitExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#bitExpressionAtom.
    def exitBitExpressionAtom(self, ctx:SelectSQLParser.BitExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#variableExpressionAtom.
    def enterVariableExpressionAtom(self, ctx:SelectSQLParser.VariableExpressionAtomContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#variableExpressionAtom.
    def exitVariableExpressionAtom(self, ctx:SelectSQLParser.VariableExpressionAtomContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#unaryOperator.
    def enterUnaryOperator(self, ctx:SelectSQLParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#unaryOperator.
    def exitUnaryOperator(self, ctx:SelectSQLParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:SelectSQLParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:SelectSQLParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#logicalOperator.
    def enterLogicalOperator(self, ctx:SelectSQLParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#logicalOperator.
    def exitLogicalOperator(self, ctx:SelectSQLParser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#bitOperator.
    def enterBitOperator(self, ctx:SelectSQLParser.BitOperatorContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#bitOperator.
    def exitBitOperator(self, ctx:SelectSQLParser.BitOperatorContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#mathOperator.
    def enterMathOperator(self, ctx:SelectSQLParser.MathOperatorContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#mathOperator.
    def exitMathOperator(self, ctx:SelectSQLParser.MathOperatorContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#charsetNameBase.
    def enterCharsetNameBase(self, ctx:SelectSQLParser.CharsetNameBaseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#charsetNameBase.
    def exitCharsetNameBase(self, ctx:SelectSQLParser.CharsetNameBaseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#transactionLevelBase.
    def enterTransactionLevelBase(self, ctx:SelectSQLParser.TransactionLevelBaseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#transactionLevelBase.
    def exitTransactionLevelBase(self, ctx:SelectSQLParser.TransactionLevelBaseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#privilegesBase.
    def enterPrivilegesBase(self, ctx:SelectSQLParser.PrivilegesBaseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#privilegesBase.
    def exitPrivilegesBase(self, ctx:SelectSQLParser.PrivilegesBaseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#intervalTypeBase.
    def enterIntervalTypeBase(self, ctx:SelectSQLParser.IntervalTypeBaseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#intervalTypeBase.
    def exitIntervalTypeBase(self, ctx:SelectSQLParser.IntervalTypeBaseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#dataTypeBase.
    def enterDataTypeBase(self, ctx:SelectSQLParser.DataTypeBaseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#dataTypeBase.
    def exitDataTypeBase(self, ctx:SelectSQLParser.DataTypeBaseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#keywordsCanBeId.
    def enterKeywordsCanBeId(self, ctx:SelectSQLParser.KeywordsCanBeIdContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#keywordsCanBeId.
    def exitKeywordsCanBeId(self, ctx:SelectSQLParser.KeywordsCanBeIdContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#functionNameBase.
    def enterFunctionNameBase(self, ctx:SelectSQLParser.FunctionNameBaseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#functionNameBase.
    def exitFunctionNameBase(self, ctx:SelectSQLParser.FunctionNameBaseContext):
        pass


