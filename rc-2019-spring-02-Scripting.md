# IMSE 8410 Spring 2019 - Scripting

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop.  Sourcecode
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Automation

Running codes remotely on large HPC systems requires
automation. Scripting does not only make running software faster in
the long term but it also makes it reproducible.  By combining source
code management, data management, package management, and scripting
research can be made easily reproducible.  The use of containers can
also make running software independent of the underlying environment.

In order to run many programs (jobs) on a large system at once a
resource manager is needed in order to schedule all the programs.  Job
submission scripts (jobfiles) are written in bash shell scripts and
shell scripts are also good for simple scripting and automation.

For more sophisticated workflow automation the Python scripting
language should be used.

Python 3 is used in this class and Python 2 should be avoided as it is
end of life.

### Reading
 * HPC Carpentry - Introduction https://hpc-carpentry.github.io/hpc-shell/ (Sections 1-6)
 * HPC Carpentry - Python https://hpc-carpentry.github.io/hpc-python/ (Sections 1-6)

### References
 * SLURM: https://slurm.schedmd.com/

