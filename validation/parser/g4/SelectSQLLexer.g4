/*
MySQL (Positive Technologies) grammar
The MIT License (MIT).
Copyright (c) 2015-2017, Ivan Kochurkin (kvanttt@gmail.com), Positive Technologies.
Copyright (c) 2017, Ivan Khudyashev (IHudyashov@ptsecurity.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/

lexer grammar SelectSQLLexer;

channels { MYSQLCOMMENT, ERRORCHANNEL }

// SKIP

SPACE:                               [ \t\r\n]+    -> channel(HIDDEN);
SPEC_MYSQL_COMMENT:                  '/*!' .+? '*/' -> channel(MYSQLCOMMENT);
COMMENT_INPUT:                       '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT:                        (
                                       ('-- ' | '#') ~[\r\n]* ('\r'? '\n' | EOF) 
                                       | '--' ('\r'? '\n' | EOF) 
                                     ) -> channel(HIDDEN);


// Keywords
// Common Keywords

ADD:                                 A D D;
ALL:                                 A L L;
ALTER:                               'ALTER';
ANALYZE:                             'ANALYZE';
AND:                                 A N D;
AS:                                  A S;
ASC:                                 A S C;
BEFORE:                              B E F O R E;
BETWEEN:                             B E T W E E N;
BOTH:                                B O T H;
BY:                                  B Y;
CALL:                                'CALL';
CASCADE:                             'CASCADE';
CASE:                                C A S E;
CAST:                                C A S T;
CHANGE:                              'CHANGE';
CHARACTER:                           'CHARACTER';
CHECK:                               'CHECK';
COLLATE:                             'COLLATE';
COLUMN:                              'COLUMN';
CONDITION:                           'CONDITION';
CONSTRAINT:                          'CONSTRAINT';
CONTINUE:                            'CONTINUE';
CONVERT:                             'CONVERT';
CREATE:                              'CREATE';
CROSS:                               C R O S S;
CURRENT_USER:                        'CURRENT_USER';
CURSOR:                              'CURSOR';
DATABASE:                            'DATABASE';
DATABASES:                           'DATABASES';
DECLARE:                             'DECLARE';
DEFAULT:                             'DEFAULT';
DELAYED:                             'DELAYED';
DELETE:                              'DELETE';
DESC:                                D E S C;
DESCRIBE:                            'DESCRIBE';
DETERMINISTIC:                       'DETERMINISTIC';
DISTINCT:                            D I S T I N C T;
DISTINCTROW:                         'DISTINCTROW';
DROP:                                'DROP';
EACH:                                E A C H;
ELSE:                                E L S E;
ELSEIF:                              E L S E I F;
ENCLOSED:                            'ENCLOSED';
ESCAPED:                             'ESCAPED';
EXISTS:                              E X I S T S;
EXIT:                                'EXIT';
EXPLAIN:                             'EXPLAIN';
FALSE:                               F A L S E;
FETCH:                               'FETCH';
FOR:                                 F O R;
FORCE:                               'FORCE';
FOREIGN:                             'FOREIGN';
FROM:                                F R O M;
FULLTEXT:                            'FULLTEXT';
GRANT:                               'GRANT';
GROUP:                               G R O U P;
HAVING:                              H A V I N G;
HIGH_PRIORITY:                       'HIGH_PRIORITY';
IF:                                  I F;
IGNORE:                              'IGNORE';
IN:                                  I N;
INDEX:                               I N D E X;
INFILE:                              'INFILE';
INNER:                               I N N E R;
INOUT:                               'INOUT';
INSERT:                              'INSERT';
INTERVAL:                            'INTERVAL';
INTO:                                I N T O;
IS:                                  I S;
ITERATE:                             'ITERATE';
JOIN:                                J O I N;
KEY:                                 'KEY';
KEYS:                                'KEYS';
KILL:                                'KILL';
LEADING:                             'LEADING';
LEAVE:                               'LEAVE';
LEFT:                                L E F T;
LIKE:                                L I K E;
LIMIT:                               L I M I T;
LINEAR:                              'LINEAR';
LINES:                               'LINES';
LOAD:                                'LOAD';
LOCK:                                'LOCK';
LOOP:                                L O O P;
LOW_PRIORITY:                        'LOW_PRIORITY';
MASTER_BIND:                         'MASTER_BIND';
MASTER_SSL_VERIFY_SERVER_CERT:       'MASTER_SSL_VERIFY_SERVER_CERT';
MATCH:                               M A T C H;
MAXVALUE:                            M A X V A L U E;
MODIFIES:                            'MODIFIES';
NATURAL:                             N A T U R A L;
NOT:                                 N O T;
NO_WRITE_TO_BINLOG:                  'NO_WRITE_TO_BINLOG';
NULL_LITERAL:                        N U L L;
ON:                                  O N;
OPTIMIZE:                            'OPTIMIZE';
OPTION:                              'OPTION';
OPTIONALLY:                          'OPTIONALLY';
OR:                                  O R;
ORDER:                               O R D E R;
OUT:                                 O U T;
OUTER:                               O U T E R;
OUTFILE:                             'OUTFILE';
PARTITION:                           'PARTITION';
PRIMARY:                             'PRIMARY';
PROCEDURE:                           'PROCEDURE';
PURGE:                               'PURGE';
RANGE:                               'RANGE';
READ:                                'READ';
READS:                               'READS';
REFERENCES:                          'REFERENCES';
REGEXP:                              R E G E X P;
RELEASE:                             'RELEASE';
RENAME:                              'RENAME';
REPEAT:                              'REPEAT';
REPLACE:                             R E P L A C E;
REQUIRE:                             'REQUIRE';
RESTRICT:                            'RESTRICT';
RETURN:                              'RETURN';
REVOKE:                              'REVOKE';
RIGHT:                               R I G H T;
RLIKE:                               'RLIKE';
SCHEMA:                              S C H E M A;
SCHEMAS:                             S C H E M A S;
SELECT:                              S E L E C T;
SET:                                 S E T;
SEPARATOR:                           S E P A R A T O R;
SHOW:                                S H O W;
SPATIAL:                             S P A T I A L;
SQL:                                 S Q L;
SQLEXCEPTION:                        'SQLEXCEPTION';
SQLSTATE:                            'SQLSTATE';
SQLWARNING:                          'SQLWARNING';
SQL_BIG_RESULT:                      'SQL_BIG_RESULT';
SQL_CALC_FOUND_ROWS:                 'SQL_CALC_FOUND_ROWS';
SQL_SMALL_RESULT:                    'SQL_SMALL_RESULT';
SSL:                                 'SSL';
STARTING:                            'STARTING';
STRAIGHT_JOIN:                       'STRAIGHT_JOIN';
TABLE:                               T A B L E;
TERMINATED:                          'TERMINATED';
THEN:                                T H E N;
TO:                                  T O;
TRAILING:                            T R A I L I N G;
TRIGGER:                             'TRIGGER';
TRUE:                                T R U E;
UNDO:                                'UNDO';
UNION:                               U N I O N;
UNIQUE:                              'UNIQUE';
UNLOCK:                              'UNLOCK';
UNSIGNED:                            U N S I G N E D;
UPDATE:                              'UPDATE';
USAGE:                               'USAGE';
USE:                                 'USE';
USING:                               U S I N G;
VALUES:                              V A L U E S;
WHEN:                                W H E N;
WHERE:                               W H E R E;
WHILE:                               W H I L E;
WITH:                                W I T H;
WRITE:                               'WRITE';
XOR:                                 X O R;
ZEROFILL:                            Z E R O F I L L;


