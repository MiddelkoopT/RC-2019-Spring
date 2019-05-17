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
        self.cluster=os.environ.get('SLURM_CLUSTER_NAME',None)
        self.jobid=os.environ.get('SLURM_JOB_ID',None)
        self.stepid=os.environ.get('SLURM_STEP_ID',None)
        self.arrayid=os.environ.get('SLURM_ARRAY_TASK_ID',None)

    def new(self,name,config=None,note=None):
        """ Creates a new campaign, closes out all current/pending campaigns """
        commitid=str(self.git.head.commit)
        print("commitid",commitid)
        cursor=self._db.cursor()
        # Close all open campaigns.  Only allow running a single campaign. Not concurrent safe.
        cursor.execute("UPDATE Campaign SET closed=datetime('now') WHERE closed IS NULL");
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
        cursor.execute("SELECT id, commitid, name FROM campaign WHERE closed IS NULL")
        self.campaign, commitid, self.name = cursor.fetchone()
        print("+++", self.campaign, commitid, self.name, self.jobid, self.stepid, self.arrayid)

    def add(self,parameters):
        cursor=self._db.cursor()
        cursor.execute("INSERT INTO experiment (campaign, parameters) VALUES (?,?)",
                       (self.campaign, parameters))
        self._db.commit()

    def get(self):
        """ Get an experiment/run """
        cursor=self._db.cursor()
        # Grab a run first due to sqlite3 concurrency and no SELECT for UPDATE
        cursor.execute("INSERT INTO run (campaign, cluster, jobid, stepid, arrayid) VALUES (?,?,?,?,?)",
                       (self.campaign, self.cluster, self.jobid, self.stepid, self.arrayid))
        self.run=cursor.lastrowid
        cursor.execute("UPDATE experiment SET runid=? WHERE id=(SELECT id FROM experiment WHERE runid IS NULL LIMIT 1)",(self.run,)) 
        cursor.execute("SELECT id, parameters FROM experiment WHERE runid=?",(self.run,))
        result=cursor.fetchone()
        if result is None:
            cursor.rollback()
            return None
        self.experiment, parameters = result
        assert cursor.fetchone() == None # Multiple experiments assigned to 1 runid
        self._db.commit()

        print("---", self.experiment, self.run, parameters)
        return json.loads(parameters)
        
    def put(self,result):
        pass
        #cursor=self._db.cursor()
        #self._db.commit()
        #(self.experiment, json.dumps(result))


## External entrypoint for utility functions/testing.
if __name__=='__main__':
    print('=== experiment.py')
    e=Experiment()

    ## New Campaign
    if e.jobid is None:
        e.new("Test1")

        ## Define 2D 3x4 array
        for j in range(0,3):
            for k in range(0,4):
                e.add(json.dumps((j,k)))
    ## Run Campaign
    else:
        e.start()
        parameters=e.get()
        if parameters is None:
            print("extra")
        else:
            e.put(parameters)
        #e.finish()

