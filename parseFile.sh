#!/bin/bash

mkdir graphs
cd submissions
pwd
for d in */ ; do
    DIR=${d%/}
    echo $DIR
    mkdir intermediate
    joern-parse --language "$1" --output "intermediate/$DIR.bin" "$DIR"
    joern-export --out "../graphs/$DIR/" --repr pdg "intermediate/$DIR.bin"
    rm -rf intermediate
done
