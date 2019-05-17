#!/usr/bin/python3

import json
import sys
import csv

print("script.py>", sys.argv[1])

if __name__=='__main__':

    config=json.load(open(sys.argv[1]))

    name=config['data']
    print(name)
    d=csv.DictReader(open(name))

    for r in d:
        print(int(r['a1'])+int(r['a2']))
