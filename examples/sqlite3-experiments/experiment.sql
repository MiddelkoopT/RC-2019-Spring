-- Simple experimental control
-- Copyright 2018 by Timothy Middelkoop, Licensed under the Apache License 2.0

CREATE TABLE Campaign (
       id INTEGER PRIMARY KEY,
       repo TEXT,
       commitid TEXT,
       branch TEXT,
       dirty TEXT,     -- Repo is dirty
       name TEXT,      -- Human readable name of this campaign
       config TEXT,    -- JSON configuration used to create the campaign
       note TEXT,      -- Optional Notes
       started DATE,
       finshed DATE,
       closed DATE     -- Campaign is closed (finished or aborted)
);

CREATE TABLE Experiment (
       id INTEGER PRIMARY KEY,
       campaign INTEGER,
       parameters TEXT, -- JSON parameters for the experiment
       runid INTEGER    -- 
);

CREATE TABLE Run (
       id INTEGER PRIMARY KEY,
       campaign INTEGER,
       cluster TEXT,   -- SLURM job information
       jobid INTEGER,
       stepid INTEGER,
       arrayid INTEGER
);

CREATE TABLE Result (
       id INTEGER PRIMARY KEY,
       campaign INTEGER,
       experiment INTEGER,
       run INTEGER,
       result TEXT,
       started DATE,
       finsihed DATE
);
