#!/bin/bash

echo "Installing dependencies"
# checking Python3
if [[ $echo $(python3 -V) == "" ]]; then
	echo "Installing python3"; apt-get install python3.8
fi
# checking pip3
if [[ $echo $(pip3 -V) == "" ]]; then
	echo "Installing pip3"; apt-get install python3-pip
fi
#Create DB
echo "Creating DB file"
db_file = $(ls | grep DB.db) 
if [[ $db_file == "" ]]; then
	touch DB.db
	print('DB file created!')
fi