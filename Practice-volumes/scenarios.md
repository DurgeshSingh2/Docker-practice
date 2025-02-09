## Docker Volume Scenarios

### 1. Create Anonymous Volume; Do Not Auto-Remove Container

**Command:** `docker run -it --name prac-vol prac-vol`

1. Start the container.
    - A new volume is created.
2. If not existing, create a file and write the number 1 to it.
    - File is created if not existing.
3. Read from the file if existing.
    - File is read and value incremented in it.
4. Stop the container.
    - Container is stopped and volume exists.
5. Start/restart the container and see if the file still contains number 1. If yes, increment the existing number by 1 and write it to the file.
    - Done.
6. Remove the container.
    - Done.
7. Check if the volume has been removed or not.
    - Volume still exists.
8. Create a new container and try to read the file from the already created container.
    - A new volume is created for each new container.

### 2. Create Anonymous Volume; Auto-Remove Container

**Command:** `docker run -it --rm --name prac-vol prac-vol`

1. Start the container.
    - A new volume is created.
2. If not existing, create a file and write the number 1 to it.
    - File is created if not existing.
3. Read from the file if existing.
    - File is read and value incremented in it.
4. Check if the volume exists.
    - Yes, volume is existing while the container is running.
5. Check if the volume exists after the container is automatically stopped.
    - Container is stopped and volume doesn't exist anymore.

### 3. Create Named Volume; Share the File Between Two Containers

**Commands:**
- `docker run -it -v prac-vol:/app/data --name prac-vol1 prac-vol1`
- `docker run -it -v prac-vol:/app/data --name prac-vol2 prac-vol2`

1. Start container1. It should write the file with value as 1 in a .txt file.
    - A new volume is created since the volume didn't exist before.
2. Start container2.
    - Container2 is started.
3. Share the file between both containers and increment the number in the file whenever the container runs.
    - Containers are incrementing the same file all the time.

### 4. Create Named Volume; create container with auto-remove command:

**Commands:**
- `docker run -it -rm -v prac-vol:/app/data --name prac-vol1 prac-vol1`
- `docker run -it -rm -v prac-vol:/app/data --name prac-vol2 prac-vol2`

1. Start container1. It should write the file with value as 1 in a .txt file.
    - A new volume is created since the volume didn't exist before.
    - container should get stopped once its task has been completed.
2. Start container2.
    - Container2 is started.
    - container should share the same file and increment number into the same file.
3. Share the file between both containers and increment the number in the file whenever the container runs.
    - Containers are incrementing the same file all the time.
4. Volume should not be automatically deleted. 
    - volume is not automatically deleted. 