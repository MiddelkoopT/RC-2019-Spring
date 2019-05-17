# Python Virtual Environments.

Accepted way of providing a light weight Python virtual environment.
Installs inside the project directory and is lightweight

This example utilizes the openpyxl module as a test.

To setup the environment (only run once - it takes a while), it removes the old environment.
```
srun ./setup.sh
```

To use the environment for development.
```
srun --pty --mem=20G /bin/bash
source ./environment.sh
python3 example.py example.xlsx
```

To submit a job run
```
sbatch jobfile.sh
```

