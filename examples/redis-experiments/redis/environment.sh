if [ -f redis.env ] ; then
 . ./redis.env
 export REDIS_HOME REDIS_HOST REDIS_PORT REDISCLI_AUTH REDIS_JOB_ID
fi
