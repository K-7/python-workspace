#!/usr/bin/env bash

file_name=$1
if [ $file_name ]; then
    python parking_lot.py $file_name
else
    python parking_lot.py
fi