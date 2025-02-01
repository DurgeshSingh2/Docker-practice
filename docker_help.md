# Docker Help

## Docker --help

To get help on Docker commands, you can use the `docker --help` command. This will display a list of available commands and their descriptions.

```sh
docker --help
```

Output:

```
Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
  --config string      Location of client config files (default "/root/.docker")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level (debug, info, warn, error, fatal) (default "info")
  --tls                Use TLS; implied by --tlsverify
  --tlscacert string   Trust certs signed only by this CA (default "/root/.docker/ca.pem")
  --tlscert string     Path to TLS certificate file (default "/root/.docker/cert.pem")
  --tlskey string      Path to TLS key file (default "/root/.docker/key.pem")
  --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.
```

## Frequently Used Docker Commands

### docker run --help

```sh
docker run --help
```

Output:

```
Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container

Options:
  -d, --detach                         Run container in background and print container ID
  -i, --interactive                    Keep STDIN open even if not attached
  -t, --tty                            Allocate a pseudo-TTY
  -u, --user string                    Username or UID (format: <name|uid>[:<group|gid>])
  -v, --volume list                    Bind mount a volume
  --rm                                 Automatically remove the container when it exits
  --name string                        Assign a name to the container
  --network string                     Connect a container to a network
  --env list                           Set environment variables
  --label list                         Set metadata on container
  --restart string                     Restart policy to apply when a container exits (default "no")
  --cpus decimal                       Number of CPUs
  --memory string                      Memory limit
```

### docker ps --help

```sh
docker ps --help
```

Output:

```
Usage:  docker ps [OPTIONS]

List containers

Options:
  -a, --all             Show all containers (default shows just running)
  -f, --filter filter   Filter output based on conditions provided
  --format string       Pretty-print containers using a Go template
  -n, --last int        Show n last created containers (includes all states)
  -q, --quiet           Only display container IDs
  -s, --size            Display total file sizes
```

### docker images --help

```sh
docker images --help
```

Output:

```
Usage:  docker images [OPTIONS] [REPOSITORY[:TAG]]

List images

Options:
  -a, --all             Show all images (default hides intermediate images)
  --digests             Show digests
  -f, --filter filter   Filter output based on conditions provided
  --format string       Pretty-print images using a Go template
  --no-trunc            Don't truncate output
  -q, --quiet           Only show numeric IDs
```

### docker logs --help

```sh
docker logs --help
```

Output:

```
Usage:  docker logs [OPTIONS] CONTAINER

Fetch the logs of a container

Options:
  --details        Show extra details provided to logs
  -f, --follow     Follow log output
  --since string   Show logs since timestamp
  --tail string    Number of lines to show from the end of the logs (default "all")
  -t, --timestamps Show timestamps
  --until string   Show logs before a timestamp
```

### docker exec --help

```sh
docker exec --help
```

Output:

```
Usage:  docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

Run a command in a running container

Options:
  -d, --detach               Run command in the background
  -i, --interactive          Keep STDIN open even if not attached
  --privileged               Give extended privileges to the command
  -t, --tty                  Allocate a pseudo-TTY
  -u, --user string          Username or UID (format: <name|uid>[:<group|gid>])
  --workdir string           Working directory inside the container
```

### docker build --help

```sh
docker build --help
```

Output:

```
Usage:  docker build [OPTIONS] PATH | URL | -

Build an image from a Dockerfile

Options:
  --build-arg list           Set build-time variables
  --cache-from list          Images to consider as cache sources
  --file string              Name of the Dockerfile (default is 'PATH/Dockerfile')
  --label list               Set metadata for an image
  --no-cache                 Do not use cache when building the image
  --pull                     Always attempt to pull a newer version of the image
  -q, --quiet                Suppress the build output and print image ID on success
  --rm                       Remove intermediate containers after a successful build (default true)
  --tag list                 Name and optionally a tag in the 'name:tag' format
```

### docker pull --help

```sh
docker pull --help
```

Output:

```
Usage:  docker pull [OPTIONS] NAME[:TAG|@DIGEST]

Pull an image or a repository from a registry

Options:
  -a, --all-tags                Download all tagged images in the repository
  --disable-content-trust       Skip image verification (default true)
```

### docker push --help

```sh
docker push --help
```

Output:

```
Usage:  docker push [OPTIONS] NAME[:TAG]

Push an image or a repository to a registry

Options:
  --disable-content-trust       Skip image signing (default true)
```

### docker start --help

```sh
docker start --help
```

Output:

```
Usage:  docker start [OPTIONS] CONTAINER [CONTAINER...]

Start one or more stopped containers

Options:
  -a, --attach      Attach STDOUT/STDERR and forward signals
  -i, --interactive Keep STDIN open even if not attached
```Start a build

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Start a build

Aliases:
  docker build, docker builder build, docker image build, docker buildx b

Options:
      --add-host strings              Add a custom host-to-IP mapping (format: "host:ip")
      --allow strings                 Allow extra privileged entitlement (e.g., "network.host", "security.insecure")
      --annotation stringArray        Add annotation to the image
      --attest stringArray            Attestation parameters (format: "type=sbom,generator=image")
      --build-arg stringArray         Set build-time variables
      --build-context stringArray     Additional build contexts (e.g., name=path)
      --builder string                Override the configured builder instance (default "desktop-linux")
      --cache-from stringArray        External cache sources (e.g., "user/app:cache", "type=local,src=path/to/dir")
      --cache-to stringArray          Cache export destinations (e.g., "user/app:cache", "type=local,dest=path/to/dir")
      --call string                   Set method for evaluating build ("check", "outline", "targets") (default "build")
      --cgroup-parent string          Set the parent cgroup for the "RUN" instructions during build
      --check                         Shorthand for "--call=check" (default )
  -D, --debug                         Enable debug logging
  -f, --file string                   Name of the Dockerfile (default: "PATH/Dockerfile")
      --iidfile string                Write the image ID to a file
      --label stringArray             Set metadata for an image
      --load                          Shorthand for "--output=type=docker"
      --metadata-file string          Write build result metadata to a file
      --network string                Set the networking mode for the "RUN" instructions during build (default "default")
      --no-cache                      Do not use cache when building the image
      --no-cache-filter stringArray   Do not cache specified stages
  -o, --output stringArray            Output destination (format: "type=local,dest=path")
      --platform stringArray          Set target platform for build
      --progress string               Set type of progress output ("auto", "plain", "tty", "rawjson"). Use plain to show container
                                      output (default "auto")
      --provenance string             Shorthand for "--attest=type=provenance"
      --pull                          Always attempt to pull all referenced images
      --push                          Shorthand for "--output=type=registry"
  -q, --quiet                         Suppress the build output and print image ID on success
      --sbom string                   Shorthand for "--attest=type=sbom"
      --secret stringArray            Secret to expose to the build (format: "id=mysecret[,src=/local/secret]")
      --shm-size bytes                Shared memory size for build containers
      --ssh stringArray               SSH agent socket or keys to expose to the build (format: "default|<id>[=<socket>|<key>[,<key>]]")
  -t, --tag stringArray               Name and optionally a tag (format: "name:tag")
      --target string                 Set the target build stage to build
      --ulimit ulimit                 Ulimit options (default [])

Experimental commands and flags are hidden. Set BUILDX_EXPERIMENTAL=1 to show them.
