#!/bin/bash

bash ./setup.sh

python3 export.py > export.json
python3 import.py < import.json

sqlite3 map.db .dump >dump.sql

md5sum -c files.md5