// DATA TYPE Keywords

TINYINT:                             T I N Y I N T;
SMALLINT:                            S M A L L I N T;
MEDIUMINT:                           M E D I U M I N T;
INT:                                 I N T;
INTEGER:                             I N T E G E R;
BIGINT:                              B I G I N T;
REAL:                                R E A L;
DOUBLE:                              D O U B L E;
FLOAT:                               F L O A T;
DECIMAL:                             D E C I M A L;
NUMERIC:                             N U M E R I C;
DATE:                                D A T E;
TIME:                                T I M E;
TIMESTAMP:                           T I M E S T A M P;
DATETIME:                            D A T E T I M E;
YEAR:                                Y E A R;
CHAR:                                C H A R;
VARCHAR:                             V A R C H A R;
BINARY:                              B I N A R Y;
VARBINARY:                           V A R B I N A R Y;
TINYBLOB:                            T I N Y B L O B;
BLOB:                                B L O B;
MEDIUMBLOB:                          M E D I U M B L O B;
LONGBLOB:                            L O N G B L O B;
TINYTEXT:                            T I N Y T E X T;
TEXT:                                T E X T;
MEDIUMTEXT:                          M E D I U M T E X T;
LONGTEXT:                            L O N G T E X T;
ENUM:                                E N U M;


// Interval type Keywords

YEAR_MONTH:                          'YEAR_MONTH';
DAY_HOUR:                            'DAY_HOUR';
DAY_MINUTE:                          'DAY_MINUTE';
DAY_SECOND:                          'DAY_SECOND';
HOUR_MINUTE:                         'HOUR_MINUTE';
HOUR_SECOND:                         'HOUR_SECOND';
MINUTE_SECOND:                       'MINUTE_SECOND'; 
SECOND_MICROSECOND:                  'SECOND_MICROSECOND';
MINUTE_MICROSECOND:                  'MINUTE_MICROSECOND';
HOUR_MICROSECOND:                    'HOUR_MICROSECOND';
DAY_MICROSECOND:                     'DAY_MICROSECOND';


// Group function Keywords

AVG:                                 A V G;
BIT_AND:                             B I T '_' A N D;
BIT_OR:                              B I T '_' O R;
BIT_XOR:                             B I T '_' X O R;
COUNT:                               C O U N T;
GROUP_CONCAT:                        G R O U P '_' C O N C A T;
MAX:                                 M A X;
MIN:                                 M I N;
STD:                                 S T D;
STDDEV:                              S T D D E V;
STDDEV_POP:                          S T D D E V '_' P O P;
STDDEV_SAMP:                         S T D D E V '_' S A M P;
SUM:                                 S U M;
VAR_POP:                             'VAR_POP';
VAR_SAMP:                            'VAR_SAMP';
VARIANCE:                            'VARIANCE';


// Common function Keywords

CURRENT_DATE:                        C U R R E N T '_' D A T E;
CURRENT_TIME:                        C U R R E N T '_' T I M E;
CURRENT_TIMESTAMP:                   C U R R E N T '_' T I M E S T A M P;
LOCALTIME:                           'LOCALTIME';
CURDATE:                             C U R D A T E;
CURTIME:                             'CURTIME';
DATE_ADD:                            'DATE_ADD';
DATE_SUB:                            'DATE_SUB';
EXTRACT:                             'EXTRACT';
LOCALTIMESTAMP:                      'LOCALTIMESTAMP';
NOW:                                 N O W;
POSITION:                            'POSITION';
SUBSTR:                              S U B S T R;
SUBSTRING:                           S U B S T R I N G;
SYSDATE:                             'SYSDATE';
TRIM:                                T R I M;
UTC_DATE:                            'UTC_DATE';
UTC_TIME:                            'UTC_TIME';
UTC_TIMESTAMP:                       'UTC_TIMESTAMP';



// Keywords, but can be ID
// Common Keywords, but can be ID

