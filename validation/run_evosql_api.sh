TIME=$(date +"%F_%T")
function echo_timestamp() {
    date +"%Y-%m-%d_%H:%M:%S"
}


system="$1"
dbname="$2"
category="$3"
test_queries=$4


WORK_DIR=$(dirname $0)
cd $WORK_DIR
WORK_DIR=$(pwd)

EVO_DIR="./evosql_files"
mkdir -p $EVO_DIR
mkdir -p ./log/evosql/

cd $WORK_DIR
echo "Start to create test dbname of ${dbname} using EvoSQL"
log_file="./log/evosql/${TIME}__${dbname}_${category}.log"

tmp=`cat $test_queries | grep -v "^[a-zA-Z]" | awk '{print$1}'`
target_indices=`echo $tmp | sed -e "s/ /,/g"`

TABLE_ORDER="${EVO_DIR}/${dbname}_table_order.tsv"
if [ ! -f $TABLE_ORDER ]; then
  TMP="${TABLE_ORDER}.tmp"
  mysql -sN -uroot -proot -e "show tables" ${dbname//-/} > $TMP
  i=0
  while read line; do
    echo -e "${line}\t${i}" | tr '[:lower:]' '[:upper:]' | sed -e 's/_/BQ/g' >> $TABLE_ORDER
    i=$((i+1))
  done < $TMP
  rm $TMP
fi
DUMPFILE="${EVO_DIR}/${dbname}_no_data_mysqldump.sql"
QUERIES="${EVO_DIR}/${dbname}_queries.sql"
remote="bhso@141.223.199.7"
REMOTE_HOME="/home/bhso/Benchmark_RA/EvoSQL_180801"
sql_columns=("Q.gold_sql_execute")
for sql_column in ${sql_columns[@]}; do
  SQL="SELECT DISTINCT Q.query_id,
                       ${sql_column}
  FROM query Q
    JOIN accuracy A ON Q.query_id=A.query_id
    JOIN experiment_info E ON E.experiment_id=A.experiment_id
    JOIN query_result R ON E.experiment_id=R.experiment_id AND Q.query_id=R.query_id
    JOIN query_split S ON Q.query_id=S.query_id
  WHERE S.split = 'test'
    AND S.category = E.category
    AND S.category = '${category}'
    AND E.test_data = '${dbname}'
    AND E.system = '${system}'
    AND Q.query_index IN (${target_indices})
    AND ${sql_column} NOT LIKE \"%:=%\"
  ORDER BY 2, 1"
  if [ ! -f $DUMPFILE ]; then
    mysqldump --no-data -uroot -proot ${dbname//-/} | tr '[:lower:]' '[:upper:]' | sed -e ':a' -e 'N' -e '$!ba'  -e 's/, *\n  UNIQUE KEY `[A-Z0-9]*` (`[A-Z0-9]*`)//g' > $DUMPFILE
    sed -i '/^$/d' $DUMPFILE
    sed -i '$ d' $DUMPFILE
    sed -i -e 's/`\([A-Z0-9]*\)_\([A-Z0-9_]*\)`/`\1BQ\2`/g' $DUMPFILE
    sed -i -e 's/`\([A-Z0-9]*\)_\([A-Z0-9_]*\)`/`\1BQ\2`/g' $DUMPFILE
    sed -i -e 's/`\([A-Z0-9]*\)_\([A-Z0-9_]*\)`/`\1BQ\2`/g' $DUMPFILE
    sed -i -e 's/`\([A-Z0-9]*\)_\([A-Z0-9_]*\)`/`\1BQ\2`/g' $DUMPFILE
    sed -i -e 's/`\([A-Z0-9]*\)_\([A-Z0-9_]*\)`/`\1BQ\2`/g' $DUMPFILE
    sed -i -e 's/`\([A-Z0-9]*\)_\([A-Z0-9_]*\)`/`\1BQ\2`/g' $DUMPFILE
    sed -i -e 's/`\([A-Z0-9]*\)_\([A-Z0-9_]*\)`/`\1BQ\2`/g' $DUMPFILE
    sed -i -e 's/`\([A-Z0-9]*\)_\([A-Z0-9_]*\)`/`\1BQ\2`/g' $DUMPFILE
    sed -i -e 's/`\([A-Z0-9]*\)_\([A-Z0-9_]*\)`/`\1BQ\2`/g' $DUMPFILE
    TMP=${DUMPFILE}.tmp
    cp $DUMPFILE $TMP
    python evosql_files/mysql_to_evosql.py $TMP $DUMPFILE
    rm $TMP
  fi

  mysql -e "${SQL}" -uroot -proot benchmark > $QUERIES
  #sed -i -e '1d' -e 's/; ;/;/g' -e 's/;\\n/;/g' -e 's/;/ ;/g' -e "s/'/\\\'/g" -e "s/\"/'/g" -e 's/\\n$//' $QUERIES
  sed -i -e '1d' -e 's/; ;/;/g' -e 's/;\\n/;/g' -e 's/;/ ;/g' -e "s/\"/'/g" -e 's/\\n$//' $QUERIES
  if [ "${dbname:0:8}" = "advising" ]; then
    sed -i -e 's/SELECT COUNT( \* ) [=><] 0 , [A-Z0-9]*ALIAS0\.[A-Z0-9]* /SELECT * /' $QUERIES
    sed -i -e 's/SELECT COUNT( \* ) [=><] 0 /SELECT * /' $QUERIES
  elif [ "${dbname:0:18}" = "wikitablequestions" ]; then
    sed -i -e 's/ ! = / != /g' $QUERIES
    sed -i -e 's/AS DECIMAL ( 10 , 6 ) )/AS DECIMAL )/g' $QUERIES
    sed -i -e 's/AS SIGNED )/AS INTEGER )/g' $QUERIES
    sed -i -e 's/LOWER (/UPPER (/g' $QUERIES
    sed -i -e "s/\([A-Za-z0-9']\)' '/\1\" \"/g" $QUERIES
  fi
  cat $QUERIES | tr '[:lower:]' '[:upper:]' | sed -e 's/_/BQ/g' > ${QUERIES}_tmp
  sed -i -e "s/\([A-Z]\)\'\([A-Z]\)/\1\2/g" ${QUERIES}_tmp
  mv ${QUERIES}_tmp $QUERIES

  scp $DUMPFILE ${remote}:${REMOTE_HOME}/files/
  scp $QUERIES ${remote}:${REMOTE_HOME}/files/
  scp $TABLE_ORDER ${remote}:${REMOTE_HOME}/files/
  echo "bash ${REMOTE_HOME}/run_EvoSQL_remote.sh ${REMOTE_HOME}/files/${dbname}_no_data_mysqldump.sql ${REMOTE_HOME}/files/${dbname}_queries.sql ${REMOTE_HOME}/files/${dbname}_table_order.tsv ${REMOTE_HOME}/files/${dbname}_${ADDITIONAL}result"
  ssh ${remote} "bash ${REMOTE_HOME}/run_EvoSQL_remote.sh ${REMOTE_HOME}/files/${dbname}_no_data_mysqldump.sql ${REMOTE_HOME}/files/${dbname}_queries.sql ${REMOTE_HOME}/files/${dbname}_table_order.tsv ${REMOTE_HOME}/files/${dbname}_${ADDITIONAL}result" > ${log_file}
  if [ -d ${EVO_DIR}/${dbname}_evosql_${ADDITIONAL}result ]; then
    rm -rf ${EVO_DIR}/${dbname}_evosql_${ADDITIONAL}result
  fi
  scp -r ${remote}:${REMOTE_HOME}/files/${dbname}_${ADDITIONAL}result ${EVO_DIR}/${dbname}_evosql_${ADDITIONAL}result

  SCHEMA_DUMP="${EVO_DIR}/${dbname}_evosql_${ADDITIONAL}result/testdata/schema.mysqldump"
  if [ "${dbname:0:8}" = "advising" ]; then
    cp ${EVO_DIR}/advising_schema_for_evosql.mysqldump $SCHEMA_DUMP
  else
    mysqldump --no-data -uroot -proot ${dbname//-/} | tr '[:lower:]' '[:upper:]' > $SCHEMA_DUMP
  fi

  for insert_query in ${EVO_DIR}/${dbname}_evosql_${ADDITIONAL}result/testdata/Q*/INSERTQUERY.sql; do
    sed -i -e 's/BQ/_/g' $insert_query
    if [ "${dbname:0:18}" = "wikitablequestions" ]; then
        python2 ${EVO_DIR}/correct_wtq_insert_query.py $insert_query
    fi
  done

  for gen_data in ${EVO_DIR}/${dbname}_evosql_${ADDITIONAL}result/testdata/Q*/*.tsv; do
    sed -i -e 's/BQ/_/g' $gen_data
    sed -i -e 's/\\\\/\\/g' $gen_data
    sed -i -e 's/\tnull\t/\t\\N\t/g' $gen_data
    rename 's/BQ/_/g' $gen_data
  done
done



cd ../../benchMyAdmin/python/

logdir=./logs/$(echo_timestamp)
mkdir -p ${logdir}
cp main.py ${logdir}/

logfilename=${system}_${dbname}_${category}_$(echo_timestamp)_1.out
TMPDATAPATH="${WORK_DIR}/evosql_files/${dbname}_evosql_result/testdata/"
echo "python2 main.py compute_accuracy_ex --system ${system} --training_data ${dbname} --test_data ${dbname} --category ${category} --tmp_data_path ${TMPDATAPATH}" |& tee ${logdir}/${logfilename}
python2 main.py compute_accuracy_ex --system ${system} --training_data ${dbname} --test_data ${dbname} --category ${category} --tmp_data_path ${TMPDATAPATH} |& tee ${logdir}/${logfilename}
echo "DONE: Execute on tmp dbname of ${dbname}"

