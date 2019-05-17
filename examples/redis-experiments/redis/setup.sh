#!/bin/bash

REDIS=redis-5.0.4
prefix=$PWD

install -dv build bin
( cd build
  wget -c http://download.redis.io/releases/${REDIS}.tar.gz
  tar -xzf ${REDIS}.tar.gz
  cd redis-5.0.4
  make
  make PREFIX=$prefix install
)

