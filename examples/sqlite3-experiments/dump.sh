#!/bin/bash

sqlite3 experiment.db .dump

cat *.out

