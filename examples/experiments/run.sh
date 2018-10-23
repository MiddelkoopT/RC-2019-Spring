#!/bin/bash

. envrionment.sh

rm -f *.out

python3 experiment.py

sqlite3 experiment.db .dump

sbatch jobfile.sh



