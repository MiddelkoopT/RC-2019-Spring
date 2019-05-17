#!/bin/bash

module load miniconda3/miniconda3-4.3.30

if [ ! -d conda ] ; then
    conda create --yes --prefix ./conda python=3.7
fi

source activate ./conda 

