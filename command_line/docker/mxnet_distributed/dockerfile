# Dockerfile for MXNet version 1.2 built from source in distributed mode
# With CUDA, CuDNN, OpenCV, OpenBlas and KVStore distributed
# Uploaded to dockerhub: https://hub.docker.com/r/hoaphumanoid/mxnet_dist/

FROM nvidia/cuda:8.0-cudnn7-devel-ubuntu16.04

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils \
    && apt-get install -y build-essential git wget curl \
    && apt-get install -y libopenblas-dev liblapack-dev \
    && apt-get install -y libopencv-dev libopenmpi-dev 

ENV PYTHON_VERSION=3.6
RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda create -y --name py$PYTHON_VERSION python=$PYTHON_VERSION numpy pyyaml scipy \
    ipython mkl pandas jupyter ipykernel scikit-learn scipy  && \
    /opt/conda/bin/conda clean -ya
ENV PATH /opt/conda/envs/py$PYTHON_VERSION/bin:$PATH

RUN git clone --recursive https://github.com/apache/incubator-mxnet \
    && cd incubator-mxnet \
    && git checkout 1.2.0.rc3 \
    && git submodule update \
    && make -j $(nproc) USE_OPENCV=1 USE_BLAS=openblas USE_CUDA=1 USE_CUDA_PATH=/usr/local/cuda USE_CUDNN=1 USE_DIST_KVSTORE=1 \
    && cd python \
    && pip install -e . 



WORKDIR /workspace
RUN chmod -R a+w /workspace

