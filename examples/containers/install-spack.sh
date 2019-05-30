#!/bin/bash

#SBATCH --job-name=spack
#SBATCH --mem=20G
#SBATCH --time=1-0
#SBATCH --cpus-per-task=10

#SBATCH --partition=hpc0

## Build spack
git clone https://github.com/spack/spack.git
. spack/share/spack/setup-env.sh
spack install lmod

## Build packages
. ./spack.sh
spack install python@3.7.3 py-pip py-pkgconfig py-setuptools
