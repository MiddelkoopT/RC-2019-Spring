#!/usr/bin/python3

import json
from git import Repo

import server


db=server.Server()

config=json.load(open('manage/config.json'))
git=Repo('../../.git')

## Setup world
world=config['world']
print("=== Generate World",world,git.head.commit,git.is_dirty())
db.hsetjson('world', world, 
           { 
               'config': config, 
               'commit-id': str(git.head.commit), 
               'dirty':git.is_dirty()
           })

## Remove old world data
db.delete("world%d:input" % (world,))
db.delete("world%d:output" % (world,))
db.delete("world%d:metadata" % (world,))
db.delete("world%d:queue" % (world,))
db.delete("world%d:running" % (world,))
db.delete("world%d:done" % (world,))

# world:experiment:test:run:iteration
experiments=config['experiments']
tests=config['tests']
runs=config['runs']

run=0
for e in range(0,experiments):
    for t in range(0,tests):
        for r in range(0,runs):
            run+=1
            instance="world%d:experiment%d:test%d:run%d" % (world,e,t,r)
            db.hsetjson("world%d:input" % (world,),instance,[e,t,r,run])
            db.lpush("world%d:queue" % (world,),instance)

## redis/redis-client.sh KEYS '*'
## redis/redis-client.sh HGET world 1
## redis/redis-client.sh LRANGE world1:queue 0 -1
## redis/redis-client.sh HKEYS world1:input
