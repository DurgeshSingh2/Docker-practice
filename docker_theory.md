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

## How is an image different from a container?

An image is a read-only template that defines the contents and configuration of a container. It includes the application code, runtime, libraries, environment variables, and other dependencies needed to run the application. Images are built from a set of instructions in a Dockerfile and can be stored in repositories like Docker Hub.

A container, on the other hand, is a runtime instance of an image. It is a lightweight, standalone, and executable package that includes everything needed to run the application. Containers are created from images and can be started, stopped, moved, and deleted. They provide an isolated environment for the application to run, ensuring consistency across different environments.

In summary, an image is a blueprint for creating containers, while a container is a running instance of an image.

## Does a container also copy the same content which images have? Are containers separate entities and can they run without an image or are they dependent on an image?

A container does not copy the content of an image; instead, it uses the image as a read-only template. When a container is created, a writable layer is added on top of the image's read-only layers. This writable layer allows the container to make changes to files and directories without affecting the underlying image.

Containers are not separate entities and cannot run without an image. They are dependent on an image to provide the necessary files, libraries, and configuration needed to run the application. The image serves as the foundation for the container, and the container adds a layer of isolation and runtime execution on top of it.

In summary, containers rely on images to function and cannot operate independently without them. 

## How to Add a Name to an Image and a Container

### Naming an Image

When you build a Docker image, you can tag it with a name using the `-t` flag with the `docker build` command. This makes it easier to reference and manage the image.

#### Usage

```sh
docker build -t <image_name>:<tag> <path_to_dockerfile>
```

#### Example

```sh
docker build -t myapp:latest .
```

In this example, the image is named `myapp` with the tag `latest`.

### Naming a Container

When you run a Docker container, you can assign it a name using the `--name` flag with the `docker run` command. This makes it easier to manage and reference the container.

#### Usage

```sh
docker run --name <container_name> <image_name>
```

#### Example

```sh
docker run --name mycontainer myapp:latest
```

In this example, the container is named `mycontainer` and is created from the `myapp:latest` image.

By naming your images and containers, you can simplify their management and improve the clarity of your Docker environment.

## Why Should We Tag an Image and What is the Purpose of It?

Tagging a Docker image is an important practice that helps in managing and organizing images effectively. A tag is a label that is assigned to an image to identify its version or variant. Here are some reasons why you should tag an image and the purpose of it:

### Version Control
Tagging allows you to version your images, making it easier to track changes and updates. For example, you can tag an image with `v1.0`, `v1.1`, etc., to indicate different versions of your application.

### Environment Differentiation
Tags can be used to differentiate images for different environments, such as development, staging, and production. For example, you can tag images with `dev`, `staging`, and `prod` to indicate their intended environment.

### Rollback Capability
By tagging images, you can easily roll back to a previous version if something goes wrong with the current version. This provides a safety net and ensures that you can quickly revert to a stable state.

### Clarity and Readability
Tags make it easier to understand the purpose and state of an image at a glance. Instead of dealing with long and complex image IDs, you can use meaningful tags to identify images.

### Automation and CI/CD
Tags are essential for automation and continuous integration/continuous deployment (CI/CD) pipelines. They allow you to specify which image version should be deployed, tested, or promoted to the next stage in the pipeline.

### Example of Tagging an Image
To tag an image, you use the `-t` flag with the `docker build` command:

```sh
docker build -t myapp:v1.0 .
```

In this example, the image is tagged with `v1.0`, making it easy to reference and manage.

### Conclusion
Tagging Docker images is a best practice that enhances version control, environment differentiation, rollback capability, clarity, and automation. By using tags, you can efficiently manage your Docker images and ensure a smooth workflow in your development and deployment processes.

## What is an Attached and Detached Container?

In Docker, containers can run in two modes: attached and detached.

### Attached Mode
When a container runs in attached mode, it is connected to the terminal session that started it. This means you can see the container's output (stdout and stderr) and interact with it directly. By default, Docker runs containers in attached mode.

To run a container in attached mode, you simply use the `docker run` command without any additional flags:
```sh
docker run <image_name>
```

### Detached Mode
When a container runs in detached mode, it runs in the background and is not connected to the terminal session. This allows you to continue using the terminal for other tasks while the container runs independently.

To run a container in detached mode, you use the `-d` flag with the `docker run` command:
```sh
docker run -d <image_name>
```

## How to Attach or Detach a Container

### Attaching to a Running Container
If you have a container running in detached mode and you want to attach to it, you can use the `docker attach` command followed by the container ID or name:
```sh
docker attach <container_id_or_name>
```
This will connect your terminal to the container's output and allow you to interact with it.

### Detaching from a Running Container
If you are attached to a container and want to detach from it without stopping the container, you can use the `Ctrl + P` followed by `Ctrl + Q` key sequence. This will detach your terminal from the container while leaving the container running in the background.

Alternatively, you can start a container in detached mode from the beginning using the `-d` flag as mentioned earlier.

By understanding and using attached and detached modes, you can manage your Docker containers more effectively based on your needs.

## What is the difference between `docker start` and `docker run` command?

The `docker start` and `docker run` commands are used to start containers, but they serve different purposes and are used in different scenarios.

### `docker run`
The `docker run` command creates and starts a new container from an image. It is used when you want to create a new container instance. The command performs the following steps:
1. Creates a new container from the specified image.
2. Allocates a filesystem and mounts a read-write layer.
3. Sets up the network (if specified).
4. Sets up container configurations (e.g., environment variables, volumes).
5. Executes the specified command.
6. Starts the container in by default attached setting.

