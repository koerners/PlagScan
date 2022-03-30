# Software Plagiarism Detection Based on Graphs

## Easy usage

1. Make sure you have [Docker](https://docs.docker.com/get-docker/) installed
2. Pull the PlagScan image: ``docker pull stefankoerner1/plagscan:latest``. Note that this will download about 1.6 GB and has to be done only once.
3. ``cd`` into the folder with the submissions that should be tested. Every submission must be in a separate subfolder. The structure should look something like this:

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
        ├── 0866696_F_A157
        │   └── f.c
        ├── 0823553_F_A030
        │   └── f.c
        └── 089679345_F_A150
            └── f.c
    ```

4. Inside this folder run:

   ```bash
   docker run --rm -it -v $PWD:/app/submissions/ plagscan:latest
   ```

   with the following arguments:  

    ```text
    usage: [-h] -l LANGUAGE [-p PROCESSES] [-o OUTPUT] [-sp SKIPPARSE] [-v VERBOSE]

    arguments:
    -h, --help            show this help message and exit
    -l LANGUAGE, --Language LANGUAGE
                            Programming language that is beeing used. Options: c, python
    -p PROCESSES, --Processes PROCESSES
                            Number of processes used.
    -o OUTPUT, --Output OUTPUT
                            Outputfile (default: report.md).
    -v VERBOSE, --Verbose VERBOSE
                            Print [all] results or only [suspicious] (default: suspicious).
    -sp SKIPPARSE, --SkipParse SKIPPARSE
                            [DEBUG] Skip code parsing [y/n] (default: n).
    ```

    Example usage for the language "C" that will use 4 threads:

    ```bash
   docker run --rm -it -v $PWD:/app/submissions/ plagscan:latest --Language c --Processes 4 
   ```


## Build locally

To build the Image locally run:

```bash
docker build --pull --rm -f "Dockerfile" -t plagscan:latest "."
```

## Development

For development it is recommended to use [Visual Studio Code Remote - Containers](https://code.visualstudio.com/docs/remote/containers) with the .devcontainer/devcontainer.json file from this repository.
