#!/bin/bash
echo "Phease enter project name"
read -r name
if [ ! -d $name ]
then
    mkdir -p $name
fi
virtualenv -p "C:\Users\tuan.tran-quoc.BANVIENCORP\AppData\Local\Programs\Python\Python39\python.exe" "$name/env"