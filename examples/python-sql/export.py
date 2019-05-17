#!/usr/bin/python3 

import json
import sqlite3

db=sqlite3.connect("map.db")
c=db.cursor()

m={}

for key,value in c.execute("SELECT key,value FROM map"):
    m[key]=value

c.close()
db.close()

print(json.dumps(m))

