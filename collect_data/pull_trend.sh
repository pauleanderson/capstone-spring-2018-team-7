#!/bin/bash
# A bash script to download all the top 500 trending games from the android marketplace
# Countries: au, nz, se, dk, no, at, ph
# Must enable execute permission for this file with chmod u+x pull_trend.sh
# Run by calling bash ~/capstone-spring-2018-team-7/collect_data/pull_trend.sh

charts='trend'
date=$(date +%Y-%m-%d)
for chart in $charts
do
    countries='dk'

    for country in $countries
    do
        node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 300 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_300.json
        i=$(grep -c 'rror: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_300.json)
        i2=$(grep -xc '^[[:space:]]*$' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_300.json)
        echo $i2
        until [ $i -eq 0 ] && [ $i2 -eq 0 ]
        do
            node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 300 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_300.json 
            i=$(grep -c 'rror: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_300.json)
            i2=$(grep -xc '^[[:space:]]*$' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_300.json)
            echo $i2
        done 
    
        node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 350 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_350.json 
        i=$(grep -c 'rror: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_350.json)
        i2=$(grep -xc '^[[:space:]]*$' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_350.json)
        until [ $i -eq 0 ] && [ $i2 -eq 0 ]
        do
            node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 350 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_350.json 
            i=$(grep -c 'rror: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_350.json)
            i2=$(grep -xc '^[[:space:]]*$' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_350.json)
        done
    
        node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 400 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_400.json
        i=$(grep -c 'rror: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_400.json)
        i2=$(grep -xc '^[[:space:]]*$' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_400.json)
        until [ $i -eq 0 ] && [ $i2 -eq 0 ]
        do
            node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 400 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_400.json 
            i=$(grep -c 'rror: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_400.json)
            i2=$(grep -xc '^[[:space:]]*$' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_400.json)
        done 
    
        node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 450 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_450.json 
        i=$(grep -c 'rror: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_450.json)
        i2=$(grep -xc '^[[:space:]]*$' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_450.json)
        until [ $i -eq 0 ] && [ $i2 -eq 0 ]
        do
            node ~/capstone-spring-2018-team-7/collect_data/gplay_${chart}.js -c $country -i 450 | sed '$ s/.$//' | sed '1s/^.//' > ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_450.json 
            i=$(grep -c 'rror: Error\|ypeError' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_450.json)
            i2=$(grep -xc '^[[:space:]]*$' ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_450.json)
        done
    
    
    
        echo '[' > ~/capstone-spring-2018-team-7/collect_data/trend/${country}_${chart}_${date}.json 
        cat ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_300.json >> ~/capstone-spring-2018-team-7/collect_data/trend/${country}_${chart}_${date}.json
        echo ',' >> ~/capstone-spring-2018-team-7/collect_data/trend/${country}_${chart}_${date}.json
        cat ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_350.json >> ~/capstone-spring-2018-team-7/collect_data/trend/${country}_${chart}_${date}.json 
        echo ',' >> ~/capstone-spring-2018-team-7/collect_data/trend/${country}_${chart}_${date}.json 
        cat ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_400.json >> ~/capstone-spring-2018-team-7/collect_data/trend/${country}_${chart}_${date}.json 
        echo ',' >> ~/capstone-spring-2018-team-7/collect_data/trend/${country}_${chart}_${date}.json
        cat ~/capstone-spring-2018-team-7/collect_data/trend/${chart}_450.json >> ~/capstone-spring-2018-team-7/collect_data/trend/${country}_${chart}_${date}.json 
        echo ']' >> ~/capstone-spring-2018-team-7/collect_data/trend/${country}_${chart}_${date}.json
        
        jsonlint -f -q -S ~/capstone-spring-2018-team-7/collect_data/trend/${country}_${chart}_${date}.json > ~/capstone-spring-2018-team-7/collect_data/trend/tempfile.json
        cat ~/capstone-spring-2018-team-7/collect_data/trend/tempfile.json > ~/capstone-spring-2018-team-7/collect_data/trend/${country}_${chart}_${date}.json
        
    done
done
