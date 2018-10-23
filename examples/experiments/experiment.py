#!/usr/bin/python3
# Simple experimental control
# Copyright 2018 by Timothy Middelkoop, Licensed under the Apache License 2.0

import os

import configparser
import sqlite3
import json

import git


class Experiment:
    def __init__(self):
        self._db=sqlite3.connect('experiment.db')
        config=configparser.ConfigParser()
        config.read('local.ini')
        self.git=git.Repo(config.get('global','repo'))
        self.jobid=os.environ.get('SLURM_JOB_ID',None)
        self.stepid=os.environ.get('SLURM_STEP_ID',None)

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

    def add(self,parameters):
        cursor=self._db.cursor()
        cursor.execute("INSERT INTO Experiment (campaign,parameters) VALUES (?,?)",
                       (self.campaign, parameters))
        self._db.commit()

def testExperiment(e):
    e.new("Test1")

    ## Define 2D 3x4 array
    for j in range(0,3):
        for k in range(0,4):
            e.add(json.dumps((j,k)))

## External entrypoint for utility functions/testing.
if __name__=='__main__':
    print('=== experiment.py')
    e=Experiment()
    if e.jobid is None:
        testExperiment(e)
    else:
        print("Slurm Job ID",e.jobid)

