#!/bin/bash

if [[ ! $1 ]]; then
  echo "Usage: cat-n.sh file"
  exit 1
fi

if [[ ! -f $1 ]]; then
  echo "\"$1\" is not a file"
  exit 1
fi

COUNT=0

while read line; do
  COUNT=$(($COUNT+1))
  echo $COUNT $line
done < $1
