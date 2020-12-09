if [ $# -ne 4 -a $# -ne 5 ]; then
    echo "./run.sh [DB NAME] [INPUT FILENAME] [OUTPUT FILENAME] [OPT LEVEL]"
    echo "OR ./run.sh [DB NAME] [INPUT FILENAME] [OUTPUT FILENAME] [OPT LEVEL] [NEW DB2 DATABASE DUMP FILENAME]"
    exit 1
fi

dbname=$1
filename=$2
out_filename=$3
opt_level=$4
db_dump=$5
#out_filename="${filename}.rewrite"
tmp_write_dir="./db2exfmt_results/tmp/${dbname}"

if [ -f ${out_filename} ]; then
   rm ${out_filename}
fi

if [ -d ${tmp_write_dir} ]; then
    rm -rf ${tmp_write_dir}/*
fi
mkdir -p ${tmp_write_dir}

#db2 DROP DATABASE ${dbname}
dbname=`echo $dbname | tr '[:lower:]' '[:upper:]'`
echo "Database name = $dbname"
db2 connect to $dbname
connected=`db2 LIST ACTIVE DATABASES | grep ${dbname}`
if [[ $connected == *"Database name"*"= $dbname"* ]]; then
  echo "DB already exists"
else
  db2 CREATE DATABASE ${dbname}
  db2 connect to ${dbname}
  db2 -tvf ${db_dump}
  db2 "CALL SYSPROC.SYSINSTALLOBJECTS('EXPLAIN', 'C', CAST (NULL AS VARCHAR(128)), CAST (NULL AS VARCHAR(128)))"
fi
db2 connect reset

id=0
while read line ; do
   id=$(($id+1))
   infile="${tmp_write_dir}/${id}.sql.in"
   currentoutfile="${tmp_write_dir}/${id}.sql.out"
   echo "${line};" | sed -e 's/;.*;/;/g' > ${infile}

   db2 connect to ${dbname}
   #db2 set current query optimization 1
   #db2 set current query optimization 2
   #db2 set current query optimization 9
   db2 set current query optimization $opt_level
   db2 set current explain mode explain
   db2 -tvf ${infile}
   db2exfmt -1 -d ${dbname} -o ${currentoutfile} -no_map_char

   start_line=$(grep -nr 'Optimized Statement' ${currentoutfile} | awk -F ':' '{printf"%d", $1+2}')
   end_line=$(grep -nr 'Access Plan' ${currentoutfile} | grep ':Access Plan' | awk -F ':' '{printf"%d", $1-2}')

   all_lines=$(cat $currentoutfile | wc -l)
   lines_grep=$(echo "$start_line $end_line" | awk '{printf"%d", $2-$1+1}')
   remaining_lines=$(echo "$all_lines $lines_grep" | awk '{printf"%d", $1-$2+1}')
   data=$(head -n $end_line ${currentoutfile} | tail -$lines_grep)

   sqlfile="${tmp_write_dir}/${id}.sql"
   echo ${data} > ${sqlfile}
done < ${filename}

IFS=$'\n' length=(` wc -l $filename | awk '{print $1}'`)

for id in $(seq 1 $length); do
   sqlfile="${tmp_write_dir}/${id}.sql"
   files=$(cat $sqlfile)

   echo $files >> ${out_filename}
done
db2 connect reset


