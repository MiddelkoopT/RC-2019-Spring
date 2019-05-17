#!/bin/bash

#SBATCH --mem=10G
#SBATCH --partition hpc0
#SBATCH --time 0-04:00:00

. ./environment.sh

REDIS_PASS=$(uuidgen)
REDIS_PORT=$((49152+$RANDOM/2))
REDIS_HOME=${PWD}

rm -f redis.conf ; touch redis.conf ; chmod 600 redis.conf
echo "port $REDIS_PORT" >> redis.conf
echo "requirepass $REDIS_PASS" >> redis.conf

echo "REDIS_HOME=$REDIS_HOME" > redis.env
echo "REDIS_HOST=$(hostname)" >> redis.env
echo "REDIS_PORT=$REDIS_PORT" >> redis.env
echo "REDISCLI_AUTH=$REDIS_PASS" >> redis.env
echo "REDIS_JOB_ID=$SLURM_JOB_ID" >> redis.env

${REDIS_HOME}/bin/redis-server redis.conf