ACCOUNT:                             'ACCOUNT';
ACTION:                              'ACTION';
AFTER:                               A F T E R;
AGGREGATE:                           'AGGREGATE';
ALGORITHM:                           'ALGORITHM';
ANY:                                 A N Y;
AT:                                  A T;
AUTHORS:                             'AUTHORS';
AUTOCOMMIT:                          'AUTOCOMMIT';
AUTOEXTEND_SIZE:                     'AUTOEXTEND_SIZE';
AUTO_INCREMENT:                      'AUTO_INCREMENT';
AVG_ROW_LENGTH:                      'AVG_ROW_LENGTH';
BEGIN:                               B E G I N;
BINLOG:                              'BINLOG';
BIT:                                 'BIT';
BLOCK:                               'BLOCK';
BOOL:                                B O O L;
BOOLEAN:                             B O O L E A N;
BTREE:                               'BTREE';
CACHE:                               'CACHE';
CASCADED:                            C A S C A D E D;
CHAIN:                               'CHAIN';
CHANGED:                             'CHANGED';
CHANNEL:                             'CHANNEL';
CHECKSUM:                            C H E C K S U M;
CIPHER:                              'CIPHER';
CLIENT:                              'CLIENT';
CLOSE:                               'CLOSE';
COALESCE:                            C O A L E S C E;
CODE:                                'CODE';
COLUMNS:                             'COLUMNS';
COLUMN_FORMAT:                       'COLUMN_FORMAT';
COMMENT:                             C O M M E N T;
COMMIT:                              'COMMIT';
COMPACT:                             'COMPACT';
COMPLETION:                          'COMPLETION';
COMPRESSED:                          'COMPRESSED';
COMPRESSION:                         'COMPRESSION';
CONCURRENT:                          'CONCURRENT';
CONNECTION:                          'CONNECTION';
CONSISTENT:                          'CONSISTENT';
CONTAINS:                            C O N T A I N S;
CONTEXT:                             'CONTEXT';
CONTRIBUTORS:                        'CONTRIBUTORS';
COPY:                                'COPY';
CPU:                                 'CPU';
DATA:                                'DATA';
DATAFILE:                            'DATAFILE';
DEALLOCATE:                          'DEALLOCATE';
DEFAULT_AUTH:                        'DEFAULT_AUTH';
DEFINER:                             'DEFINER';
DELAY_KEY_WRITE:                     'DELAY_KEY_WRITE';
DES_KEY_FILE:                        'DES_KEY_FILE';
DIRECTORY:                           'DIRECTORY';
DISABLE:                             'DISABLE';
DISCARD:                             'DISCARD';
DISK:                                'DISK';
DO:                                  D O;
DUMPFILE:                            'DUMPFILE';
DUPLICATE:                           'DUPLICATE';
DYNAMIC:                             'DYNAMIC';
ENABLE:                              'ENABLE';
ENCRYPTION:                          'ENCRYPTION';
END:                                 E N D;
ENDS:                                'ENDS';
ENGINE:                              'ENGINE';
ENGINES:                             'ENGINES';
ERROR:                               'ERROR';
ERRORS:                              'ERRORS';
ESCAPE:                              'ESCAPE';
EVEN:                                'EVEN';
EVENT:                               'EVENT';
EVENTS:                              'EVENTS';
EVERY:                               'EVERY';
EXCHANGE:                            'EXCHANGE';
EXCLUSIVE:                           'EXCLUSIVE';
EXPIRE:                              'EXPIRE';
EXPORT:                              'EXPORT';
EXTENDED:                            'EXTENDED';
EXTENT_SIZE:                         'EXTENT_SIZE';
FAST:                                'FAST';
FAULTS:                              'FAULTS';
FIELDS:                              'FIELDS';
FILE_BLOCK_SIZE:                     'FILE_BLOCK_SIZE';
FILTER:                              F I L T E R;
FIRST:                               'FIRST';
FIXED:                               'FIXED';
FLUSH:                               'FLUSH';
FOLLOWS:                             'FOLLOWS';
FOUND:                               'FOUND';
FULL:                                F U L L;
FUNCTION:                            F U N C T I O N;
GENERAL:                             'GENERAL';
GLOBAL:                              'GLOBAL';
GRANTS:                              'GRANTS';
GROUP_REPLICATION:                   'GROUP_REPLICATION';
HANDLER:                             'HANDLER';
HASH:                                H A S H;
HELP:                                'HELP';
HOST:                                'HOST';
HOSTS:                               'HOSTS';
IDENTIFIED:                          'IDENTIFIED';
IGNORE_SERVER_IDS:                   'IGNORE_SERVER_IDS';
IMPORT:                              'IMPORT';
INDEXES:                             I N D E X E S;
INITIAL_SIZE:                        'INITIAL_SIZE';
INPLACE:                             'INPLACE';
INSERT_METHOD:                       'INSERT_METHOD';
INSTALL:                             'INSTALL';
INSTANCE:                            'INSTANCE';
INVOKER:                             'INVOKER';
IO:                                  'IO';
IO_THREAD:                           'IO_THREAD';
IPC:                                 'IPC';
ISOLATION:                           'ISOLATION';
ISSUER:                              'ISSUER';
JSON:                                'JSON';
KEY_BLOCK_SIZE:                      'KEY_BLOCK_SIZE';
LANGUAGE:                            'LANGUAGE';
LAST:                                'LAST';
LEAVES:                              'LEAVES';
LESS:                                L E S S;
LEVEL:                               'LEVEL';
LIST:                                'LIST';
LOCAL:                               'LOCAL';
LOGFILE:                             'LOGFILE';
LOGS:                                'LOGS';
MASTER:                              'MASTER';
MASTER_AUTO_POSITION:                'MASTER_AUTO_POSITION';
MASTER_CONNECT_RETRY:                'MASTER_CONNECT_RETRY';
MASTER_DELAY:                        'MASTER_DELAY';
MASTER_HEARTBEAT_PERIOD:             'MASTER_HEARTBEAT_PERIOD';
MASTER_HOST:                         'MASTER_HOST';
MASTER_LOG_FILE:                     'MASTER_LOG_FILE';
MASTER_LOG_POS:                      'MASTER_LOG_POS';
MASTER_PASSWORD:                     'MASTER_PASSWORD';
MASTER_PORT:                         'MASTER_PORT';
MASTER_RETRY_COUNT:                  'MASTER_RETRY_COUNT';
MASTER_SSL:                          'MASTER_SSL';
MASTER_SSL_CA:                       'MASTER_SSL_CA';
MASTER_SSL_CAPATH:                   'MASTER_SSL_CAPATH';
MASTER_SSL_CERT:                     'MASTER_SSL_CERT';
MASTER_SSL_CIPHER:                   'MASTER_SSL_CIPHER';
MASTER_SSL_CRL:                      'MASTER_SSL_CRL';
MASTER_SSL_CRLPATH:                  'MASTER_SSL_CRLPATH';
MASTER_SSL_KEY:                      'MASTER_SSL_KEY';
MASTER_TLS_VERSION:                  'MASTER_TLS_VERSION';
MASTER_USER:                         'MASTER_USER';
MAX_CONNECTIONS_PER_HOUR:            'MAX_CONNECTIONS_PER_HOUR';
MAX_QUERIES_PER_HOUR:                'MAX_QUERIES_PER_HOUR';
MAX_ROWS:                            'MAX_ROWS';
MAX_SIZE:                            'MAX_SIZE';
MAX_UPDATES_PER_HOUR:                'MAX_UPDATES_PER_HOUR';
MAX_USER_CONNECTIONS:                'MAX_USER_CONNECTIONS';
MEDIUM:                              'MEDIUM';
MERGE:                               'MERGE';
MID:                                 'MID';
MIGRATE:                             'MIGRATE';
MIN_ROWS:                            'MIN_ROWS';
MODE:                                'MODE';
MODIFY:                              'MODIFY';
MUTEX:                               'MUTEX';
MYSQL:                               'MYSQL';
NAME:                                'NAME';
NAMES:                               'NAMES';
NCHAR:                               'NCHAR';
NEVER:                               'NEVER';
NEXT:                                N E X T;
NO:                                  N O;
NODEGROUP:                           'NODEGROUP';
NONE:                                N O N E;
OFFLINE:                             'OFFLINE';
OFFSET:                              O F F S E T;
OJ:                                  'OJ';
OLD_PASSWORD:                        'OLD_PASSWORD';
ONE:                                 O N E;
ONLINE:                              'ONLINE';
ONLY:                                O N L Y;
OPEN:                                'OPEN';
OPTIMIZER_COSTS:                     'OPTIMIZER_COSTS';
OPTIONS:                             'OPTIONS';
OWNER:                               'OWNER';
PACK_KEYS:                           'PACK_KEYS';
PAGE:                                'PAGE';
PARSER:                              'PARSER';
PARTIAL:                             'PARTIAL';
PARTITIONING:                        'PARTITIONING';
PARTITIONS:                          'PARTITIONS';
PASSWORD:                            'PASSWORD';
PHASE:                               'PHASE';
PLUGIN:                              'PLUGIN';
PLUGIN_DIR:                          'PLUGIN_DIR';
PLUGINS:                             'PLUGINS';
PORT:                                'PORT';
PRECEDES:                            'PRECEDES';
PREPARE:                             'PREPARE';
PRESERVE:                            'PRESERVE';
PREV:                                'PREV';
PROCESSLIST:                         'PROCESSLIST';
PROFILE:                             'PROFILE';
PROFILES:                            'PROFILES';
PROXY:                               'PROXY';
QUERY:                               'QUERY';
QUICK:                               'QUICK';
REBUILD:                             'REBUILD';
RECOVER:                             'RECOVER';
REDO_BUFFER_SIZE:                    'REDO_BUFFER_SIZE';
REDUNDANT:                           'REDUNDANT';
RELAY:                               'RELAY';
RELAY_LOG_FILE:                      'RELAY_LOG_FILE';
RELAY_LOG_POS:                       'RELAY_LOG_POS';
RELAYLOG:                            'RELAYLOG';
REMOVE:                              'REMOVE';
REORGANIZE:                          'REORGANIZE';
REPAIR:                              'REPAIR';
REPLICATE_DO_DB:                     'REPLICATE_DO_DB';
REPLICATE_DO_TABLE:                  'REPLICATE_DO_TABLE';
REPLICATE_IGNORE_DB:                 'REPLICATE_IGNORE_DB';
REPLICATE_IGNORE_TABLE:              'REPLICATE_IGNORE_TABLE';
REPLICATE_REWRITE_DB:                'REPLICATE_REWRITE_DB';
REPLICATE_WILD_DO_TABLE:             'REPLICATE_WILD_DO_TABLE';
REPLICATE_WILD_IGNORE_TABLE:         'REPLICATE_WILD_IGNORE_TABLE';
REPLICATION:                         'REPLICATION';
RESET:                               'RESET';
RESUME:                              'RESUME';
RETURNS:                             'RETURNS';
ROLLBACK:                            'ROLLBACK';
ROLLUP:                              'ROLLUP';
ROTATE:                              'ROTATE';
ROW:                                 'ROW';
ROWS:                                'ROWS';
ROW_FORMAT:                          'ROW_FORMAT';
SAVEPOINT:                           'SAVEPOINT';
SCHEDULE:                            'SCHEDULE';
SECURITY:                            'SECURITY';
SERVER:                              'SERVER';
SESSION:                             'SESSION';
SHARE:                               'SHARE';
SHARED:                              'SHARED';
SIGNED:                              S I G N E D;
SIMPLE:                              'SIMPLE';
SLAVE:                               'SLAVE';
SLOW:                                'SLOW';
SNAPSHOT:                            'SNAPSHOT';
SOCKET:                              'SOCKET';
SOME:                                'SOME';
SONAME:                              'SONAME';
SOUNDS:                              'SOUNDS';
SOURCE:                              'SOURCE';
SQL_AFTER_GTIDS:                     'SQL_AFTER_GTIDS';
SQL_AFTER_MTS_GAPS:                  'SQL_AFTER_MTS_GAPS';
SQL_BEFORE_GTIDS:                    'SQL_BEFORE_GTIDS';
SQL_BUFFER_RESULT:                   'SQL_BUFFER_RESULT';
SQL_CACHE:                           'SQL_CACHE';
SQL_NO_CACHE:                        'SQL_NO_CACHE';
SQL_THREAD:                          'SQL_THREAD';
START:                               'START';
STARTS:                              'STARTS';
STATS_AUTO_RECALC:                   'STATS_AUTO_RECALC';
STATS_PERSISTENT:                    'STATS_PERSISTENT';
STATS_SAMPLE_PAGES:                  'STATS_SAMPLE_PAGES';
STATUS:                              'STATUS';
STOP:                                'STOP';
STORAGE:                             'STORAGE';
STRING:                              'STRING';
SUBJECT:                             'SUBJECT';
SUBPARTITION:                        'SUBPARTITION';
SUBPARTITIONS:                       'SUBPARTITIONS';
SUSPEND:                             'SUSPEND';
SWAPS:                               'SWAPS';
SWITCHES:                            'SWITCHES';
TABLESPACE:                          'TABLESPACE';
TEMPORARY:                           'TEMPORARY';
TEMPTABLE:                           'TEMPTABLE';
THAN:                                'THAN';
TRADITIONAL:                         'TRADITIONAL';
TRANSACTION:                         'TRANSACTION';
TRIGGERS:                            'TRIGGERS';
TRUNCATE:                            'TRUNCATE';
UNDEFINED:                           'UNDEFINED';
UNDOFILE:                            'UNDOFILE';
UNDO_BUFFER_SIZE:                    'UNDO_BUFFER_SIZE';
UNINSTALL:                           'UNINSTALL';
UNKNOWN:                             'UNKNOWN';
UNTIL:                               'UNTIL';
UPGRADE:                             'UPGRADE';
USER:                                'USER';
USE_FRM:                             'USE_FRM';
USER_RESOURCES:                      'USER_RESOURCES';
VALIDATION:                          'VALIDATION';
VALUE:                               'VALUE';
VARIABLES:                           'VARIABLES';
VIEW:                                'VIEW';
WAIT:                                'WAIT';
WARNINGS:                            'WARNINGS';
WITHOUT:                             'WITHOUT';
WORK:                                'WORK';
WRAPPER:                             'WRAPPER';
X509:                                'X509';
XA:                                  'XA';
XML:                                 'XML';


