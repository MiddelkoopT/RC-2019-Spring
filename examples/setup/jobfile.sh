#!/bin/bash

#SBATCH --partition hpc0
#SBATCH --mem=20G
#SBATCH --time=5:00

. ./environment.sh

echo === $(hostname) $(date)

## Default to config.json otherwise take the first argument (note the magic here)
srun python3 script.py ${1:-config.json}
srun Rscript script.R ${1:-config.json}

echo === $(hostname) $(date)
