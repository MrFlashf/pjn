#!/bin/bash

count=0
while read line
do
	words=$(echo $line | tr -d ',.;!:()-?"-'"'" | wc -w)
	count=$(($count+$words))
done

echo $count
