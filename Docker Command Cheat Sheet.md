
**Start Docker engine:** 

`sudo systemctl start docker`

**Check Docker status**:

`sudo systemctl status docker`

**Enable Docker to start on boot:**

`sudo systemctl enable docker

**Stop Docker**:

`sudo systemctl stop docker

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
