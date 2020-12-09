USER="root"
PASSWD="root"
TMP_DB_PATH=$4

EvoSQL_DIR="./evosql"
SCENARIO="SQLEquiv"
SCENARIO_DIR="${EvoSQL_DIR}/evaluation/scenarios/${SCENARIO}"

cd $(dirname $0)
mkdir -p $SCENARIO_DIR

### Copy schema.sql & queries.sql & table_order.sql ###
SCHEMA="${SCENARIO_DIR}/schema.sql"
QUERIES="${SCENARIO_DIR}/queries.sql"
cp $1 $SCHEMA
cp $2 $QUERIES
cp $3 $SCENARIO_DIR/table_order.sql


### Generate config.properties ###
PROP="${SCENARIO_DIR}/config.properties"
echo "url=jdbc:mysql://localhost:3306/?nullNamePatternMatchesAll=true&useSSL=false&serverTimezone=UTC" > $PROP
echo "database=evosql${SCENARIO}" >> $PROP
echo "physicaldatabase=databasetmp" >> $PROP
echo "schema=public" >> $PROP
echo "user=${USER}" >> $PROP
echo "pwd=${PASSWD}" >> $PROP



### Run EvoSQL ###
cd ${EvoSQL_DIR}/evaluation
java -cp "build/libs/evaluation-1.0.jar:/home/bhso/.m2/repository/mysql/mysql-connector-java/6.0.5/mysql-connector-java-6.0.5.jar:../ga/build/libs/ga-1.0.jar:/home/bhso/.m2/repository/com/github/jsqlparser/jsqlparser/0.9.6/jsqlparser-0.9.6.jar:/home/bhso/.m2/repository/org/apache/logging/log4j/log4j-api/2.6.2/log4j-api-2.6.2.jar:/home/bhso/.m2/repository/org/apache/logging/log4j/log4j-core/2.6.2/log4j-core-2.6.2.jar" nl/tudelft/serg/evosql/evaluation/query/Runner $SCENARIO
java -cp "build/libs/evaluation-1.0.jar:/home/bhso/.m2/repository/mysql/mysql-connector-java/6.0.5/mysql-connector-java-6.0.5.jar:../ga/build/libs/ga-1.0.jar:/home/bhso/.m2/repository/com/github/jsqlparser/jsqlparser/0.9.6/jsqlparser-0.9.6.jar:/home/bhso/.m2/repository/org/apache/logging/log4j/log4j-api/2.6.2/log4j-api-2.6.2.jar:/home/bhso/.m2/repository/org/apache/logging/log4j/log4j-core/2.6.2/log4j-core-2.6.2.jar" nl/tudelft/serg/evosql/evaluation/SerializeMySQLTableSchemas $SCENARIO

java -cp "build/libs/evaluation-1.0.jar:../ga/build/libs/ga-1.0.jar:../instrumented-hsqldb/build/libs/instrumented-hsqldb-1.0.jar:../lib/sqlrules.jar:/home/bhso/.m2/repository/org/mockito/mockito-all/2.0.2-beta/mockito-all-2.0.2-beta.jar:/home/bhso/.m2/repository/wsdl4j/wsdl4j/1.6.2/wsdl4j-1.6.2.jar:/home/bhso/.m2/repository/commons-discovery/commons-discovery/0.5/commons-discovery-0.5.jar:/home/bhso/.m2/repository/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.jar:/home/bhso/.m2/repository/org/apache/axis/axis/1.4/axis-1.4.jar:/home/bhso/.m2/repository/javax/xml/rpc/javax.xml.rpc-api/1.1.1/javax.xml.rpc-api-1.1.1.jar:/home/bhso/.m2/repository/org/hsqldb/hsqldb/2.3.4/hsqldb-2.3.4.jar:/home/bhso/.m2/repository/mysql/mysql-connector-java/6.0.5/mysql-connector-java-6.0.5.jar:build/libs/evaluation-1.0.jar:/home/bhso/.m2/repository/org/hibernate/common/hibernate-commons-annotations/5.0.1.Final/hibernate-commons-annotations-5.0.1.Final.jar:/home/bhso/.m2/repository/com/github/jsqlparser/jsqlparser/0.9.6/jsqlparser-0.9.6.jar:/home/bhso/.m2/repository/org/apache/logging/log4j/log4j-api/2.6.2/log4j-api-2.6.2.jar:/home/bhso/.m2/repository/org/apache/logging/log4j/log4j-core/2.6.2/log4j-core-2.6.2.jar:/home/bhso/.m2/repository/org/hibernate/hibernate-core/5.2.10.Final/hibernate-core-5.2.10.Final.jar" nl/tudelft/serg/evosql/evaluation/Runner $SCENARIO evosql


### Copy generated test data ###
cd ../..
rm -r $TMP_DB_PATH
mv $SCENARIO_DIR/results $TMP_DB_PATH
mkdir $SCENARIO_DIR/results