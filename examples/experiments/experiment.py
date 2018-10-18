#!/usr/bin/python3
# Simple experimental control
# Copyright 2018 by Timothy Middelkoop, Licensed under the Apache License 2.0

import configparser
import sqlite3

import git


class Experiment:
    def __init__(self):
        self._db=sqlite3.connect('experiment.db')
        config=configparser.ConfigParser()
        config.read('local.ini')
        self.git=git.Repo(config.get('global','repo'))

    def new(self,name,config=None,note=None):
        commitid=str(self.git.head.commit)
        print("commitid",commitid)
        cursor=self._db.cursor()
        cursor.execute("INSERT INTO Campaign (repo,commitid,dirty,name,config,note) VALUES (?,?,?,?,?,?)",
                         (self.git.remotes.origin.url,
                          commitid, 
                          self.git.is_dirty(), 
                          name, config, note))
        self.campaign=cursor.lastrowid
        self._db.commit()
        self.name=name
        self.config=config
        print("campaign",self.campaign)
        

## External entrypoint for utility functions/testing.
if __name__=='__main__':
    print('experiment.py')
    e=Experiment()
    e.new("Test1")

  
