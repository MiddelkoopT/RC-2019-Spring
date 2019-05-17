#!/usr/bin/python3

import os
import redis

db=redis.Redis(host=os.getenv('REDIS_HOST'),
               port=os.getenv('REDIS_PORT'),
               password=os.getenv('REDISCLI_AUTH'))

count=0

cursor=0
for a in db.scan_iter("arc:*"):
    count+=1

    d=int(db.get(a))
    if count%1000 == 0:
        print(count,a.decode('utf-8'),d)
