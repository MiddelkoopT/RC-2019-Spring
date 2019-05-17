#!/bin/bash

unset MODULEPATH
unset MODULESHOME

. spack/share/spack/setup-env.sh
. $(spack location -i lmod)/lmod/lmod/init/bash

