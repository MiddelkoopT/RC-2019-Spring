#!/bin/bash

## Install CBC
install -dv cbc
( cd cbc 
  wget -c 'https://bintray.com/coin-or/download/download_file?file_path=Cbc-2.10.0-linux-x86_64-gcc4.8.tgz' -O cbc.tar.gz
  if [ ! -d build ] ; then
    tar -xzf cbc.tar.gz
  fi
)

export COIN_INSTALL_DIR=$PWD/cbc/build


. ./environment.sh
python3 -m venv venv
. ./environment.sh
pip install --upgrade pip
pip install numpy
pip install --pre cylp

