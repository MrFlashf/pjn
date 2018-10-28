#!/bin/bash

while read line
do
	echo $line | sed -e 's/[żźćńółęąśŻŹĆĄŚĘŁÓŃ]/X/g'
done
