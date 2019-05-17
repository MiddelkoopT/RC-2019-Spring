#!/bin/bash

. ./environment.sh

install -dvp "${R_LIBS_USER}"

Rscript setup.R
