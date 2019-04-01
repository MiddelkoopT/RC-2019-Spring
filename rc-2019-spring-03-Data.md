# IMSE 8410 Spring 2019 - Data

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop.  Sourcecode
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Data

"It's all data"

In this module we will cover "data" in research computing and data
systems and the different ways representing, managing, and using this
data.

### Reading
* JSON data format and specification: http://www.json.org/
* Database design with UML and SQL, 4th edition: http://web.csulb.edu/colleges/coe/cecs/dbdesign
  * Models and languages http://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=models.html
  * Basic structures: classes and schemes http://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=class.php
  * Basic structures: rows and tables http://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=tables.php
  * Basic structure: associations http://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=association.php
  * Discussion: more about keys http://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=keys.php
* SQLite tutorial http://www.sqlitetutorial.net/
  * See the "Database Example (chinook)" section on how to load the data.
  * Sections 1-10 (Simple Query - Transactions)
* Software Carpentry - Databases and SQL http://swcarpentry.github.io/sql-novice-survey/
  * See the "Hands On SQLite3" section on how to load the databvase.
  * Section 1-6 (Selecting Data, Sorting and Removing Duplicates,
    Filtering, Calculating New Values, Missing Data, and Aggregation).

### Data

In order to collect, process, and analyze data we must first store and
represent it in a computing and storage system.  Most data can be
represented by the following fundamental data types (this is a loose
definition):

 * Byte: an opaque 8-bit value. Often represented in hex.  Example `0xFF 0xFE`
 * Integer: A whole number (Int32, Int64). Example: `42`
 * Float: A floating point number (an estimate), (Float32, Float64).  Often represented in IEEE 754 format. Example `3.14e1`
 * String: Human readable text.  Often encoded as UTF-8. Example `"世界"`
 * Boolean: True or False
 * Array: An indexed collection of values. Index starts at 0 ('C' format) or 1 (Fortran format).  Example: `[ 100, 200, 300]`
 * Associative Array: A collection of key/value pairs.  Accessed via the key.  Example `{"Apple": 1, "Banana":2}`
 * Date and Time: Seconds since January 1, 1970. Often displayed in ISO 8610. Example: `2017-09-19T08:00Z`
 * Object.  A collection named attributes with values.
 * NULL: The absence of a value.

