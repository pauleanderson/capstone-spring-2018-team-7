#!/bin/bash
# A bash script to download all the top 500 free, grossing, and trending games from the android marketplace
# Countries: au, nz, se, dk, no, at, ph
# Must enable execute permission for this file with chmod u+x pull_android.sh
# Run by calling bash ~/capstone-spring-2018-team-7/collect_data/pull_android.sh

charts='free gross trend'
date=$(date +%Y-%m-%d)
for chart in $charts
do
    countries='au nz se dk no at ph'

    for country in $countries
    do
        node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 0 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/android/${chart}_0.json 
        i=$(grep -c 'Error: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/android/${chart}_0.json)
        until [ $i -eq 0 ]
        do
            node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 0 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/android/${chart}_0.json 
            i=$(grep -c 'Error: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/android/${chart}_0.json)
        done

        node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 100 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/android/${chart}_100.json
        i=$(grep -c 'Error: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/android/${chart}_100.json)
        until [ $i -eq 0 ]
        do
            node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 100 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/android/${chart}_100.json 
            i=$(grep -c 'Error: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/android/${chart}_100.json)
        done   
    
        node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 200 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/android/${chart}_200.json
        i=$(grep -c 'Error: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/android/${chart}_200.json)
        until [ $i -eq 0 ]
        do
            node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 200 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/android/${chart}_200.json 
            i=$(grep -c 'Error: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/android/${chart}_200.json)
        done   
    
        node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 300 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/android/${chart}_300.json
        i=$(grep -c 'Error: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/android/${chart}_300.json)
        until [ $i -eq 0 ]
        do
            node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 300 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/android/${chart}_300.json 
            i=$(grep -c 'Error: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/android/${chart}_300.json)
        done 
    
        node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 400 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/android/${chart}_400.json
        i=$(grep -c 'Error: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/android/${chart}_400.json)
        until [ $i -eq 0 ]
        do
            node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 400 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/android/${chart}_400.json 
            i=$(grep -c 'Error: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/android/${chart}_400.json)
        done 
    
        echo '[' > ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json 
        cat ~/capstone-spring-2018-team-7/collect_data/android/${chart}_0.json >> ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json 
        echo ',' >> ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json 
        cat ~/capstone-spring-2018-team-7/collect_data/android/${chart}_100.json >> ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json 
        echo ',' >> ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json 
        cat ~/capstone-spring-2018-team-7/collect_data/android/${chart}_200.json >> ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json 
        echo ',' >> ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json 
        cat ~/capstone-spring-2018-team-7/collect_data/android/${chart}_300.json >> ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json 
        echo ',' >> ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json 
        cat ~/capstone-spring-2018-team-7/collect_data/android/${chart}_400.json >> ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json 
        echo ']' >> ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json
        
        jsonlint -f -q -S ~/capstone-spring-2018-team-7/collect_data/android/${country}_${chart}_${date}.json > ~/capstone-spring-2018-team-7/collect_data/android/tempfile.json
        
        rm ~/capstone-spring-2018-team-7/collect_data/android/tempfile.json ~/capstone-spring-2018-team-7/collect_data/android/${chart}_0.json ~/capstone-spring-2018-team-7/collect_data/android/${chart}_100.json ~/capstone-spring-2018-team-7/collect_data/android/${chart}_200.json ~/capstone-spring-2018-team-7/collect_data/android/${chart}_300.json ~/capstone-spring-2018-team-7/collect_data/android/${chart}_400.json
    done
done