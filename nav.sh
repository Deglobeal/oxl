#!/bin/bash

curl -s https://www.amfiindia.com/spages/NAVAll.txt -o NAVAll.txt

awk -F ';' 'NF >= 5 && $1 ~ /^[0-9]+$/ { print $4 "\t" $5 }' NAVAll.txt > nav_data.tsv

echo "Data extracted to nav_data.tsv"
