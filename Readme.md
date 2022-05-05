# Software Plagiarism Detection Based on [Program Dependence Graphs](https://docs.joern.io/code-property-graph)

## Usage

1. Make sure you have [Docker](https://docs.docker.com/get-docker/) installed. This repository does not need to be cloned.
2. Pull the prebuilt PlagScan image: `docker pull stefankoerner1/plagscan:latest`. Note that this will download about 1.6 GB.
3. `cd` into the folder with the submissions that should be tested. Every submission must be in a separate subfolder. The structure should look something like this:

   ```text
   .
   └── submissions
       ├── 08891236_F_A082
       │   └── f.c
       ├── 08534792_F_A026
       │   └── f.c
       ├── 08845662_F_A167
       │   └── f.c
       ├── 02343900_F_A255
       │   └── f.c
       ├── 08234263_F_A056
       │   └── f.c
       ├── 08666956_F_A157
       │   └── f.c
       ├── 08235553_F_A030
       │   └── f.c
       └── 08962935_F_A150
           └── f.c
   ```

4. Inside this folder run:

   ```bash
   docker run --rm -it -v $PWD:/app/submissions/ stefankoerner1/plagscan:latest
   ```

   (Note: $PWD might not work on every OS. See [here](https://docs.docker.com/desktop/windows/troubleshoot/#path-conversion-on-windows) and [here](https://stackoverflow.com/questions/41485217/mount-current-directory-as-a-volume-in-docker-on-windows-10) for possible solutions.)

   with the following arguments:

   ```
   usage: [-h] -l LANGUAGE [-t THREADS] [-o OUTPUT] [-v VERBOSE]

   arguments:
       -h, --help            show this help message and exit
       -l LANGUAGE, --Language LANGUAGE
                               Programming language that is being used. Options: c, python
       -t THREADS, --Threads THREADS
                               Number of threads used (default: 4).
       -o OUTPUT, --Output OUTPUT
                               CSV that contains all suspicious combinations (default: report.csv).
       -v VERBOSE, --Verbose VERBOSE
                               Print [all] results or only [suspicious] (default: suspicious).
   ```

   Example usage for the language "C" that will use 8 threads:

   ```bash
   docker run --rm -it -v $PWD:/app/submissions/ stefankoerner1/plagscan:latest --Language c --Threads 8
   ```

## Build locally

To build the image locally run:

```bash
docker build --pull --rm -f "Dockerfile" -t plagscan:latest "."
```

## Development

For development, it is recommended to use [Visual Studio Code Remote - Containers](https://code.visualstudio.com/docs/remote/containers) with the .devcontainer/devcontainer.json file from this repository.
