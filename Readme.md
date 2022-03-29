# Software Plagiarism Detector based on Graphs

## Easy usage

1. Make sure you have [Docker](https://docs.docker.com/get-docker/) installed
2. Create a new folder with the submissions in it e.g., ``mkdir submissions``. Inside that folder put in the submissions that should be tested. Every submission must be in a separate subfolder. The structure should look something like this:

```
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

3. Run ``docker run --rm -it -v {ABSOLUTE PATH TO THE SUBMISSION FOLDER CREATED IN STEP 2}:/app/submissions/ plagscan:latest`` with the following options:  

```
usage: main.py [-h] -l LANGUAGE [-p PROCESSES] [-o OUTPUT] [-sp SKIPPARSE]

optional arguments:
  -h, --help            show this help message and exit
  -l LANGUAGE, --Language LANGUAGE
                        Programming language that is beeing parsed. Options: c, python
  -p PROCESSES, --Processes PROCESSES
                        Number of processes used
  -o OUTPUT, --Output OUTPUT
                        Outputfile (default: report.md)
  -sp SKIPPARSE, --SkipParse SKIPPARSE
                        [DEBUG] Skip code parsing (Default: n).
```

