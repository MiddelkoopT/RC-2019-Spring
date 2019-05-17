#!/usr/bin/python3

import os
import redis
import json

print("redis.py")

r=redis.Redis(host=os.getenv('REDIS_HOST'),
              port=os.getenv('REDIS_PORT'),
              password=os.getenv('REDISCLI_AUTH'))
print(r.get('test'))

r.set('test',1)
print(r.get('test'))

d=json.load(open("test.json"))
r.set('test',json.dumps(d))

j=r.get('test').decode('utf-8')
print(j)
d=json.loads(j)
print(d)
