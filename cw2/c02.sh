#!/bin/bash

top_speed=0

while read line
do
  speed=($(echo $line | awk '{print $3}'))
  if [ "$speed" -eq "$speed" ]
  then
    if [ "$speed" -gt "$top_speed" ]
    then
      top_speed=$speed
    fi
  else
    echo "Top speed must be an integer!"
    exit 1
  fi
	
done
echo $top_speed