// Date format Keywords

EUR:                                 'EUR';
USA:                                 'USA';
JIS:                                 'JIS';
ISO:                                 'ISO';
INTERNAL:                            'INTERNAL';


// Interval type Keywords

QUARTER:                             'QUARTER';
MONTH:                               'MONTH';
DAY:                                 'DAY';
HOUR:                                'HOUR';
MINUTE:                              'MINUTE';
WEEK:                                'WEEK';
SECOND:                              'SECOND';
MICROSECOND:                         'MICROSECOND';


// PRIVILEGES

TABLES:                              'TABLES';
ROUTINE:                             'ROUTINE';
EXECUTE:                             'EXECUTE';
FILE:                                'FILE';
PROCESS:                             'PROCESS';
RELOAD:                              'RELOAD';
SHUTDOWN:                            'SHUTDOWN';
SUPER:                               'SUPER';
PRIVILEGES:                          'PRIVILEGES';


// Charsets

ARMSCII8:                            'ARMSCII8';
ASCII:                               'ASCII';
BIG5:                                'BIG5';
CP1250:                              'CP1250';
CP1251:                              'CP1251';
CP1256:                              'CP1256';
CP1257:                              'CP1257';
CP850:                               'CP850';
CP852:                               'CP852';
CP866:                               'CP866';
CP932:                               'CP932';
DEC8:                                'DEC8';
EUCJPMS:                             'EUCJPMS';
EUCKR:                               'EUCKR';
GB2312:                              'GB2312';
GBK:                                 'GBK';
GEOSTD8:                             'GEOSTD8';
GREEK:                               'GREEK';
HEBREW:                              'HEBREW';
HP8:                                 'HP8';
KEYBCS2:                             'KEYBCS2';
KOI8R:                               'KOI8R';
KOI8U:                               'KOI8U';
LATIN1:                              'LATIN1';
LATIN2:                              'LATIN2';
LATIN5:                              'LATIN5';
LATIN7:                              'LATIN7';
MACCE:                               'MACCE';
MACROMAN:                            'MACROMAN';
SJIS:                                'SJIS';
SWE7:                                'SWE7';
TIS620:                              'TIS620';
UCS2:                                'UCS2';
UJIS:                                'UJIS';
UTF16:                               'UTF16';
UTF16LE:                             'UTF16LE';
UTF32:                               'UTF32';
UTF8:                                'UTF8';
UTF8MB3:                             'UTF8MB3';
UTF8MB4:                             'UTF8MB4';


