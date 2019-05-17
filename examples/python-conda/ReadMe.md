# Python Virtual Environments.

Installs the complete miniconda system for local packages.

This example utilizes the pandas module as a test.

To setup the environment (only run once - it takes a while), it removes the old environment.
```
srun --mem=10G ./setup.sh
```

To use the environment for development.
```
srun --pty --mem=20G /bin/bash
source ./environment.sh
python3 example.py
```

To submit a job run
```
sbatch jobfile.sh
```

