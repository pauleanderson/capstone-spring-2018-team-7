#!/bin/bash
# A bash script to reformat apple json files correctly

cd ~/capstone-spring-2018-team-7/collect_data/apple
for filename in *
do
    jsonlint -f -q $filename > tempfile.json
    cat tempfile.json > $filename
done
rm tempfile.json