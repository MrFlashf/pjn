#!/bin/bash

i="1"

while [ $i -lt 100 ]
do
  echo "Linia ${i}" >> zad3_lessthan123.txt
  i=$[$i+1]
done