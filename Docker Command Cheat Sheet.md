
**Start Docker engine:** 

`sudo systemctl start docker`

**Check Docker status**:

`sudo systemctl status docker`

**Enable Docker to start on boot:**

`sudo systemctl enable docker`

**Stop Docker**:

`sudo systemctl stop docker`

**Disable Docker from starting on boot:**

`sudo systemctl disable docker`

**List All Docker Containers:**

`docker ps -a`

**List Running Docker Containers:**

`docker ps`

**Remove Containers:**

`docker rm <container_name>`
you can get the container name from the `docker ps -a` command. 

**Remove Images:**
for removing images you will have to first remove any container attached to it. 

`docker rmi <image_name>`

**Run Docker and expose to a particular port**

`docker run -p <port>:<port> <image_name>`

example: `docker run -p 5000:5000 <image_name>`
where '-p' is being used to publish the containers port to host port. it maps a port on host machine to port on the docker machine allowing access to container service from host. 

**Stop a Docker Container**

`docker stop <container_id>`


**Start a Docker Container and Interact with its Terminal:**

`docker run -it <image_name> /bin/bash`

The `-it` flag allows you to open an interactive terminal inside the container.


**Attach to a Running Docker Container's Terminal:**

`docker exec -it <container_id> /bin/bash`

The `exec` command allows you to run commands in a running container. The `-it` flag opens an interactive terminal inside the container.
