# Docker Theory

## What is Docker?
Docker is an open-source platform that automates the deployment, scaling, and management of applications using containerization. Containers allow developers to package an application with all its dependencies into a standardized unit for software development.

## Key Concepts

### Container
A container is a lightweight, standalone, and executable package that includes everything needed to run a piece of software, including the code, runtime, system tools, libraries, and settings.

### Image
An image is a read-only template used to create containers. Images are built from a set of instructions written in a Dockerfile.

### Dockerfile
A Dockerfile is a text file that contains a series of instructions on how to build a Docker image. It specifies the base image, application code, dependencies, and other configurations.

### Docker Hub
Docker Hub is a cloud-based repository where Docker users can create, test, store, and distribute container images.

### Volume
A volume is a persistent storage mechanism for Docker containers. It allows data to be stored and shared among containers.

## Common Commands

- `docker run`: Run a container from an image.
- `docker build`: Build an image from a Dockerfile.
- `docker pull`: Download an image from a repository.
- `docker push`: Upload an image to a repository.
- `docker ps`: List running containers.
- `docker stop`: Stop a running container.
- `docker rm`: Remove a container.
- `docker rmi`: Remove an image.

## Frequently Asked Questions

### What are the benefits of using Docker?
- **Portability**: Docker containers can run on any system that supports Docker, ensuring consistent environments across development, testing, and production.
- **Scalability**: Docker makes it easy to scale applications horizontally by adding more containers.
- **Isolation**: Containers provide process and resource isolation, ensuring that applications run independently without interference.
- **Efficiency**: Containers are lightweight and share the host system's kernel, making them more efficient than traditional virtual machines.

### How does Docker differ from virtual machines?
Docker containers share the host system's kernel and are more lightweight compared to virtual machines, which include a full operating system. This makes containers faster to start and use fewer resources.

### What is Docker Compose?
Docker Compose is a tool for defining and running multi-container Docker applications. It uses a YAML file to configure the application's services, networks, and volumes.

### How do you create a Dockerfile?
A Dockerfile is created by writing a series of instructions in a text file. Each instruction specifies a step in building the image, such as setting the base image, copying files, installing dependencies, and running commands.

Example Dockerfile:
```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

## Docker Layered Architecture

Docker uses a layered architecture to build and run container images. Each layer represents a set of filesystem changes, and they are stacked on top of each other to form the final image. This architecture provides several benefits, including reusability, efficiency, and ease of management.

### Layers

1. **Base Layer**: The base layer is the starting point of a Docker image, typically an operating system like Ubuntu or Alpine.
2. **Intermediate Layers**: These layers include changes made to the base layer, such as installing software packages, copying files, or setting environment variables.
3. **Top Layer**: The top layer is the final layer that contains the application code and any last-minute configurations.

### Benefits of Layered Architecture

- **Reusability**: Layers can be reused across different images, reducing redundancy and saving storage space.
- **Efficiency**: Only the layers that have changed need to be updated or transferred, making image builds and deployments faster.
- **Version Control**: Each layer can be versioned and managed independently, allowing for better control over changes and updates.

### Example of Layered Architecture in a Dockerfile

```Dockerfile
# Base layer
FROM ubuntu:20.04

# Intermediate layer: Install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Intermediate layer: Set working directory
WORKDIR /app

# Intermediate layer: Copy application code
COPY . /app

# Intermediate layer: Install Python packages
RUN pip3 install -r requirements.txt

# Top layer: Set environment variable and expose port
ENV FLASK_APP=app.py
EXPOSE 5000

