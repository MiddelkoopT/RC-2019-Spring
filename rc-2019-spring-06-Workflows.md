# IMSE 8410 Spring 2019 - Workflows

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop.  Sourcecode
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Research and Engineering Computational and Data Workflows

Computational and Data workflows are about building new systems and
scaling existing ones.  The best approach is to do things deliberately
and incrementally, which means starting small, testing often, and
scaling slowly both in terms of code and data.

One method for this is to use the 1,2,3 Go method, which can be expanded to 1:
  1. Hello - get the technology working.
  2. Textbook Example - do something easy.
  3. Benchmark and Reference problems - resolve community problems.

Only after this go and solve your original problem.

This will provide a framework to test code and data alike in a
sustainable way, making the use of techniques such as Test Driven
Development (TDD) and Continuous Integration (CI) a natural and
logical next step.

### Reading
 * Scientific Workflows:
   http://www.pnl.gov/computing/technologies/sci_workflow.stm

### Workflows

Even before a workflow is created there are important prerequisites.

1. A problem statement.  What research, engineering, or business
   question are you trying to answer.
2. A description of the system.  Detailed information about the system
   that the question derives its information.
3. Actual data.  Access to the full raw data.  A subset in an
   spreadsheet does not count.  The way in which the data is to be
   extracted in used must also be in place (access to the database for
   instance).
4. Metadata.  A proper description of the actual data fields and the
   data relations is required.
4. A Data Management Plan.  Who owns the data and can you publish the
   results?  What are the security requirements?  Who will have access
   to this data? Where will the data live? How will it be stored and
   tracked? How will the integrity of the data be assured (checksums,
   backups, etc).

Once the these requirements have been met, then a workflow can be
developed. A workflow in general consists of the following steps:

1. Data Acquisition (Input)
   * Test Data (simple and known-good-solutions)
   * Generated Data
   * Benchmark Problems
   * Real Data
2. Data Pre-Processing
   * Data format conversion
   * Data filtering (subset)
   * Data cleaning (matching events, outliers etc.)
   * Data transformation (arc based to node based)
   * Data pre-processing and storage (preparation for analysis)
3. Experimental and Analysis Control
   * Plan and generate jobs (experiments, analysis parameters etc).
   * Prepare data and jobs (marshal data)
   * Monitor job progress
4. Computation
   * SLRUM runs the jobs on the cluster
   * Job get's input for computation
   * Job runs computation (Python)
   * Job collects and writes data
5. Results Collection
   * Collect and verify data (feasibility and structure/format).
   * Transform and filter for analysis
   * Comparison with *known good solutions* for verification
6. Analysis and Analytics (Output)
   * Statistics (R)
   * Visualization 
   * Report generation

These steps utilize the following components:
1. A source code management system (git) to manage code.
2. A project management system (gitlabs) to manage people and work.
3. A data management system (may include a database) to manage data and metadata.
4. A job management system (experiment generation and a cluster with SLURM) to manage compute.
5. An information management system to coordinate everything (workflows).
6. Documentation to help others understand, including yourself.
7. Data visualization to see the data, the code, and the analysis in action.