// DB Engines

ARCHIVE:                             'ARCHIVE';
BLACKHOLE:                           'BLACKHOLE';
CSV:                                 'CSV';
FEDERATED:                           'FEDERATED';
INNODB:                              'INNODB';
MEMORY:                              'MEMORY';
MRG_MYISAM:                          'MRG_MYISAM';
MYISAM:                              'MYISAM';
NDB:                                 'NDB';
NDBCLUSTER:                          'NDBCLUSTER';
PERFOMANCE_SCHEMA:                   'PERFOMANCE_SCHEMA';


// Transaction Levels

REPEATABLE:                          'REPEATABLE';
COMMITTED:                           'COMMITTED';
UNCOMMITTED:                         'UNCOMMITTED';
SERIALIZABLE:                        'SERIALIZABLE';


// Spatial data types

GEOMETRYCOLLECTION:                  'GEOMETRYCOLLECTION';
LINESTRING:                          'LINESTRING';
MULTILINESTRING:                     'MULTILINESTRING';
MULTIPOINT:                          'MULTIPOINT';
MULTIPOLYGON:                        'MULTIPOLYGON';
POINT:                               'POINT';
POLYGON:                             'POLYGON';


// Common function names

ABS:                                 A B S;
ACOS:                                'ACOS';
ADDDATE:                             A D D D A T E;
ADDTIME:                             A D D T I M E;
AES_DECRYPT:                         'AES_DECRYPT';
AES_ENCRYPT:                         'AES_ENCRYPT';
AREA:                                'AREA';
ASBINARY:                            A S B I N A R Y;
ASIN:                                A S I N;
ASTEXT:                              A S T E X T;
ASWKB:                               A S W K B;
ASWKT:                               A S W K T;
ASYMMETRIC_DECRYPT:                  'ASYMMETRIC_DECRYPT';
ASYMMETRIC_DERIVE:                   'ASYMMETRIC_DERIVE';
ASYMMETRIC_ENCRYPT:                  'ASYMMETRIC_ENCRYPT';
ASYMMETRIC_SIGN:                     'ASYMMETRIC_SIGN';
ASYMMETRIC_VERIFY:                   'ASYMMETRIC_VERIFY';
ATAN:                                'ATAN';
ATAN2:                               'ATAN2';
BENCHMARK:                           'BENCHMARK';
BIN:                                 B I N;
BIT_COUNT:                           B I T '_' C O U N T;
BIT_LENGTH:                          B I T '_' L E N G T H;
BUFFER:                              'BUFFER';
CEIL:                                C E I L;
CEILING:                             C E I L I N G;
CENTROID:                            C E N T R O I D;
CHARACTER_LENGTH:                    C H A R A C T E R '_' L E N G T H;
CHARSET:                             C H A R S E T;
CHAR_LENGTH:                         C H A R '_' L E N G T H;
COERCIBILITY:                        'COERCIBILITY';
COLLATION:                           'COLLATION';
COMPRESS:                            'COMPRESS';
CONCAT:                              C O N C A T;
CONCAT_WS:                           C O N C A T '_' W S;
CONNECTION_ID:                       'CONNECTION_ID';
CONV:                                'CONV';
CONVERT_TZ:                          'CONVERT_TZ';
COS:                                 C O S;
COT:                                 C O T;
CRC32:                               'CRC32';
CREATE_ASYMMETRIC_PRIV_KEY:          'CREATE_ASYMMETRIC_PRIV_KEY';
CREATE_ASYMMETRIC_PUB_KEY:           'CREATE_ASYMMETRIC_PUB_KEY';
CREATE_DH_PARAMETERS:                'CREATE_DH_PARAMETERS';
CREATE_DIGEST:                       'CREATE_DIGEST';
CROSSES:                             'CROSSES';
DATEDIFF:                            D A T E D I F F;
DATE_FORMAT:                         D A T E '_' F O R M A T;
DAYNAME:                             D A Y N A M E;
DAYOFMONTH:                          D A Y O F M O N T H;
DAYOFWEEK:                           D A Y O F W E E K;
DAYOFYEAR:                           D A Y O F Y E A R;
DECODE:                              D E C O D E;
DEGREES:                             'DEGREES';
DES_DECRYPT:                         'DES_DECRYPT';
DES_ENCRYPT:                         'DES_ENCRYPT';
DIMENSION:                           'DIMENSION';
DISJOINT:                            'DISJOINT';
ELT:                                 E L T;
ENCODE:                              E N C O D E;
ENCRYPT:                             E N C R Y P T;
ENDPOINT:                            'ENDPOINT';
ENVELOPE:                            'ENVELOPE';
EQUALS:                              E Q U A L S;
EXP:                                 E X P;
EXPORT_SET:                          'EXPORT_SET';
EXTERIORRING:                        'EXTERIORRING';
EXTRACTVALUE:                        'EXTRACTVALUE';
FIELD:                               'FIELD';
FIND_IN_SET:                         F I N D '_' I N '_' S E T;
FLOOR:                               F L O O R;
FORMAT:                              F O R M A T;
FOUND_ROWS:                          'FOUND_ROWS';
FROM_BASE64:                         'FROM_BASE64';
FROM_DAYS:                           'FROM_DAYS';
FROM_UNIXTIME:                       'FROM_UNIXTIME';
GEOMCOLLFROMTEXT:                    'GEOMCOLLFROMTEXT';
GEOMCOLLFROMWKB:                     'GEOMCOLLFROMWKB';
GEOMETRYCOLLECTIONFROMTEXT:          'GEOMETRYCOLLECTIONFROMTEXT';
GEOMETRYCOLLECTIONFROMWKB:           'GEOMETRYCOLLECTIONFROMWKB';
GEOMETRYFROMTEXT:                    'GEOMETRYFROMTEXT';
GEOMETRYFROMWKB:                     'GEOMETRYFROMWKB';
GEOMETRYN:                           'GEOMETRYN';
GEOMETRYTYPE:                        'GEOMETRYTYPE';
GEOMFROMTEXT:                        'GEOMFROMTEXT';
GEOMFROMWKB:                         'GEOMFROMWKB';
GET_FORMAT:                          'GET_FORMAT';
GET_LOCK:                            'GET_LOCK';
GLENGTH:                             'GLENGTH';
GREATEST:                            'GREATEST';
GTID_SUBSET:                         'GTID_SUBSET';
GTID_SUBTRACT:                       'GTID_SUBTRACT';
HEX:                                 H E X;
IFNULL:                              I F N U L L;
INET6_ATON:                          'INET6_ATON';
INET6_NTOA:                          'INET6_NTOA';
INET_ATON:                           'INET_ATON';
INET_NTOA:                           'INET_NTOA';
INSTR:                               I N S T R;
INTERIORRINGN:                       'INTERIORRINGN';
INTERSECTS:                          'INTERSECTS';
ISCLOSED:                            I S C L O S E D;
ISEMPTY:                             I S E M P T Y;
ISNULL:                              I S N U L L;
ISSIMPLE:                            I S S I M P L E;
IS_FREE_LOCK:                        'IS_FREE_LOCK';
IS_IPV4:                             'IS_IPV4';
IS_IPV4_COMPAT:                      'IS_IPV4_COMPAT';
IS_IPV4_MAPPED:                      'IS_IPV4_MAPPED';
IS_IPV6:                             'IS_IPV6';
IS_USED_LOCK:                        'IS_USED_LOCK';
LAST_INSERT_ID:                      'LAST_INSERT_ID';
LCASE:                               L C A S E;
LEAST:                               L E A S T;
LENGTH:                              L E N G T H;
LINEFROMTEXT:                        'LINEFROMTEXT';
LINEFROMWKB:                         'LINEFROMWKB';
LINESTRINGFROMTEXT:                  'LINESTRINGFROMTEXT';
LINESTRINGFROMWKB:                   'LINESTRINGFROMWKB';
LN:                                  'LN';
LOAD_FILE:                           'LOAD_FILE';
LOCATE:                              'LOCATE';
LOG:                                 'LOG';
LOG10:                               'LOG10';
LOG2:                                'LOG2';
LOWER:                               L O W E R;
LPAD:                                'LPAD';
LTRIM:                               L T R I M;
MAKEDATE:                            M A K E D A T E;
MAKETIME:                            M A K E T I M E;
MAKE_SET:                            'MAKE_SET';
MASTER_POS_WAIT:                     'MASTER_POS_WAIT';
MBRCONTAINS:                         'MBRCONTAINS';
MBRDISJOINT:                         'MBRDISJOINT';
MBREQUAL:                            'MBREQUAL';
MBRINTERSECTS:                       'MBRINTERSECTS';
MBROVERLAPS:                         'MBROVERLAPS';
MBRTOUCHES:                          'MBRTOUCHES';
MBRWITHIN:                           'MBRWITHIN';
MD5:                                 'MD5';
MLINEFROMTEXT:                       'MLINEFROMTEXT';
MLINEFROMWKB:                        'MLINEFROMWKB';
MONTHNAME:                           'MONTHNAME';
MPOINTFROMTEXT:                      'MPOINTFROMTEXT';
MPOINTFROMWKB:                       'MPOINTFROMWKB';
MPOLYFROMTEXT:                       'MPOLYFROMTEXT';
MPOLYFROMWKB:                        'MPOLYFROMWKB';
MULTILINESTRINGFROMTEXT:             'MULTILINESTRINGFROMTEXT';
MULTILINESTRINGFROMWKB:              'MULTILINESTRINGFROMWKB';
MULTIPOINTFROMTEXT:                  'MULTIPOINTFROMTEXT';
MULTIPOINTFROMWKB:                   'MULTIPOINTFROMWKB';
MULTIPOLYGONFROMTEXT:                'MULTIPOLYGONFROMTEXT';
MULTIPOLYGONFROMWKB:                 'MULTIPOLYGONFROMWKB';
NAME_CONST:                          'NAME_CONST';
NULLIF:                              N U L L I F;
NUMGEOMETRIES:                       'NUMGEOMETRIES';
NUMINTERIORRINGS:                    'NUMINTERIORRINGS';
NUMPOINTS:                           'NUMPOINTS';
OCT:                                 'OCT';
OCTET_LENGTH:                        'OCTET_LENGTH';
ORD:                                 'ORD';
OVERLAPS:                            'OVERLAPS';
PERIOD_ADD:                          'PERIOD_ADD';
PERIOD_DIFF:                         'PERIOD_DIFF';
PI:                                  'PI';
POINTFROMTEXT:                       'POINTFROMTEXT';
POINTFROMWKB:                        'POINTFROMWKB';
POINTN:                              'POINTN';
POLYFROMTEXT:                        'POLYFROMTEXT';
POLYFROMWKB:                         'POLYFROMWKB';
POLYGONFROMTEXT:                     'POLYGONFROMTEXT';
POLYGONFROMWKB:                      'POLYGONFROMWKB';
POW:                                 'POW';
POWER:                               'POWER';
QUOTE:                               'QUOTE';
RADIANS:                             'RADIANS';
RAND:                                R A N D;
RANDOM_BYTES:                        'RANDOM_BYTES';
RELEASE_LOCK:                        'RELEASE_LOCK';
REVERSE:                             R E V E R S E;
ROUND:                               R O U N D;
ROW_COUNT:                           'ROW_COUNT';
RPAD:                                'RPAD';
RTRIM:                               R T R I M;
SEC_TO_TIME:                         'SEC_TO_TIME';
SESSION_USER:                        'SESSION_USER';
SHA:                                 'SHA';
SHA1:                                'SHA1';
SHA2:                                'SHA2';
SIGN:                                'SIGN';
SIN:                                 'SIN';
SLEEP:                               'SLEEP';
SOUNDEX:                             'SOUNDEX';
SQL_THREAD_WAIT_AFTER_GTIDS:         'SQL_THREAD_WAIT_AFTER_GTIDS';
SQRT:                                'SQRT';
SRID:                                'SRID';
STARTPOINT:                          'STARTPOINT';
STRCMP:                              S T R C M P;
STR_TO_DATE:                         S T R '_' T O '_' D A T E;
ST_AREA:                             'ST_AREA';
ST_ASBINARY:                         'ST_ASBINARY';
ST_ASTEXT:                           'ST_ASTEXT';
ST_ASWKB:                            'ST_ASWKB';
ST_ASWKT:                            'ST_ASWKT';
ST_BUFFER:                           'ST_BUFFER';
ST_CENTROID:                         'ST_CENTROID';
ST_CONTAINS:                         'ST_CONTAINS';
ST_CROSSES:                          'ST_CROSSES';
ST_DIFFERENCE:                       'ST_DIFFERENCE';
ST_DIMENSION:                        'ST_DIMENSION';
ST_DISJOINT:                         'ST_DISJOINT';
ST_DISTANCE:                         'ST_DISTANCE';
ST_ENDPOINT:                         'ST_ENDPOINT';
ST_ENVELOPE:                         'ST_ENVELOPE';
ST_EQUALS:                           'ST_EQUALS';
ST_EXTERIORRING:                     'ST_EXTERIORRING';
ST_GEOMCOLLFROMTEXT:                 'ST_GEOMCOLLFROMTEXT';
ST_GEOMCOLLFROMTXT:                  'ST_GEOMCOLLFROMTXT';
ST_GEOMCOLLFROMWKB:                  'ST_GEOMCOLLFROMWKB';
ST_GEOMETRYCOLLECTIONFROMTEXT:       'ST_GEOMETRYCOLLECTIONFROMTEXT';
ST_GEOMETRYCOLLECTIONFROMWKB:        'ST_GEOMETRYCOLLECTIONFROMWKB';
ST_GEOMETRYFROMTEXT:                 'ST_GEOMETRYFROMTEXT';
ST_GEOMETRYFROMWKB:                  'ST_GEOMETRYFROMWKB';
ST_GEOMETRYN:                        'ST_GEOMETRYN';
ST_GEOMETRYTYPE:                     'ST_GEOMETRYTYPE';
ST_GEOMFROMTEXT:                     'ST_GEOMFROMTEXT';
ST_GEOMFROMWKB:                      'ST_GEOMFROMWKB';
ST_INTERIORRINGN:                    'ST_INTERIORRINGN';
ST_INTERSECTION:                     'ST_INTERSECTION';
ST_INTERSECTS:                       'ST_INTERSECTS';
ST_ISCLOSED:                         'ST_ISCLOSED';
ST_ISEMPTY:                          'ST_ISEMPTY';
ST_ISSIMPLE:                         'ST_ISSIMPLE';
ST_LINEFROMTEXT:                     'ST_LINEFROMTEXT';
ST_LINEFROMWKB:                      'ST_LINEFROMWKB';
ST_LINESTRINGFROMTEXT:               'ST_LINESTRINGFROMTEXT';
ST_LINESTRINGFROMWKB:                'ST_LINESTRINGFROMWKB';
ST_NUMGEOMETRIES:                    'ST_NUMGEOMETRIES';
ST_NUMINTERIORRING:                  'ST_NUMINTERIORRING';
ST_NUMINTERIORRINGS:                 'ST_NUMINTERIORRINGS';
ST_NUMPOINTS:                        'ST_NUMPOINTS';
ST_OVERLAPS:                         'ST_OVERLAPS';
ST_POINTFROMTEXT:                    'ST_POINTFROMTEXT';
ST_POINTFROMWKB:                     'ST_POINTFROMWKB';
ST_POINTN:                           'ST_POINTN';
ST_POLYFROMTEXT:                     'ST_POLYFROMTEXT';
ST_POLYFROMWKB:                      'ST_POLYFROMWKB';
ST_POLYGONFROMTEXT:                  'ST_POLYGONFROMTEXT';
ST_POLYGONFROMWKB:                   'ST_POLYGONFROMWKB';
ST_SRID:                             'ST_SRID';
ST_STARTPOINT:                       'ST_STARTPOINT';
ST_SYMDIFFERENCE:                    'ST_SYMDIFFERENCE';
ST_TOUCHES:                          'ST_TOUCHES';
ST_UNION:                            'ST_UNION';
ST_WITHIN:                           'ST_WITHIN';
ST_X:                                'ST_X';
ST_Y:                                'ST_Y';
SUBDATE:                             S U B D A T E;
SUBSTRING_INDEX:                     S U B S T R I N G '_' I N D E X;
SUBTIME:                             S U B T I M E;
SYSTEM_USER:                         'SYSTEM_USER';
TAN:                                 'TAN';
TIMEDIFF:                            T I M E D I F F;
TIMESTAMPADD:                        'TIMESTAMPADD';
TIMESTAMPDIFF:                       'TIMESTAMPDIFF';
TIME_FORMAT:                         'TIME_FORMAT';
TIME_TO_SEC:                         'TIME_TO_SEC';
TOUCHES:                             'TOUCHES';
TO_BASE64:                           'TO_BASE64';
TO_DAYS:                             'TO_DAYS';
TO_SECONDS:                          'TO_SECONDS';
UCASE:                               U C A S E;
UNCOMPRESS:                          'UNCOMPRESS';
UNCOMPRESSED_LENGTH:                 'UNCOMPRESSED_LENGTH';
UNHEX:                               'UNHEX';
UNIX_TIMESTAMP:                      'UNIX_TIMESTAMP';
UPDATEXML:                           'UPDATEXML';
UPPER:                               U P P E R;
UUID:                                'UUID';
UUID_SHORT:                          'UUID_SHORT';
VALIDATE_PASSWORD_STRENGTH:          'VALIDATE_PASSWORD_STRENGTH';
VERSION:                             'VERSION';
WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS:   'WAIT_UNTIL_SQL_THREAD_AFTER_GTIDS';
WEEKDAY:                             W E E K D A Y;
WEEKOFYEAR:                          W E E K O F Y E A R;
WEIGHT_STRING:                       'WEIGHT_STRING';
WITHIN:                              W I T H I N;
YEARWEEK:                            Y E A R W E E K;
Y_FUNCTION:                          'Y';
X_FUNCTION:                          'X';



