# IMSE 8410 Spring 2019 - GitLabs

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop.  Sourcecode
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Project and Code Management

Managing a research project and the associated code and data is an
important part of the research lifecycle.  The ability to produce and
communicate reproducible research must be deliberate and requires the
use of project and source code management tools and techniques.  The
set of tools and services (GitLab, GitHub) surrounding the git
distributed version control tool provide a powerful combination of
project management, collaboration, and source code management
capabilities that have been widely adopted.  In this section we
explore the use of git and GitLab for this purpose.

### Reading

* Pro Git (https://git-scm.com/book/en/v2) Chapters 1 (except 1.5), 2, 3, 5, (6 Optional)
* GitLab Flavored Markdown (https://docs.gitlab.com/ee/user/markdown)

### Git Workflow
A git workflow takes changes in an editor and provides a mechanism to create publishable "work" in the form of a "Work Package" in project management speak.  We can see this as a "stack" as follows.

1. Community Repository (gitlab.missouri.edu)
2. Staging Repository (topic branches, maintainers)
3. Machine/Local repository
4. Project index or staging area
5. Project local filesystem
6. Editor (unsaved changes)

Moving up and down this stack is accomplished by a series of git commands (presented in class and below).  Between 1 and 2 is also social.

### Git Workflow Hands-On

Below is the workflow to edit and commit a file.  This is just an example, please be sure to replace many of the example values with actual values that pertain to your environment.

For a new system or repository (if you only configure locally) update your name and email to ensure the commit information is correct.  Optionally set your preferred editor (nano in this case).
```
git config --global user.name "First Last"
git config --global user.email pawprint@missouri.edu
git config --global core.editor nano
```

Clone your project into a folder
```
git clone git@gitlab.missouri.edu:user/welcome.git
cd user
```

At many of the steps throughout the process run the following to see what is going on and your changes.
```
git status
git diff
git diff -r HEAD
```

Edit the ReadMe.md file.
```
nano ReadMe.md
```

Save and exit.  Now view the changes and add the changes to the index.
```
git diff
git add ReadMe.md
```

This is where you would change other files.  When done commit.  First view what is "staged" in the index with

```
git status
```

Then see what your "commit" will be 

```
git diff -r HEAD
```

From this determine a good description (not "changes and updates") and commit the changes.

```
git commit -m "Fix spelling"
```

Now the changes are in the local repository and ready to be "published" to gitlabs (vcs.rnet.missouri.edu).  View the commit in the logs (press 'q' to exit)

```
git log
```

And push to the remote with the following:

```
git push origin master
```

Also verify that the changes have been pushed and there are no more changes.  The last commit is also printed.  This is what is "proof" of your work, and should be submitted to the Homework assignment along with your repository URL.

```
git status
git rev-parse HEAD
```

### Markdown

Markdown is a lightweight text-based language that is easily readable
and renderable.  It is the de-facto standard for simple markup inside
git projects.  Git project websites use variants of this to allow deep linking
into project issues, branches, milestones etc.  We will be using
"GitLab Flavored Markdown"
(https://docs.gitlab.com/ee/user/markdown) in this class.


### Homework

Using the hands-on instructions and the documentation complete the following homework:

Homework 1-1: Markdown
  * Complete the following online tutorial: https://www.markdowntutorial.com

Homework 1-2: Git
  1. If you have not already done so create a git repository on
     `gitlab.missouri.edu` and share it with the instructors and TA.
  2. Ensure that in the commit log the "Author:" line contains your
     full name and email address and fix if need be.
  3. Clean up your repository (removing any extra test files etc.) and commit the changes.
  4. Create a folder called `homework-1-2` in the project and create a
     file called `homework-1-2-shell.txt` that contains the *text* of
     the commands and results (including the prompt) of the following:
	 1. Create a file called `fruit.txt` in the `homework-1-2` folder
        with a number of fruit names, one on each line.
	 2. Display this file to the console/screen (hint `cat`).
	 3. Count the number of fruit in this file using a pipe (`|`).
	 4. Sort the fruit into a second file named `fruit-sorted.txt`
        (hint: redirection).
	 5. Show the changes to `fruit.txt` and `fruit-sorted.txt` that
        you are about to commit and then commit these files to the
        repository.
	 6. What is the **commit** id of the previous step.
	 7. Commit the *text* of the commands and results (including the
        prompt) of the previous steps stored in the
        `homework-1-2-shell.txt` file.
  6. Push all the commits to the `gitlab.missouri.edu` repository and submit the most
     recent (HEAD) commit-id and the `gitlab.missouri.edu` repository URL to the course
     assignment 'Homework 1-2'.

### References
 * Pro Git book https://git-scm.com/book/en/v2
 * Software Carpentry - Git http://swcarpentry.github.io/git-novice/
 * GitLabs Markdown https://docs.gitlab.com/ee/user/markdown
