#!/bin/bash

for i in redis python ; do
  cd $i ; source ./environment.sh ; cd ..
done

#echo $REDIS_HOME $REDIS_HOST
#which python3

