#!/bin/bash

#SBATCH -J Experiment
#SBATCH -p hpc0
##SBATCH -N1 -n1 -c1
#SBATCH --time=00:01:00
#SBATCH --mem=1G

. ./envrionment.sh

srun python3 experiment.py 


