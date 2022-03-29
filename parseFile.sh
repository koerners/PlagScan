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

max_children=$3

function parallel {
  "$@" &
  local my_pid=$$
  local children=$(ps -eo ppid | grep -w $my_pid | wc -w)
  children=$((children-1))
  if [[ $children -ge $max_children ]]; then
    wait -n
  fi
}

for d in */ ; do
    DIR=${d%/}
    parallel parse $1 $DIR 
done
wait 
cd ..
rm -rf intermediate
