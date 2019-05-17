#!/bin/bash

## Based on http://docs.rnet.missouri.edu/Software/anaconda

rm -rf ./conda/
. ./environment.sh

conda install --yes pandas
conda install --yes matplotlib

