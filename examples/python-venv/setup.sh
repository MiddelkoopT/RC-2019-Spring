#!/bin/bash

## Remove old environment
rm -rf ./venv/
. ./environment.sh

pip install --upgrade pip
pip install openpyxl
