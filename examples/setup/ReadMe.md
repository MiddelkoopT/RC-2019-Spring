## Setup depencies for this wonderful program

Setup environment (once)

```
srun bash setup.sh
```

Run test scripts (development with loaded modules and explicit config)

```
srun --pty /bin/bash
. ./environment.sh
srun python3 script.py config.json
srun Rscript script.R config.json
exit
```

Run jobfile (defaults to config.json)
```
sbatch jobfile.sh
```

Run all configurations
```
bash ./run.sh
```

Cleanup
```
bash ./cleanup.sh
```
