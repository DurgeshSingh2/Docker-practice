# Container Networking:

## Conneting With LocalHost:

**Scenario:** My application containing two api's GET and POST are running in a docker container and they want to intereact with a DB that is hosted locally and not on a container

### Host.docker.internal

`host.docker.internal` is a special DNS name that resolves to the internal IP address used by the host. This is particularly useful when you need to access services running on the host machine from within a Docker container.

#### Use Case

One common use case for `host.docker.internal` is when you have a development environment where some services are running on your local machine, and you want to connect to these services from within a Docker container. For example, you might have a database running on your host machine and a web application running inside a Docker container that needs to connect to this database.

##### Example

Here is an example of how you can use `host.docker.internal` to connect to a postgresql database running on your host machine from a Docker container:

1. Start the postgresql database on your host machine.

2. Run your Docker container and use `host.docker.internal` as the hostname for the database connection.

```dockerfile
FROM python:3.11

WORKDIR /app

# environment variable
ENV postgre_connect="host.docker.internal"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 3000

CMD [ "python3", "pytodb_con.py"]
```

In your web application configuration, you would use `host.docker.internal` as the database host:

```python
def connect_db():
    global conn
    try:
        conn = psycopg2.connect(
            host=postgre_connect,
            database="postgres",
            user="durgeshsingh",
            port="5432",
        )
        print("Database connection successful")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
```

This setup allows your web application running inside the Docker container to connect to the postgresql database running on your host machine.

##### Notes

- `host.docker.internal` is supported on Docker for Mac, Docker for Windows, and Docker Desktop for Linux.
- This feature is not available in native Linux installations of Docker.

## Container to Container connection: 

Scenario: My postgresDB is running on container1 and my application is running on container2. For having a connection between these 
two containers i can use the hardcoded approach or the container networking solution. 

### Hardcoded approach

In this approach we provide the hardcoded IP address of container running db to the container running python code and trying to connect. 

**Step1:**

Download and run postgresdb on a container using the following command. 

```shell

docker run -d \                     
  -v '/Users/developer/Desktop/developer workspace/Docker-Db-Volume':/app/db \
  -e POSTGRES_PASSWORD=admin \
  --name postgresdb \
  -p 5432:5432 \
  postgres
```

Above command explained: 
*   ```docker run -d``` : is responsible for running the container in detached mode. 
*   ```-v '/Users/developer/Desktop/developer workspace/Docker-Db-Volume':/app/db \```: This portion of command specifies that we are binding a known volume to the container for easy monitoring. we can use named volume or provide any other known volume from your local system.
*   ```-e POSTGRES_PASSWORD=admin \```: providing/setting up password for the postgresdb. 
*   ```--name postgresdb \```: naming the container to postgresdb ( we can name it anything)
*   ```-p 5432:5432 \```: exposing the db running on port 5432 of container to port 5432 of localhost machine
*   ```postgres```: name of the image, postgres based on which the container will be running. 

Running this command will set and run the container on which postgresdb is running. 

Now we will have to find the IP address of the container which then will be provided in the python code to make the connection and to that we will simply use the command. 

```shell
docker inspect <container_name/id>
```

and will try to locate the ip adress under the section 

```json

"NetworkSettings": {
            "Bridge": "",
            "SandboxID": "9be1aa553203d623285a659c753c2c73bad4d975ebb3a313882a961172523cd0",
            "SandboxKey": "/var/run/docker/netns/9be1zz553203",
            "Ports": {
                "5432/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "5433"
                    }
                ]
            },
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "ddb578d3de710122e1fa520026df56f80ad6bf95b1baa343946c0453fcecdc1e27",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "08:21:zc:21:01:03",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "MacAddress": "08:21:zc:21:01:03",
                    "DriverOpts": null,
                    "NetworkID": "1238bff3ca23462a59d633fc7506585ea8249d5a19e9a718d3e60d69b0ffb972",
                    "EndpointID": "ddb578d3de907731fa520026df56f80ad6bf95b1baa343946c0453fcecdc1e27",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        }
```

This will give us the ip address "172.17.0.2" might be different for different at your local system. We will use this IP address and put it as an environment variable in the dockerfile. Then will pass this environment variable in python to connect to db. 

```DOCKERFILE

FROM python:3.11

WORKDIR /app

# environment variable
ENV postgre_connect="172.17.0.2"
ENV postgre_user="postgres"
ENV postgre_password="admin"

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 3000

CMD [ "python3", "pytodb_con.py"]

```

**Python Code:**

```python 

def connect_db():
    global conn
    try:
        conn = psycopg2.connect(
            host=postgre_connect,
            #host="host.docker.internal", using this we will be able to connect to postgressql running on local machine 
            # whereas we are providing ip of docker container and trying to connect to db running in a container
            database="postgres",
            password="admin",
            user="postgres",
            port="5432",
        )
        print("Database connection successful")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

```
This will connect the db to the python code. 

## Creating Container Network