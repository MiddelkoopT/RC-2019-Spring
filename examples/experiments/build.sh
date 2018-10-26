#!/bin/bash

. ./envrionment.sh

## Experiment DB
rm -v experiment.db
if [ ! -f experiment.db ] ; then
    sqlite3 experiment.db < experiment.sql
fi



