#!/bin/bash

#SBATCH -N 1
#SBATCH -n 4

echo '### SLURM' $(hostname) ${SLURM_JOB_ID}  $(date) 
module load gurobi/gurobi-8.1.0
module list

echo "+++ gurobi"
srun gurobi.sh ./gurobi-simple.py
