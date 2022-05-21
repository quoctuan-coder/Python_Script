#!/bin/bash

# How to run: source 02_active.sh

echo "Phease chose project name to active"
read -r name
if [ ! -d $name ]
then
    echo "Project don't exist. Please create the project"
else
    cd $name/
    source env/Scripts/activate
    echo "Project active"
fi
