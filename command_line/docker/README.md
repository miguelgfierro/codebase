# Docker basic commands

List of Docker basic commands. More info can be found [here](https://docs.docker.com/engine/reference/commandline/docker/).

```bash
sudo docker build -t my_image_name . -> Build the image my_image_name using the Dockerfile of the current location
sudo docker run -it my_image_name bash -> Run the docker image and enter the bash
sudo nvidia-docker run -it my_image_name bash -> Run the docker image and enter the bash with NVIDIA drivers support
sudo docker run -p 8888:8888 -it my_image_name bash -> Run the image redirecting a port (useful for jupyter support)
sudo docker run -p 8888:8888 -v $HOME:/mnt/home -it my_image_name bash -> Run the image redirecting a port and making your local home accessible
sudo docker images -> list the images available
sudo docker ps -> list the images currently running
sudo docker stop my_image_id -> Stop the image using its ID (the ID can be found with docker ps)
sudo docker stop $(docker ps -q --filter ancestor=<image-name> ) -> Stop the image by its name
```
## Upload image to DockerHub

```bash
sudo docker login --username=hoaphumanoid 
sudo docker images
```
You will get a list of your images:

```bash
REPOSITORY                                 TAG                            IMAGE ID            CREATED             SIZE
cuda_ubuntu_base                           latest                         f161297fd883        9 minutes ago       4.22GB
nvidia/cuda                                8.0-cudnn7-devel-ubuntu16.04   0c17239b6723        13 days ago         2.09GB
azureml_25f82d93633330a2a06f0a73fb43bb0a   latest                         fd02e6d814fa        8 weeks ago         7.04GB
azureml_d03b8bc55f6f6aae78794809bd9c4cdd   latest                         4f95489c8626        2 months ago        3.8GB
microsoft/mmlspark                         plus-0.9.9                     7d6dc0293c47        6 months ago        1.58GB
```

Now you can tag your image:

```bash
sudo docker tag f161297fd883 hoaphumanoid/cuda_ubuntu_base:cuda8-cudnn7-ubuntu16.04
```

Then push your image to the repository you created:

```bash
sudo docker push hoaphumanoid/cuda_ubuntu_base
```



