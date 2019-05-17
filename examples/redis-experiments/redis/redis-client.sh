#!/bin/bash

. ./environment.sh

${REDIS_HOME}/bin/redis-cli -h ${REDIS_HOST} -p ${REDIS_PORT} "$@"

