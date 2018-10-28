#/bin/bash

while read line
do
	cz_count=$(echo $line | grep -o "cz" | wc -l)
	sz_count=$(echo $line | grep -o "sz" | wc -l)
	all_count=$(($cz_count+$sz_count))
done

echo "Sum of 'cz' and 'sz': " $all_count
