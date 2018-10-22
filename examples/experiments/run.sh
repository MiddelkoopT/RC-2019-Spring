#!/bin/bash

. envrionment.sh

python3 experiment.py

sqlite3 experiment.db .dump