The data transfer format we will be using this semester
is [JSON](http://www.json.org/).  Example:
```JSON
{
	"Apple": 1,
	"Banana": 2,
	"Carrot": [100, 200, 300]
}
```

### Hands-On Python

[Python](http://python.org) is an popular Open Source language for
scripting and doing data processing.  In this class will be using
Python 3.

Log in to the teaching cluster for the following hands-on exercise.

First, Create a new file called `data.json` and place the above JSON
example in it.  Run the following test (`jq`) to ensure the data is formatted
correctly.

```bash
echo '{"Apple": 1, "Banana": 2, "Carrot": [100, 200, 300]}' > data.json 
jq . data.json
```

To start an interactive Python 3 shell on a node run the following command:
```bash
srun --pty python3
```

Then enter the following commands to load the JSON data.
```python
import json
f=open("data.json")
d=json.load(f)
f.close()
```

Show the data structure in Python
```
d
```

Add "Apples and Banana's"
```python
d["Apple"]+d["Banana"]
```

To exit Python either press the `control-d` key or run the exit function.
```python
exit()
```

### Hands On Julia

[Julia](https://docs.julialang.org) is an Open Source
scientific/engineering language loosely based on Matlab but
dramatically faster and built to take advantage of multiple core and
multiple node systems (HPC).

Log in to the teaching cluster for the following hands-on exercise.

First, Create a new file called `data.json` and place the above JSON
example in it.  Run the following test to ensure the data is formatted
correctly.

Load the Julia module and launch Julia on a compute node (if the
`srun` command fails just run `julia`).

```bash
module load julia/julia-0.5.0
srun --pty julia
```

The first time we use JSON in Julia we must first install the
package. This command may take some time to run.  Only run once.

```Julia
Pkg.add("JSON")
```

Load the package for use (every time we use Julia) and load the JSON file.
```Julia
import JSON
d=JSON.parsefile("data.json")
```

This should show the parsed JSON data (same information, different representation).

Add "Apples and Banana's"
```Julia
d["Apple"]+d["Banana"]
```

To exit Julia either press the `control-d` key or run the exit function.
```Julia
exit()
```


### Homework
Homework 3-1: JSON and Python
  1. In your class repository create a folder called `homework-3-1` and place all the files here.
  2. In this folder create a `example1.json` file with **valid** JSON that represents some data.  For example (but you cannot use this one) a sample from a weather station.
  3. Load this data into Python and do some simple calculations on it.  Feel free to read the Python manual for advanced commands.
  5. Copy the calculations and the results into a `output.md` file the homework folder (text, not screen-shots).
  4. Commit and push your work (the JSON and `output.md` file) to Gitlabs.
  6. Copy the `commit-id` and the repository URL


### Hands-On SQLite3

You may find the SQLite SQL Reference
(http://www.sqlite.org/lang.html) useful in understanding commands.

All the following examples are using the teaching cluster.  Please
change your current directory to a folder to contain these examples
(do not use your home folder).

Get the data from the example
```bash
srun wget -c https://github.com/swcarpentry/sql-novice-survey/raw/gh-pages/files/survey.db
```

Start SQLite3 with the sample data
```bash
srun --pty sqlite3 survey.db
```

Use the `.help`, `.exit`, `.tables`, `.schema`, and `.dump` commands.

### Homework

Homework 3-2: SQLite3. 

Download and start `sqlite3` as per the above hands-on instructions.
Complete the following and copy/paste the session into the course
assignment similarly named:
  1. Display the database schema.
  2. List the columns for the `Site` table.
  3. Who took samples from site  'DR-1' on '1927-02-10. (use a SQL comment `-- 3-2: Your answer` to record your answer)
  4. Write an SQL statement for the above question.
  6. Formulate another question to ask the database (use a SQL comment `-- 3-2: Your answer` to record your answer)
  7. Write and SQL statement for the above question.

### Databases

In this section we will explore relational databases in the context of
an example database (https://chinookdatabase.codeplex.com/). Some of
the examples are taken from http://www.sqlitetutorial.net/

First create a simple database and use it.
```bash
srun --pty sqlite3 simple.db
```

```sql
.header ON
CREATE TABLE map (key string PRIMARY KEY, value number);
INSERT INTO map (key,value) VALUES ("One",1),("Two",2);
SELECT * FROM map WHERE key="One";
UPDATE map SET value=100 WHERE key="One";
DELETE FROM map WHERE key="One";
```

Save the database to an `.sql` file and commit it to git.
```bash
sqlite3 simple.db .dump > simple.sql
git add simple.sql
git diff -r HEAD
git commit
```

### Database Example (chinook)

Now download, unzip, and run the sample database.
```bash
wget -c http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip
unzip chinook.zip
srun --pty sqlite3 chinook.db
```

Review the database [**schema**](http://www.sqlitetutorial.net/wp-content/uploads/2018/03/sqlite-sample-database-diagram-color.pdf).

Some sample queries:
```sql
SELECT * FROM tracks JOIN genres ON tracks.GenreId=genres.GenreId;
SELECT CustomerId, InvoiceDate, BillingCity FROM invoices;
```

### Homework

Homework 3-3: Chanook

Download and load the chinook datbase as described in the notes and
answer the following questions. Copy and paste the SQL commands into
the file `homework-3-3/chanook.sql` and paste the commit-ID and
repository in the course homework assignment.  For written questions
use the "SQL Comment" syntax (`-- comment`) within SQLite.
  1. Develop a simple question to ask the database.  The question must
     limit the data to a subset of a table or tables.
  2. Write and execute the SQL for the previous question.
  3. Develop a more complex question will span at least two tables.
  4. Write and execute the SQL for the previous question.


### Example Database (Baseball)

The next in-class example is using a baseball statistics database.
 * Baseball Data http://www.seanlahman.com/baseball-archive/statistics/
 * Sqlite3 version of the data https://github.com/jknecht/baseball-archive-sqlite

```bash
wget https://github.com/jknecht/baseball-archive-sqlite/raw/master/lahman2016.sqlite
srun --pty sqlite3 lahman2016.sqlite
```

Many time you will want to save the query, not just run it in the
shell.  To do this save the query in a file and *redirect* the output
into the `sqlite3` command and optionally redirect the output to a
file.  For the following example:

What did the top 10 season hitters of all time make during that year?
```sql
SELECT 
  Master.playerID, 
  Master.NameLast,
  Master.debut,
  Salaries.YearID,
  Batting.YearID,
  Batting.H
FROM
  Master
JOIN Salaries ON Master.playerID=Salaries.playerID
JOIN Batting ON Master.playerID=Batting.playerID
WHERE
  Salaries.yearID=Batting.yearID
ORDER BY Batting.H DESC, Master.playerID
LIMIT 10;
```

Save the text to a file called `baseball.sql` and run the following command (it takes about 50 seconds to run):
```bash
srun sqlite3 lahman2016.sqlite -header -csv < baseball.sql > baseball.csv
```

Please note the `srun` command runs the `sqlite3` command on a node in
the cluster.  The `-header` and `-csv` make it so the output can be
used by programs such as Excel, R, Julia, Python, etc.  One way to
access the file is to commit it to git and download it from VCS.
There are other tools to access files via either "sftp" or "rsync" but
those methods are left as an exercise for the reader.

### Homework

Homework 3-4: Databases

Design a small simple database based on a real world example with at
least two relationships and three tables.  The database should be
stored in `homework-3-4/realworld.sqlite` file and the SQL creation
and queries should be placed in the `homework-3-4/realworld.sql`
file and be annotated with SQL comments.  The metadata should be
placed in the file `homework-3-4/realworld.md` and be written in
gitlabs markdown in a similar format as the Baseball example used in
class.  You must not use an example used in class, in any other
assignment, or any other public or private source.  You must not use
proprietary or sensitive data and all data must be synthetic (made
up).
  1. Describe the database structure in the
     `homework-3-4/realworld.md` file.  Include as many sections as
     relevant.  Describe all relevant relationships.
  2. Using SQL create the tables.  Define the *Primary Key* but do no
     not force referential integrity.
  3. Populate the database with data in all tables, enough to be
     non-trivial and be usable in the remaining questions.
  4. Demonstrate the use of the `JOIN` statement on one or two
     relationships.
  5. Develop a simple question of the database and write the SQL to show
     the answer.  This must be more than `SELECT * FROM simple`.
  6. Develop a question that requires the use of the `GROUP BY` and
     aggregate functions (`SUM`, `COUNT` etc.).  Write the SQL to show
     the answer.
  7. Commit `homework-3-4/realworld.sql` and
     `homework-3-4/realworld.md` to your git class assignment
     repository and push it to your class repository.

### References
 * ASCII https://en.wikipedia.org/wiki/ASCII
 * UTF-8/Unicode http://www.fileformat.info/info/charset/UTF-8/list.htm
 * JSON data format and specification http://www.json.org/
 * HDF5 data format introduction https://portal.hdfgroup.org/display/HDF5/Introduction+to+HDF5
 * Database Design http://web.csulb.edu/colleges/coe/cecs/dbdesign/
 * SQL database SQLite http://www.sqlite.org/
 * SQLite tutorial http://www.sqlitetutorial.net/
 * Software Carpentry - Databases and SQL http://swcarpentry.github.io/sql-novice-survey/
