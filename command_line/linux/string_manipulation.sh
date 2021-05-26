#!/bin/bash

# Find a substring in a string
string='My string';
if [[ $string =~ "My" ]]; then
   echo "It's there!"
fi
if [[ $string == *"My"* ]]; then
   echo "String found!"
fi
