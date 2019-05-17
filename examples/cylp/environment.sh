#!/bin/bash

module load python/python-3.5.2
if [ -d venv ] ; then
 . venv/bin/activate
fi

## CBC
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PWD/cbc/build/lib



