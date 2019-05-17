#!/usr/bin/python3

import os
import redis
import json


class Server:
    def __init__(self):
        self.db=redis.Redis(host=os.getenv('REDIS_HOST'),
                            port=os.getenv('REDIS_PORT'),
                            password=os.getenv('REDISCLI_AUTH'))
    
    def hsetjson(self,key,field,values):
        return self.db.hset(key,field,json.dumps(values))

    def hgetjson(self,key,field):
        return json.loads(self.db.hget(key,field).decode('utf-8'))

    def set(self,key,value):
        return self.db.set(key,value)

    def get(self,key):
        return self.db.put(key)

    def lpush(self,key,value):
        return self.db.lpush(key,value)

    def lpop(self,key):
        return self.db.lpush(key)

    def delete(self,key):
        return self.db.delete(key)


def tdd_test_server(tdd):
    # test round redis/json/python round trip
    s=Server()
    j='{ "one": 1, "two": 2, "three": [1,2,3]}'
    d=json.loads(j)

    tdd.true(s.hsetjson('_test',1,100))
    tdd.equals(s.hgetjson('_test',1),100)

    tdd.true(s.hsetjson('_test','2',d))   ## Write json
    tdd.equals(s.hgetjson('_test','2'),d) ## Read and compare JSON

    tdd.true(s.delete('_test'))   ## Remove test key


if __name__=='__main__':
    from tdd import Tdd
    tdd=Tdd()
    tdd_test_server(tdd)
