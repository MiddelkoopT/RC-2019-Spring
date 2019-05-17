# Redis on Clark

## Build a local copy of redis
```
cd src
wget http://download.redis.io/releases/redis-5.0.4.tar.gz
tar -xzf redis-5.0.4.tar.gz
cd redis-5.0.4
make install
install -dvp $HOME/opt/redis
make PREFIX=$HOME/opt/redis install
```

## Run and test server
```
sbatch redis-server-jobfile.sh
echo set test 1 | ./redis-client.sh
echo get test | ./redis-client.sh
```
