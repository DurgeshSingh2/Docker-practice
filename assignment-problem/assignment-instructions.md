Dockerize BOTH apps - the Python and the Node app.

1) Create appropriate images for both apps (two separate images!).
HINT: Have a brief look at the app code to configure your images correctly!

*server.js :*

``` 
    docker build . .
```

*bmi.py*

``` 
    docker build . . 
    docker run -it --rm python_assign
```

2) Launch a container for each created image, making sure, 
that the app inside the container works correctly and is usable.

*server.js*

```
    docker run -d --rm -p 3000:3000 node_assign
```
*bmi.py*

```
   docker run -it --rm python_assign 
```

3) Re-create both containers and assign names to both containers. Use these names to stop and restart both containers.

```
    docker run -d --rm -p 3000:3000 -name node_assign node_assign
```
*bmi.py*

```
   docker run -it --rm -name python_assign python_assign 
```

4) Clean up (remove) all stopped (and running) containers, 
clean up all created images.

*server.js*

```
    docker stop node_assign
    docker rm node_assign
    docker rmi node_assign
```

*bmi.py*

```
    docker stop python_assign
    docker rm python_assign
    docker rmi python_assign
```

5) Re-build the images - this time with names and tags assigned to them.

*server.js*

```
    docker build -t node_assign:v1
```

*bmi.py*
```
    docker build -t python:assign:v1
```

6) Run new containers based on the re-built images, ensuring that the containers
are removed automatically when stopped.

*server.js*

```
    docker run --rm -p 3000:3000 --name node_assign node_assign:v1
```

*bmi.py*

```
    docker run -it --rm --name python_assign python_assign:v1
```