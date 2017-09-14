#!/bin/bash

if [[ $1 == "" ]] || [[ $2 == "" ]]; then
  echo "Usage: hello-arg2.sh greeting name"
  exit 1
fi

echo "$1, $2!"
