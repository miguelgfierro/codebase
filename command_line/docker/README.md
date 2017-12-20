# Docker basic commands

List of Docker basic commands. More info can be found [here](https://docs.docker.com/engine/reference/commandline/docker/).

```bash
    docker build -t my_image_name . -> Build the image my_image_name using the Dockerfile of the current location
    docker run -it my_image_name bash -> Run the docker image and enter the bash
    nvidia-docker run -it my_image_name bash -> Run the docker image and enter the bash with NVIDIA drivers support
    docker run -p 8888:8888 -it my_image_name bash -> Run the image redirecting a port (useful for jupyter support)
    docker run -p 8888:8888 -v $HOME:/mnt/home -it my_image_name bash -> Run the image redirecting a port and making your local home accessible
    docker images -> list the images available
    docker ps -> list the images currently running
    docker stop my_image_id -> Stop the image using its ID (the ID can be found with docker ps)
    docker stop $(docker ps -q --filter ancestor=<image-name> ) -> Stop the image by its name
```
