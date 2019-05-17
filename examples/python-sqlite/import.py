#!/usr/bin/python3

import sys
import json
import sqlite3

m=json.loads(sys.stdin.read())

db=sqlite3.connect("map.db")
c=db.cursor()

for key,value in m.items():
    c.execute("INSERT INTO map (key,value) VALUES (?,?)", (key,value))
c.close()

db.commit()
db.close()
