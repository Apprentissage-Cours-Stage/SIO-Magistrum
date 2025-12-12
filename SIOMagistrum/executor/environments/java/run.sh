#!/bin/sh

cd /code

javac Main.java 2>&1

if [$? -eq 0]; then
    java Main 2>&1
else
    exit 1
fi