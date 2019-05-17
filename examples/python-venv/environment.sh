#!/bin/bash

module load python/python-3.5.2

if [ ! -d venv ] ; then
  python3 -m venv venv
fi

source venv/bin/activate
