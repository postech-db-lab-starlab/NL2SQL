TIME=$(date +"%F_%T")
function echo_timestamp() {
    date +"%Y-%m-%d_%H:%M:%S"
}


# TODO: change all dbnames to files (of dbnames) in db2exfmt_results directory
dbname="$2"

#category="basic"
category="$3"

#system="syntaxSQLNet"
system="$1"

test_queries=$4
opt_level=$5
new_db_dump=$6

WORK_DIR=$(dirname $0)
cd $WORK_DIR
WORK_DIR=$(pwd)

mkdir -p ./queries
mkdir -p ./db2exfmt_results
#rm ./queries/*.tsv
#rm ./queries/*.sql

rw_dir="./db2exfmt_results/"
al_dir="./aliased_queries/"
cn_dir="./canonicalized_files/"
mkdir -p ${rw_dir}/${TIME}
mkdir -p ${al_dir}/${TIME}
mkdir -p ${cn_dir}/${TIME}
mkdir -p ./log/alias/
mkdir -p ./log/canon/
mkdir -p ./results/

# run python which bring queires to run db2exfmt
filename="./queries/${system}_${dbname}_queries_index.tsv"
sqlfilename="./queries/${system}_${dbname}_queries.sql"
python2 get_all_queries.py ${filename} ${dbname} ${category} $test_queries $system
python get_sql_only.py ${filename} ${sqlfilename} 5

dump="./queries/${TIME}"
mkdir $dump
cp ./queries/*.tsv $dump
cp ./queries/*.sql $dump
cp $0 get_all_queries.py get_sql_only.py $dump



sqlfilename="./queries/${system}_${dbname}_queries.sql"
rewrite_file="${rw_dir}/${system}_${dbname}_queries.sql.rewrite"
db2_dbname=${dbname//null/}
db2_dbname=${db2_dbname:0:8}
if [ "$db2_dbname" == "restaura" ]; then
  db2_dbname="RESTRNT"
#elif [ "$db2_dbname" == "wikitabl" ]; then
#  db2_dbname="WTQ"
fi
echo "rewrite using db2 $db2_dbname $sqlfilename $rewrite_file"
bash run_db2exfmt_api.sh $db2_dbname $sqlfilename $rewrite_file $opt_level $new_db_dump
cp -rp $rewrite_file ${rewrite_file}.${category}.opt${opt_level}

echo "Start to create rewritten queries of ${dbname} using DB2"
sqlfilename="./queries/${system}_${dbname}_queries.sql"
rewrite_file="${rw_dir}/${system}_${dbname}_queries.sql.rewrite"
aliased_file="${al_dir}/${system}_${dbname}_aliased_queries.sql"
canonicalized_file="${cn_dir}/${system}_${dbname}_canonicalized.sql"
log_file="log/alias/${TIME}__${system}_${dbname}_${category}.log"
python3.5 alias_db2exfmt_sql.py ${rewrite_file} ${aliased_file} ${sqlfilename} |& tee ${log_file}
fieldsfile="./db_schema/${dbname//null/}-fields.txt"
if [ ! -f $fieldsfile ]; then
  python2 db_schema/extract_fields.py ${dbname//null/} $fieldsfile
fi
echo ${aliased_file} | python3 canonicaliser_after_alias.py --nonjson --fields $fieldsfile --write ${canonicalized_file} --db2_rewritten --log > $log_file
echo "DONE: ${dbname}, DB2"

cp ${rw_dir}/*.sql.rewrite ${rw_dir}/${TIME}/
cp ${al_dir}/*_aliased_queries.sql ${al_dir}/${TIME}/
cp $0 alias_db2exfmt_sql.py ${al_dir}/${TIME}/



results_path="./results/"

mkdir -p ./log/update_qm_db2
log_file="./log/update_qm_db2/$(echo_timestamp)"

exists_result_files="./results/*.results"
topath="./results/handmade_correct/"
dump_dir="${topath}/${system}_$(echo_timestamp)"
mv ${exists_result_files} "./results/done/"

echo "Start string match of ${dbname} rewritten queries"
#fieldsfile="./db_schema/${dbname//null/}-fields.txt"
fieldsfile="./db_schema/${dbname}-fields.txt"
python2 string_match.py $system ${dbname} $fieldsfile > ${log_file} 2>&1
echo "DONE: ${dbname}, string_match"

cp ${cn_dir}*_canonicalized.sql ${cn_dir}/${TIME}/
cp $0 string_match.py canonicaliser_after_alias.py ${cn_dir}/${TIME}/



mkdir -p $dump_dir

result_file="${results_path}/${system}_${dbname}_${dbname}_${category}.results"
python2 create_accuracy_file.py $result_file $system $dbname $category

cp $0 create_accuracy_file.py $dump_dir
cp ${exists_result_files} $dump_dir

