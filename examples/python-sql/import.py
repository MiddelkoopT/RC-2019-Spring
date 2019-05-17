#!/usr/bin/python3 

print("import.py")

import sys
import json
import sqlite3

f=open("config.json")
config=json.loads(f.read())

m=json.loads(sys.stdin.read())

print(m)

db=sqlite3.connect(config["db"])
c=db.cursor()

for key,value in m.items():
    print(key,value)
    c.execute("INSERT INTO map (key,value) VALUES (?,?)" , (key,value))

c.close()
db.commit()
db.close()


