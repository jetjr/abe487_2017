#!/bin/bash

if [[ $1 == "" ]]; then
   echo "Usage: hello.sh name"
   exit 1
fi

echo "Hello, $1!"
