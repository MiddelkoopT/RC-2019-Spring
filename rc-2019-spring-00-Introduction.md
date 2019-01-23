# IMSE 8410 Spring 2019 - Introduction

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop. Sourcecode
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Introduction

The objective of this course is give students the skills, tools, and
hands-on experience required to effectively utilize advanced
computational and data capabilities for their research.  Topics will
include command line usage, batch submission on HPC systems, source
code revision management systems, relational and non-relational
databases, message and data structures, web application programmer
interfaces, computational engineering software, software development,
test driven development (TDD), scientific and engineering workflows,
data management, experimental design, and the life-cycle of research
projects.  Tools include Git, Python, R, Julia, SQLite with domain
specific tools such as CPLEX, Gurobi, and others.

### Outline 
 * Welcome and personal introduction
 * Motivation for the class (scientific and engineering workflows)
 * Class overview and outline of topics
 * Hands on with secure shell (ssh).
 * What is Research Computing?
 * Careers in Research Computing

### Hands on
 * Use a secure shell client and connect to `clark.rnet.missouri.edu` using your pawprint login (SSO) and password.  You must use all lower case for your username and do not include the `@` or anything after it.
 * The following ssh clients are recommended: 
   * MobaXterm (https://missouri.app.box.com/rcss-mobaxterm) for Windows, 
   * Putty (https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe ) for Windows, 
   * or hterm, the Chrome browser “Secure Shell” extension for Windows, Mac, and Chromebooks (https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo).
   * Mac users can use the built-in terminal by launching it from Spotlight by hitting `Command + Spacebar` and typing `Terminal` and then return.  To connect to the teaching cluster enter the command `ssh pawprint@clark.rnet.missouri.edu` where `pawprint` is your login (SSO) and enter your password when prompted.

### Discussion 
 * What is Information Technology?
 * What does High Performance Computing mean to you?
 * What about computational and data research would you like to learn?

Information Technology (IT), and by extension research computing
systems is the **physical**, **computational**, and **software**,
infrastructure built by **teams**, to manage **information**.

IT needs **physical** infrastructure consisting of
 * power, 
 * cooling,
 * and space,

to supports the fundamental **computational** resources 
 * compute,
 * storage, and
 * networking.

From these resources a **software** system is built through
 * provisioning (physical and logical), 
 * configuration,
 * software (Operating System, libraries, applications), and
 * security.

This infrastructure is used to **manage information** (data) through 
 * business process,
 * data,
 * policy, and
 * security.

All this is all brought together by **teams** with 
 * people,
 * process, and
 * community.

** Security a fundamental property of systems and applications.

### Reading
 * Chapter 1, Introduction. "High Performance Computing: Modern Systems and Practices"
 
### Homework
Homework 1-0: Using Secure Shell
 1. Connect to clark.rnet.missouri.edu with your pawprint (SSO) and pawprint password and run the following commands and copy and paste the session (as text).
    1. `hostname`
    1. `whoami |sum`
