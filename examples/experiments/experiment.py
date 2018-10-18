#!/usr/bin/python3
# Simple experimental control
# Copyright 2018 by Timothy Middelkoop, Licensed under the Apache License 2.0

import configparser
import sqlite3

import git


class Experiment:
    def __init__(self):
        self.db=sqlite3.connect('experiment.db')
        config=configparser.ConfigParser()
        self.config=config.read('local.ini')
        self.git=git.Repo(config.get('global','repo'))

    def new(self):
        commitid=self.git.head.commit
        print("commitid",commitid)
        print("dirty",self.git.is_dirty())

## External entrypoint for utility functions/testing.
if __name__=='__main__':
    print('experiment.py')
    e=Experiment()
    e.new()

  
