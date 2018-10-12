#!/usr/bin/python3
# Simple experimental control
# Copyright 2018 by Timothy Middelkoop, Licensed under the Apache License 2.0

import sqlite3
import subprocess

class Experiment:
    def __init__(self):
        self.db=sqlite3.connect('experiment.db')

    def new(self):
        hostname=subprocess.run(['hostname'],stdout=subprocess.PIPE).stdout
        print("hostname",hostname)

## External entrypoint for utility functions/testing.
if __name__=='__main__':
    print('experiment.py')
    e=Experiment()
    e.new()

    
