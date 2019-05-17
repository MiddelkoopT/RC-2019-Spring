#!/bin/bash

. ./envrionment.sh

## Python Virtual Env
pyvenv python
#python3 -m venv python ## python 3.6+

. python/bin/activate

pip install --upgrade pip
pip install gitpython

