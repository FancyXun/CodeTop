#!/bin/bash

list=()

for file in "./"; do
    if [[ $file == *.py ]]
    then
           echo $file
           extension="${$file##*.}"
           filename="${$file%.*}"
           list+=(filename)
    fi
done;