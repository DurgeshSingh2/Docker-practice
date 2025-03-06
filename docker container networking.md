# Container Networking and Interaction with Host/Web

## Host.docker.internal

`host.docker.internal` is a special DNS name that resolves to the internal IP address used by the host. This is particularly useful when you need to access services running on the host machine from within a Docker container.

### Use Case

One common use case for `host.docker.internal` is when you have a development environment where some services are running on your local machine, and you want to connect to these services from within a Docker container. For example, you might have a database running on your host machine and a web application running inside a Docker container that needs to connect to this database.

#### Example

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

#### Notes

- `host.docker.internal` is supported on Docker for Mac, Docker for Windows, and Docker Desktop for Linux.
- This feature is not available in native Linux installations of Docker.

