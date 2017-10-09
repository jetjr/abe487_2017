#!/bin/bash

if [[ ! $1 ]]; then
  echo "Usage: head.sh FILE [NUM]"
  exit 1
fi

if [[ ! -f $1 ]]; then
  echo "\"$1\" is not a file"
  exit 1
fi

if [[ ! $2 ]]; then
  NUM=3
else
  NUM=$2
fi

head -n $NUM $1
