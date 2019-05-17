FROM centos:7
MAINTAINER Timothy Middelkoop

## Basic install/update
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git

## Build environment
RUN yum install -y gcc gcc-c++ patch file make bzip2

## Build Spack
RUN install -dv -o nobody spack .spack
USER nobody
RUN git clone https://github.com/spack/spack.git
RUN ( . spack/share/spack/setup-env.sh; spack install lmod )

COPY spack.sh /
