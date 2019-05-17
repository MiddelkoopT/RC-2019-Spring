#!/bin/bash

. ./environment.sh

zcat data/USA-road-d.NY.gr.gz | python3 nodes/path.py
