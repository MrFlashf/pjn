#!/bin/bash

arr=[]
i=0
while read line 
do
  if [ "$line" -eq "$line" ]
  then 
    arr[$i]=$line
    i=$i+1
  else
    echo "Not integer"
    exit 1
  fi
done

echo ${arr[*]} | tr " " "\n" | sort -nur | tr "\n" " "
