# base image of docker file: based on python
FROM python:3 

# set the working directory in the container as a standard we set it to /app
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# RUN shell commands
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt

# copy the current directory contents into the container at /app
COPY . .

# make port 5000 available to the world outside this container so that 
# we can access it on the browser. 
EXPOSE 5000

# run the command to start the app. BaSically, this is the command that will be run when the container starts
CMD ["python3", "getdata.py"]   
