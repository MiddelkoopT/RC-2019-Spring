#!/bin/bash

if [ "$(./redis-client.sh set test 1)" != "OK" ] ; then
    echo "--- redist-client set failed"
    exit 1
fi

if [ "$(./redis-client.sh get test)" != '1' ] ; then
    echo "--- redis-client get failed"
    exit 1
fi
