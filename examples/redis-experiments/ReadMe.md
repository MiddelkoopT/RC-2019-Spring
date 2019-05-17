# Experiment Control w/ Redis and Python

## Setup Python Virtual Env.
```
( cd python ; ./setup.sh )
```



## Load Redis server and load environment
```
./server.sh
. ./environment.sh
```

## Test redis server
```
cd redis ; ./test.sh
```

## Project Development
```
. ./environment.sh
cd python ; python3 ./test-redis.py
python3 manage/server.py
python3 manage/generate.py
```

## Application Example
```
nodes/setup-download.sh
nodes/run.sh
```
