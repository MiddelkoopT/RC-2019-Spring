#!/bin/bash

. ./environment.sh

echo === $(hostname) $(date)

python3 example.py example.xlsx

echo === $(hostname) $(date)

