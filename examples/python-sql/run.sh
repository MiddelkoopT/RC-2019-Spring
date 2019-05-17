#!/bin/bash


## Create database
rm -vf map.db
sqlite3 map.db < schema.sql
sqlite3 map.db < sample.sql
sqlite3 map.db .dump

## import data
srun python3 import.py < import.json

## dump
sqlite3 map.db .dump

## Export JSON
rm -v export.json
srun python3 export.py  > export.json
srun jq . export.json


