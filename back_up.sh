#!/bin/bash
# file path is exit?
if [ ! -d "/mnt/sql_back_up" ]; then
  mount -t cifs -v -o username=f001,password=f3333 //192.168.0.11/bi/ /mnt/
fi


cur_time=`date +%Y_%m_%d`

# change user
su - postgres <<EOF 
/usr/pgsql-9.6/bin/pg_dump -Ft -b back_test > "/home/back_tmp/$cur_time.tar"
EOF

mv "/home/back_tmp/$cur_time.tar" "/mnt/sql_back_up/$cur_time.tar"

echo "All has done!"