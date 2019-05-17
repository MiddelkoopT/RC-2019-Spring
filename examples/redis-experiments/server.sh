#!/bin/bash

cd redis
rm -f *.out
sbatch redis-server-jobfile.sh
