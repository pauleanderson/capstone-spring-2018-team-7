#!/bin/bash
# A bash script to download all the top 200 free, grossing, and new games from the apple app store
# Countries: au, nz, se, dk, no, at, ph
# Must enable execute permission for this file with chmod u+x pull_apple.sh
# Run by calling bash ~/capstone-spring-2018-team-7/collect_data/pull_apple.sh

charts='free gross new'
date=$(date +%Y-%m-%d)

for chart in $charts
do
    countries='au nz se dk no at ph'

    for country in $countries
    do
        node ~/capstone-spring-2018-team-7/collect_data/apl_${chart}.js -c $country | jsonlint -f -q -S > ~/capstone-spring-2018-team-7/collect_data/apple/${country}_${chart}_${date}.json
    done
done