#!/bin/bash

lines=[]
i=0
while read line 
do
  lines[$i]=$line
  i=$i+1
done

i=9
while [ $i -lt 20 ]
do
  echo ${lines[$i]}
  i=$[$i+1]
done
