#!/bin/bash

rm -vf map.db
sqlite3 map.db < schema.sql
sqlite3 map.db < sample.sql


