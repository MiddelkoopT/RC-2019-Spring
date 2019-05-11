# IMSE 8410 Spring 2019 - Workflows

*IMSE 8410 Advanced Computational Systems and Data Engineering*

Material Copyright 2017-2019 by Timothy Middelkoop.  Sourcecode
licensed under the Apache License, Version 2.0. Documentation licensed
under CC by SA 3.0.

## Project

The objective of this project is to gain experience with and
demonstrate competency in developing Scientific and Engineering
Workflows and managing data. The project will utilize the methods and
examples covered in the class. Using the "1,2,3, Go" system discussed
in class the data is expected to be "3" (benchmark) and the
computation is expected to be at least "2" (textbook) class.

The project will use the gitlabs `rc-project-$USER-$FIRST-$LAST` git
repository for the project and shared with "Reporter" permission to
the instructor.


### Specific Instructions
  1. The project must implement a reproducible scientific workflow
     that runs on the Clark cluster.
  2. The project results must be reproducible.  The project will be graded by
     cloning the repository and following the provided instructions.  Absolute 
     filenames in configuration files or source code is strictly prohibited.
  3. The workflow must consist of at least a data download and/or
     filtering step, an analysis step, and a results step in at least
     two languages.
  4. The workflow must be able to run multiple analysis or scenarios
     as SLURM jobs with the same analysis code.  At a minimum it must
     be able to run the textbook example (small, step 2) and the
     larger analysis.
  5. All textbook examples (small) must be included in the
     repository with any expected output (use an example folder
     if needed).
  6. There must not be any large data or propriety data in the repo.
     All large data must be public and downloaded as a part of the
     workflow.
  7. Use proper commits.  Commits must be logical and of appropriate
     size with descriptive commit messages.
  8. The workflow must be properly documented, licensed, and use
     proper citation.  The significant use of example code is
     permitted as long as it is sited and the licenses are compatible.
     For the documentation,
	 1. Provide a brief overview of the analysis.
	 2. Document the overall workflow (data, steps, analysis)
     3. Document each step in the process in detail (analysis, transformations).
	 4. Document the source data and the intermediary data (the format
        and metadata of the data between steps).
	 5. Use of the textbook example in the documentation may be helpful.
  9. Multiple workflows must use configuration files (`config.json`),
     not changes in source files.
 10. The primary goal is to build and document a scientific workflow,
     not to do the analysis.



### Grading
The project will be graded on the following areas:
1. The utilization of git to manage the project including properly
   formed commits and commit comments.
2. Documentation of the project with a project level
"project/ReadMe.md" file written in "gitlabs flavored markdown" to
describe the files, data, and metadata.  This file should contain the
references to the data used in the project.
3. Documentation of the project data (metadata) placed in the
"project/ReadMe.md" file in a "metadata" section.  If this data is
copied from the website then the URL must be included in the
document.
4. The quality of the data processing and analysis.
5. The quality of the code (formatting, comments, coding style etc.).
6. The use of SLURM to manage the Workflow.

