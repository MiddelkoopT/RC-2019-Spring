#!/usr/bin/python3

import json
import sqlite3

db=sqlite3.connect("map.db")
c=db.cursor()

m={}
for key,value in c.execute("SELECT * FROM map"):
    m[key]=value

print(json.dumps(m))

