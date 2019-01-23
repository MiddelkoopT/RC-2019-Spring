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
 * Hands on with secure shell (ssh)
 * Careers in Research Computing
 * Discussion

### Hands on
 * Use a secure shell client and connect to `clark.rnet.missouri.edu` using your pawprint login (SSO) and password.  You must use all lower case for your username and do not include the `@` or anything after it.
 * The following ssh clients are recommended: 
   * MobaXterm (https://missouri.app.box.com/rcss-mobaxterm) for Windows, 
   * Putty (https://the.earth.li/~sgtatham/putty/latest/w32/putty.exe ) for Windows, 
   * or hterm, the Chrome browser “Secure Shell” extension for Windows, Mac, and Chromebooks (https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo).
   * Mac users can use the built-in terminal by launching it from Spotlight by hitting `Command + Spacebar` and typing `Terminal` and then return.  To connect to the teaching cluster enter the command `ssh pawprint@clark.rnet.missouri.edu` where `pawprint` is your login (SSO) and enter your password when prompted.

### Discussion 
 * What does High Performance Computing mean to you?
 * What about computational and data research would you like to learn?
 * What is Information Technology?

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

## Working with a Cluster

And in the beginning there was git. `git init`

### Basic Linux
There are a number of good tutorials and videos online.  We use the Software Carpentry website section on the Linux Shell (http://swcarpentry.github.io/shell-novice/) sections 1-3.

To get help run the `man` command with the first argument with the name of the command.  Many programs you can also just run the command with `--help`, for example `man --help`.

CLI Concepts:
* prompt/shell, path, file, program, arguments, switches

Basic commands:
* `man`, `ls`, `pwd`, `cd`, `mkdir`, `rmdir`, `mv`, `rm`, `echo`, `touch`, `cat`, `less`, `grep`, `wc`, `sort`, `gzip`
* `git`
* `ssh`, `wget`, `curl`, `rsync`
* `tar`, `unzip`, `zip`
* `exit`

Redirection:
* `<`, `>`, `>>`, `|`, 

Editors:
* `nano`, `emacs`, `vi`


### Git

We will first create a `gitlab.missouri.edu` repository and clone it.

Go to Mizzou's Gitlabs server at https://gitlab.missouri.edu and login using your Pawprint (SSO) and password (use the default LDAP method).

Create a new private project called `rc-login-First-Last` where login is your pawprint, for example I would be `rc-middelkoopt-Timothy-Middelkoop`.

Make sure your gitlabs project visibility is set to private. To make it priviate navigate to Settings -> Sharing and Visibility -> Project Visibility -> Private.

Share this project with myself `@middelkoopt` with the access "Reporter".

Create a ssh key by logging into `clark.rnet.missouri.edu` and running the following (make sure to create a strong passphrase):

```
$ cd ~
$ ssh-keygen
$ cat .ssh/id_rsa.pub
```

Copy the public key shown by the `cat .ssh/id_rsa.pub` command, it should look similar to this:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDuSqEsyPw9gULRil72VHCrpw/+dmKpcPp50rr7YypK95T4US7eiwOqX0VJANKde77MjAy7+rgbjNJDbO6V3VLSJxOlUWS4Vj7wBF1j/u7EUnjdp2mMMHA2zu7sIwbjp+tjt44MYxK1P/RbB1sXwwIOUvxOZjG1uKsO/Xze6GX3l2pxkb+aDiZ+i8JZdnwC9+0ZFwUVBhcXO90IHapz1rppTFO9K1LRJtj/aiSOcD2E0mphLLDD7Z5l9EDK0tijYz/fB2F0lUFlF1isjKAGkW+Uq5CzsMDtfXWG5skaEKMf2ujMDGEenHZ3662tN2XfVc/I6NOGFGZ9QH+jLmV7JhCl middelkoopt@tc-m610-login-node623
```

Go back to gitlabs and add your public ssh-key to your account as follows (the Avatar/Account button is on the top right of the page):

```
"Avatar" -> Settings -> ssh-keys -> Key: paste public key
```

Now go to "Project" website and copy the git URL by doing the following (the "Hamburger" is the icon with three lines on the top left of the page).

"Hamburger" -> Projects -> Your Projects -> select the project to
clone (in this case mis-$USER-$NAME) -> home -> click the clipboard
icon next to the URL, make sure SSH is selected not HTTP.

Now go to your class folder on `clark.rnet.missouri.edu` and clone the repository
```
git clone git@gitlab.missouri.edu:middelkoopt/welcome.git
```
where `git@gitlab.missouri.edu:middelkoopt/welcome.git` is the pasted from the step before.

### Homework

1. Homework 1-2: Gitlabs
    1. Create a repository on https://gitlab.missouri.edu called rc-pawprint-first-last as described in the Hands-On section (`git@gitlab.missouri.edu:$PAWPRINT/mis-$PAWPRINT-$FIRST-$LAST.git`).
    2. Assign "Reporter" permissions to `@middelkoopt` to the project
    3. Create a `ReadMe.md` file and commit it to the repository (note the upper/lower case and spelling).
    4. Clone the repository on `clark.rnet.missouri.edu`
    5. Modify the `ReadMe.md` on `clark.rnet.missouri.edu` and push it back to `gitlab.missouri.edu`.  Include your name and short one paragraph biography.
    6. Run `git log` and paste the last commit/revision/hash or the output of `git rev-parse HEAD` into the homework assignment.

### References
* Software Carpentry: Linux Shell (http://swcarpentry.github.io/shell-novice/) sections 1-3
* Pro Git book https://git-scm.com/book/en/v2
* Software Carpentry - Git http://swcarpentry.github.io/git-novice/
* GitLabs Markdown https://docs.gitlab.com/ee/user/markdown.html

