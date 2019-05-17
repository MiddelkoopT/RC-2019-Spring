#!/bin/bash

. ./environment.sh
python3 -m venv venv
. ./environment.sh
pip install --upgrade pip

pip install redis
pip install gitpython


