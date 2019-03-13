# IMSE 8410 Spring 2019 - Applications

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop.  Sourcecode
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Applications and Integration

### Reading
 * R Tutorial http://www.cyclismo.org/tutorial/R/ (Sections 1-9)
 * Software Carpentry R Tutorial http://swcarpentry.github.io/r-novice-inflammation/ (Sections 1-4)

### R

The [R language](https://www.r-project.org/) is used extensively in
industry and academia and is an open source alternative to many
expensive statistical software packages.  R utilizes a shell like the
rest of the tools covered in this course and allows for easy
automation for statistical analysis tasks.

To run R you must first load the module, then run it on the cluster (check the version!)
```
module avail r/
module load r/r-3.5.3-python-2.7.14-tk
srun --pty R
```

In R you can quit by running `quit(save='no')` or by pressing `control-d`.

Students that are running MobaXterm can display graphs (this may be
slow over wireless or from home).  To test this in the R shell run the
following:

```R 
plot(1) 
```

To write a plot to a PNG file (supported by most browsers) adapt the example below

```R
png(filename = "Rplot%03d.png")
d <- read.csv("http://www.cyclismo.org/tutorial/R/_static/simple.csv",header=TRUE)
plot(velocity~mass,d)
dev.off()
```

To view the file you can either use a "sftp" client or commit it to
the git repository.  MobaXterm has a built in sftp client (sftp tab on
side) and there is an excellent open source sftp client for windows
WinSCP (https://winscp.net).  ChromeOS (Chomebooks) can use the SFTP
button/client in the secure shell app used in this class that allows
access to the files via the built-in file browser.


The following example shows how to run an R script on the command line.
```bash
module load r/r-3.5.3-python-2.7.14-tk
srun Rscript example.R
```

The example `example.R` file contains the following:
```R
3+4
```

### Python

[Python](http://python.org) is an popular Open Source language for
scripting and doing data processing.  In this class will be using
Python 3.

To start an interactive Python 3 shell on a node run the following command:
```bash
srun --pty python3
```

You can save python scripts in a file and run them.  For example the
following file called `example.py`

```python
print("Hello World")
```

can be run by entering the following command
```bash
srun python3 example.py
```

### Julia

[Julia](https://julialang.org) is an emerging Open Source language
similar to Matlab.  It has better performance and supports multi-core
and multi-node parallelism.  Vectorization of code to increase
performance is not required.

To run Julia on a single node with a single core, run the following:
```
module load julia/julia-0.5.0
srun --pty julia
```

To run 4 cores and 10GB or RAM use
```
module load julia/julia-0.5.0
srun --pty --mem=10G -c 4 julia -p 4
```

See the Julia docs (https://docs.julialang.org) for basic and advanced
use.

### References
 * Python Tutorial https://docs.python.org/3/tutorial/
 * Python Reference https://docs.python.org/3/
 * Python Regular Expressions https://docs.python.org/3/library/re.html
 * Software Carpentry - Python: http://swcarpentry.github.io/python-novice-inflammation/
 * R tutorial http://www.cyclismo.org/tutorial/R/
 * Software Carpentry R module http://swcarpentry.github.io/r-novice-inflammation/
 * R language introduction https://cran.r-project.org/doc/manuals/R-intro.html
 * Introduction to R and Statistics for IMSE 4410
   * https://github.com/MiddelkoopT/Stats-2016-Spring/blob/master/stats-2016-00-Introduction.Rmd (R markdown)
   * https://github.com/MiddelkoopT/Stats-2016-Spring/blob/master/stats-2016-00-Introduction.pdf (pdf)
 * Julia Docs https://docs.julialang.org 