// Operators
// Operators. Assigns

VAR_ASSIGN:                          ':=';
PLUS_ASSIGN:                         '+=';
MINUS_ASSIGN:                        '-=';
MULT_ASSIGN:                         '*=';
DIV_ASSIGN:                          '/=';
MOD_ASSIGN:                          '%=';
AND_ASSIGN:                          '&=';
XOR_ASSIGN:                          '^=';
OR_ASSIGN:                           '|=';


// Operators. Arithmetics

STAR:                                '*';
DIVIDE:                              '/';
MODULE:                              '%';
PLUS:                                '+';
MINUSMINUS:                          '--';
MINUS:                               '-';
DIV:                                 'DIV';
MOD:                                 'MOD';


// Operators. Comparation

EQUAL_SYMBOL:                        '=';
GREATER_SYMBOL:                      '>';
LESS_SYMBOL:                         '<';
EXCLAMATION_SYMBOL:                  '!';


// Operators. Bit

BIT_NOT_OP:                          '~';
BIT_OR_OP:                           '|';
BIT_AND_OP:                          '&';
BIT_XOR_OP:                          '^';


// Constructors symbols

DOT:                                 '.';
LR_BRACKET:                          '(';
RR_BRACKET:                          ')';
COMMA:                               ',';
SEMI:                                ';';
AT_SIGN:                             '@';
ZERO_DECIMAL:                        '0';
ONE_DECIMAL:                         '1';
TWO_DECIMAL:                         '2';
SINGLE_QUOTE_SYMB:                   '\'';
DOUBLE_QUOTE_SYMB:                   '"';
REVERSE_QUOTE_SYMB:                  '`';
COLON_SYMB:                          ':';



