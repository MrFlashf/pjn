#!/bin/bash

lines=[]
i=0
while read line 
do
  lines[$i]=$line
  i=$[$i+1]
done

# i=$[$i-1]
while [ $i -ge 1 ]
do
  echo $i. ${lines[$i-1]}
  i=$[$i-1]
done