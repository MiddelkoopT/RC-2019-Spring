#!/usr/bin/python3

import os
import sys
import redis
import re

db=redis.Redis(host=os.getenv('REDIS_HOST'),
               port=os.getenv('REDIS_PORT'),
               password=os.getenv('REDISCLI_AUTH'))

a=re.compile('a (\d+) (\d+) (\d+)')

count=0
for l in sys.stdin:
    l=l[:-1]
    r=a.match(l)
    
    if r is None:
        continue
    count+=1

    n1,n2,d=r.groups()
    d=int(d)
    #print(n1,n2,d)
    db.set("arc:%s:%s" % (n1,n2),d)
    db.sadd("node:%s:out" % (n1,),n2)
    db.sadd("node:%s:in" % (n2,),n1)
    if count%1000 == 0:
        print(count)
