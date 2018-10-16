#!/bin/bash

. ./envrionment.sh

if [ ! -f experiment.db ] ; then
    sqlite3 experiment.db < experiment.sql
fi