# Top layer: Define the command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
```

### Does Docker update the same image every time it is created or generate a new image?

When you build a Docker image using a Dockerfile, Docker generates a new image every time. Each build creates a new image with a unique ID, even if the Dockerfile has not changed. This ensures that you have a consistent and immutable image for each build. If you want to update an existing image, you need to build a new image and tag it appropriately.

### How does Docker use or reuse layered architecture if it creates the image every time?

Docker uses a layered architecture to optimize the build process and reuse layers whenever possible. When you build a Docker image, Docker checks its cache to see if any existing layers can be reused. If a layer has not changed since the last build, Docker will reuse that layer instead of creating a new one. This caching mechanism significantly speeds up the build process and reduces the amount of data that needs to be transferred.

For example, if you have a Dockerfile with multiple layers and only the top layer changes, Docker will reuse all the previous layers and only rebuild the top layer. This means that dependencies and base images that have not changed will not be reinstalled or recreated, saving time and resources.

By leveraging the layered architecture and caching, Docker ensures efficient image builds and minimizes redundancy, even though each build generates a new image with a unique ID.

For example, consider the following Dockerfile:

```Dockerfile

# Use a base image
FROM python:3.9

# Install dependencies
RUN pip install flask

# Copy application code
COPY . /app

# Set the working directory
WORKDIR /app

# Run the application
CMD ["python", "app.py"]
```

Docker uses a layered architecture to optimize the build process and reuse layers whenever possible. Here's a more detailed explanation:

When you build a Docker image, Docker processes the instructions in the Dockerfile step by step. Each instruction creates a new layer. Docker caches these layers, so if a layer has not changed between builds, Docker can reuse the cached layer instead of rebuilding it. This makes the build process faster and more efficient.

For example, consider the following Dockerfile:

```Dockerfile
# Use a base image
FROM python:3.9

# Install dependencies
RUN pip install flask

# Copy application code
COPY . /app

# Set the working directory
WORKDIR /app

# Run the application
CMD ["python", "app.py"]
```

If you build this Dockerfile, Docker will create layers for each instruction:

1. The `FROM` instruction creates a layer from the `python:3.9` base image.
2. The `RUN` instruction creates a layer with Flask installed.
3. The `COPY` instruction creates a layer with the application code.
4. The `WORKDIR` and `CMD` instructions create layers for setting the working directory and running the application.

If you make changes to the application code and rebuild the image, Docker will reuse the cached layers for the `FROM` and `RUN` instructions, since they have not changed. Only the `COPY`, `WORKDIR`, and `CMD` layers will be rebuilt.

This layered architecture allows Docker to efficiently manage dependencies and base images, even though each build generates a new image with a unique ID.

Would you like to see an example of how Docker caches layers in practice?

**Since Docker uses layered architecture it is best practice to first copy the requirements file only, that command thus becomes a mid layer.**

How this helps: Docker everytime checks which layer has changed and rebuilds all the layers after and including the changed layer. Since requirements.txt doesn't changes frequently hence it is a good practice to copy it first and install it. This will create this as a mid level layer and won't require downloading and installing packages everytime the image is rebuild. 

### How is an image different from a container?

An image is a read-only template that defines the contents and configuration of a container. It includes the application code, runtime, libraries, environment variables, and other dependencies needed to run the application. Images are built from a set of instructions in a Dockerfile and can be stored in repositories like Docker Hub.

A container, on the other hand, is a runtime instance of an image. It is a lightweight, standalone, and executable package that includes everything needed to run the application. Containers are created from images and can be started, stopped, moved, and deleted. They provide an isolated environment for the application to run, ensuring consistency across different environments.

In summary, an image is a blueprint for creating containers, while a container is a running instance of an image.

### Does a container also copy the same content which images have? Are containers separate entities and can they run without an image or are they dependent on an image?

A container does not copy the content of an image; instead, it uses the image as a read-only template. When a container is created, a writable layer is added on top of the image's read-only layers. This writable layer allows the container to make changes to files and directories without affecting the underlying image.

Containers are not separate entities and cannot run without an image. They are dependent on an image to provide the necessary files, libraries, and configuration needed to run the application. The image serves as the foundation for the container, and the container adds a layer of isolation and runtime execution on top of it.

In summary, containers rely on images to function and cannot operate independently without them.