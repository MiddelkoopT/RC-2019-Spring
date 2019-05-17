# Containerization

## Build Vagrant and Run Shell
```
vagrant plugin install vagrant-reload
vagrant up
vagrant ssh
```

## Build Docker and Run Shell
```
docker build -t spack .
docker run -i -t spack
```

## Build Singularity and Run Shell
```
sudo singularity build spack.img Singularity
singularity shell spack.img
```

## Spack Build
```
git clone https://github.com/spack/spack.git
. spack/share/spack/setup-env.sh
```
