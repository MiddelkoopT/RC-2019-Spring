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
        """ Creates a new campaign, closes out all current/pending campaigns """
        commitid=str(self.git.head.commit)
        print("commitid",commitid)
        cursor=self._db.cursor()
        cursor.execute("UPDATE Campaign SET closed=?",(True,))
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

    def start(self):
        """ Start experiments """
        cursor=self._db.cursor()
        result=cursor.execute("SELECT id, commitid, name FROM campaign WHERE closed IS NULL")
        self.campaign, commitid, self.name = result.fetchone()
        print("+++", self.campaign, commitid, self.name, self.jobid, self.stepid)

    def add(self,parameters):
        cursor=self._db.cursor()
        cursor.execute("INSERT INTO experiment (campaign, parameters) VALUES (?,?)",
                       (self.campaign, parameters))
        self._db.commit()

    def get(self):
        cursor=self._db.cursor()
        result=cursor.execute("SELECT id, parameters FROM experiment WHERE campaign=? AND started IS NULL LIMIT 1",(self.campaign,))
        self.experimentid, parameters = result.fetchone()
        print("---",self.experimentid, parameters)
        cursor.execute("UPDATE experiment SET started=datetime('now') WHERE id=? AND started IS NULL", (self.experimentid,))
        assert self._db.total_changes==1 ## race condition achieved!
        self._db.commit()
        return json.loads(parameters)
        

## Tests
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
        e.start()
        parameters=e.get()
        

