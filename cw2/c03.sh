#!/bin/bash

lines=[]
i=0
while read line 
do
  lines[$i]=$line
  i=$i+1
done

if [[ ${lines[122]} ]] ; then
   echo ${lines[122]}
else 
	echo "Not enough elements"
fi