// Charsets

CHARSET_REVERSE_QOUTE_STRING:        '`' CHARSET_NAME '`';



// File's sizes


FILESIZE_LITERAL:                    DEC_DIGIT+ ( K | M | G | T );



// Literal Primitives


START_NATIONAL_STRING_LITERAL:       'N' SQUOTA_STRING;
STRING_LITERAL:                      DQUOTA_STRING | SQUOTA_STRING;
DECIMAL_LITERAL:                     DEC_DIGIT+;
HEXADECIMAL_LITERAL:                 'X' '\'' (HEX_DIGIT HEX_DIGIT)+ '\''
                                     | '0X' HEX_DIGIT+;

REAL_LITERAL:                        (DEC_DIGIT+)? '.' DEC_DIGIT+
                                     | DEC_DIGIT+ '.' EXPONENT_NUM_PART
                                     | (DEC_DIGIT+)? '.' (DEC_DIGIT+ EXPONENT_NUM_PART)
                                     | DEC_DIGIT+ EXPONENT_NUM_PART;
NULL_SPEC_LITERAL:                   '\\' 'N';
BIT_STRING:                          BIT_STRING_L;
STRING_CHARSET_NAME:                 '_' CHARSET_NAME;




// Hack for dotID
// Prevent recognize string:         .123somelatin AS ((.123), FLOAT_LITERAL), ((somelatin), ID)
//  it must recoginze:               .123somelatin AS ((.), DOT), (123somelatin, ID)

