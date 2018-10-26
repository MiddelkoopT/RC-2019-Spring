#!/bin/bash

. envrionment.sh

rm -f *.out

python3 experiment.py

sbatch jobfile.sh



