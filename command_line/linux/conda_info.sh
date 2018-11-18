#!/bin/bash

# Check if a conda environment exists
TARGET_ENV="py36"
ENVS=$(conda env list | awk '{print $1}' )
if [[ $ENVS = *"$TARGET_ENV"* ]]; then
   echo "Environment exists"
else 
   echo "Error: The environment provided doesn't exist."
   exit
fi;

