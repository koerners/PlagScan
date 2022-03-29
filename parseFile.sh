#!/bin/bash

rm -rf graphs
rm -rf intermediate

mkdir graphs
mkdir intermediate

cd submissions

parse() {
    joern-parse --language "$1" --output "../intermediate/$2.bin" "$2"
    joern-export --out "../graphs/$2/" --repr pdg "../intermediate/$2.bin"
}


for d in */ ; do
    DIR=${d%/}
    echo $DIR
    parse $1 $DIR
done

cd ..
rm -rf intermediate