Example:
```sh
docker run -d --name my_container nginx
```

### `docker start`
The `docker start` command is used to start an existing, stopped container. It does not create a new container but starts one that was previously created and stopped. This command is useful for restarting containers without creating new instances.

It Starts the container in by Default detached setting. 

Example: default way to start the container
```sh
docker start my_container
```

Example: Start the container in attached mode. 
```sh
docker start -a my_container
```

In summary, `docker run` is used to create and start a new container, while `docker start` is used to start an existing, stopped container.

## Docker Logs

The `docker logs` command is used to fetch the logs of a container. This command is useful for debugging and monitoring the output of your applications running inside containers.

### Usage

To view the logs of a running or stopped container, use the following command:
```sh
docker logs <container_id_or_name>
```

### Options

- `-f` or `--follow`: Stream the logs in real-time. This is also a way to attach a container. 
- `--tail`: Show only the last N lines of the logs.
- `-t` or `--timestamps`: Show timestamps in the logs.

Example:
```sh
docker logs -f --tail 100 <container_id_or_name>
```

This command will stream the last 100 lines of the container's logs in real-time.

## What is Docker Prune Command?

The `docker prune` command is used to remove unused Docker objects, such as containers, images, volumes, and networks. This command helps to free up disk space by cleaning up resources that are no longer in use.

### Usage

To remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes, you can use the following command:
```sh
docker system prune
```

### Options

- `-a` or `--all`: Remove all unused images, not just dangling ones.
- `--volumes`: Remove all unused volumes in addition to containers, networks, and images.
- `-f` or `--force`: Do not prompt for confirmation before pruning.

Example:
```sh
docker system prune -a --volumes
```

### Advantages

- **Disk Space Management**: Frees up disk space by removing unused Docker objects.
- **Clean Environment**: Helps maintain a clean and organized Docker environment by removing unnecessary resources.
- **Performance**: Improves Docker performance by reducing the number of unused objects that Docker has to manage.

### Disadvantages

- **Data Loss**: Can lead to accidental data loss if important containers, images, or volumes are removed unintentionally.
- **Irreversible**: Once objects are pruned, they cannot be recovered.
- **Time-Consuming**: Pruning large amounts of data can be time-consuming, especially if there are many unused objects.

In summary, the `docker prune` command is a powerful tool for managing disk space and maintaining a clean Docker environment. However, it should be used with caution to avoid accidental data loss.

## How can we automatically remove a container when it exits?

To automatically remove a container when it exits, you can use the `--rm` flag with the `docker run` command. This flag ensures that the container is removed as soon as it stops running, freeing up resources and keeping your Docker environment clean.

### Usage

```sh
docker run --rm <image_name>
```

### Example

```sh
docker run --rm ubuntu echo "This container will be removed after it exits"
```

In this example, the container will be automatically removed after it finishes executing the `echo` command.

Using the `--rm` flag is particularly useful for short-lived containers and one-off tasks where you don't need to keep the container after it has completed its job.

## Inspecting Docker Images

To inspect a Docker image, you can use the `docker inspect` command. This command provides detailed information about the image, including its configuration, layers, environment variables, and more.

### Usage

```sh
docker inspect <image_name_or_id>
```

### Example

```sh
docker inspect nginx
```

This command will output a JSON object containing detailed information about the `nginx` image.

### Key Information Provided

- **ID**: The unique identifier of the image.
- **RepoTags**: The repository name and tag of the image.
- **Created**: The creation date and time of the image.
- **Size**: The size of the image.
- **Layers**: The layers that make up the image.
- **Config**: The configuration of the image, including environment variables, entrypoint, and exposed ports.

### Use Cases

- **Debugging**: Inspecting an image can help you understand its configuration and troubleshoot issues.
- **Verification**: You can verify the contents and settings of an image before using it in production.
- **Documentation**: The detailed information provided by `docker inspect` can be used for documentation purposes.

By using the `docker inspect` command, you can gain a comprehensive understanding of your Docker images and ensure they are configured correctly.

## Docker `cp` Command

The `docker cp` command is used to copy files or directories between a container and the local filesystem. This command is useful for transferring data into or out of a container without needing to rebuild the image or restart the container.

### Usage

To copy files from the local filesystem to a container:
```sh
docker cp <source_path> <container_id>:<destination_path>
```

To copy files from a container to the local filesystem:
```sh
docker cp <container_id>:<source_path> <destination_path>
```

### Example

Copy a file from the local filesystem to a container:
```sh
docker cp /path/to/local/file.txt my_container:/path/to/container/directory/
```

Copy a file from a container to the local filesystem:
```sh
docker cp my_container:/path/to/container/file.txt /path/to/local/directory/
```

### Use Cases

- **Debugging**: Copy log files or configuration files from a container to the local filesystem for analysis and debugging.
- **Data Transfer**: Transfer data files into a container for processing or copy processed data out of a container.
- **Backup and Restore**: Backup important files from a container or restore files into a container.

### Real Project Example

In a real project, you might have a container running a web application that generates log files. To analyze these logs, you can copy them from the container to your local machine:

```sh
docker cp web_app_container:/var/log/web_app.log /local/path/to/logs/
```

Similarly, if you need to update a configuration file in the container without rebuilding the image, you can copy the updated file into the container:

```sh
docker cp /local/path/to/config.yaml web_app_container:/app/config/
```

By using the `docker cp` command, you can efficiently manage files and data between your local environment and Docker containers, making it easier to handle various tasks and scenarios.