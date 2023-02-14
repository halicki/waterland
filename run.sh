#!/usr/bin/env bash
# get one argument from commad line
FILE=$1

# check if argument is not empty
if [ -z "$FILE" ]
then
    echo "No argument supplied"
    exit 1
fi

# check if file exists
if [ ! -f "$FILE" ]
then
    echo "File $FILE does not exist"
    exit 1
fi

DIR=$(dirname "$(realpath "$FILE")")
NAME=$(basename "$FILE")

docker compose run --rm -ti -v "$DIR":/data app python -m waterland /data/"$NAME"
