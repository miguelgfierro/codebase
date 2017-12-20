# Docker for PyTorch

This document explains how to install a docker image in Ubuntu 16.04 with PyTorch, CUDA9 and CUDNN7 in an Azure DSVM.

## Uninstall all NVIDIA dependencies in your VM (optional)
Uninstall all NVIDIA dependencies

    sudo apt-get remove --purge nvidia-*
    sudo apt-get remove --purge bbswitch-dkms  libcupti-dev:amd64 libcupti-doc libcupti7.5:amd64

## Download and install CUDA9

Download [CUDA9](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=deblocal) and install it.

    wget https://developer.nvidia.com/compute/cuda/9.1/Prod/local_installers/cuda-repo-ubuntu1604-9-1-local_9.1.85-1_amd64
    sudo dpkg -i cuda-repo-ubuntu1604-9-1-local_9.1.85-1_amd64
    sudo apt-key add /var/cuda-repo-9-1-local/7fa2af80.pub
    sudo apt-get update
    sudo apt-get install cuda

## Install nvidia-docker

    curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
    sudo apt-key add -
    curl -s -L https://nvidia.github.io/nvidia-docker/ubuntu16.04/amd64/nvidia-docker.list | \
    sudo tee /etc/apt/sources.list.d/nvidia-docker.list
    sudo apt-get update
    sudo apt-get install nvidia-docker

# Clone PyTorch

    git clone https://github.com/pytorch/pytorch

## Replace the new Dockerfile in this repo with the one available in PyTorch root folder

    cp Dockerfile /path/to/pytorch

## Build the Docker image

    cd /path/to/pytorch
    sudo docker build -t pytorchcuda9  .

## Run the image

You can list your docker images by typing:

    sudo docker images

There are several options to run the image. Standard run:

    sudo nvidia-docker run -it pytorchcuda9 bash

Run the image and map your local home to the docker filesystem:

    sudo nvidia-docker run -v $HOME:/mnt/home -it pytorchcuda9 bash

Run the image and open a port to access jupyter:

    sudo nvidia-docker run -p 8888:8888 -v $HOME:/mnt/home -it pytorchcuda9 bash

## Make sure that everything works correctly

Once inside the docker image:

    python
    >>> import torch
    >>> print(torch.__version__)
    0.4.0a0+0bc1505
    >>> print(torch.backends.cudnn.version())
    7005
    >>> print(torch.cuda.device_count())
    4

Enjoy!








