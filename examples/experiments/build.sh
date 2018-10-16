#!/bin/bash

. ./envrionment.sh

## Experiment DB
if [ ! -f experiment.db ] ; then
    sqlite3 experiment.db < experiment.sql
fi