DOT_ID:                              '.' ID_LITERAL;



// Identifiers

ID:                                  ID_LITERAL;
// DOUBLE_QUOTE_ID:                  '"' ~'"'+ '"';
REVERSE_QUOTE_ID:                    '`' ~'`'+ '`';
STRING_USER_NAME:                    (
                                       SQUOTA_STRING | DQUOTA_STRING 
                                       | BQUOTA_STRING | ID_LITERAL
                                     ) '@' 
                                     (
                                       SQUOTA_STRING | DQUOTA_STRING 
                                       | BQUOTA_STRING | ID_LITERAL
                                     );
LOCAL_ID:                            '@'
                                (
                                  [A-Za-z0-9._$]+ 
                                  | SQUOTA_STRING
                                  | DQUOTA_STRING
                                  | BQUOTA_STRING
                                );
GLOBAL_ID:                           '@' '@' 
                                (
                                  [A-Za-z0-9._$]+ 
                                  | BQUOTA_STRING
                                );


// Fragments for Literal primitives

fragment CHARSET_NAME:               ARMSCII8 | ASCII | BIG5 | BINARY | CP1250 
                                     | CP1251 | CP1256 | CP1257 | CP850 
                                     | CP852 | CP866 | CP932 | DEC8 | EUCJPMS 
                                     | EUCKR | GB2312 | GBK | GEOSTD8 | GREEK 
                                     | HEBREW | HP8 | KEYBCS2 | KOI8R | KOI8U 
                                     | LATIN1 | LATIN2 | LATIN5 | LATIN7 
                                     | MACCE | MACROMAN | SJIS | SWE7 | TIS620 
                                     | UCS2 | UJIS | UTF16 | UTF16LE | UTF32 
                                     | UTF8 | UTF8MB4;

fragment EXPONENT_NUM_PART:          'E' '-'? DEC_DIGIT+;
fragment ID_LITERAL:                 [A-Za-z_$0-9]*?[A-Za-z_$]+?[A-Za-z_$0-9]*;
fragment DQUOTA_STRING:              '"' ( '\\'. | '""' | ~('"'| '\\') )* '"';
fragment SQUOTA_STRING:              '\'' ('\\'. | '\'\'' | ~('\'' | '\\'))* '\'';
fragment BQUOTA_STRING:              '`' ( '\\'. | '``' | ~('`'|'\\'))* '`';
fragment HEX_DIGIT:                  [0-9A-Fa-f];
fragment DEC_DIGIT:                  [0-9];
fragment BIT_STRING_L:               'B' '\'' [01]+ '\'';


fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];


// Last tokens must generate Errors

ERROR_RECONGNIGION:                  .    -> channel(ERRORCHANNEL);
