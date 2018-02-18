#!/bin/bash
# A bash script to download all the top 500 free, grossing, and trending games from the android marketplace
# Countries: au, nz, se, dk, no, at, ph
# Must enable execute permission for this file with chmod u+x pull_android.sh
# Run by calling bash ~/capstone-spring-2018-team-7/collect_data/pull_android.sh

countries='au nz se dk no at ph'
#countries='au nz'

for country in $countries
do
    node ~/capstone-spring-2018-team-7/collect_data/gplay_free.js -c $country -i 0 | tr -d '[]' > ~/capstone-spring-2018-team-7/collect_data/JSON/free_0.json 
    i=$(grep -c 'Error: Error' ~/capstone-spring-2018-team-7/collect_data/JSON/free_0.json)
    until [ $i -eq 0 ]
    do
        node ~/capstone-spring-2018-team-7/collect_data/gplay_free.js -c $country -i 0 | tr -d '[]' > ~/capstone-spring-2018-team-7/collect_data/JSON/free_0.json 
        i=$(grep -c 'Error: Error' ~/capstone-spring-2018-team-7/collect_data/JSON/free_0.json)
    done

    node ~/capstone-spring-2018-team-7/collect_data/gplay_free.js -c $country -i 100 | tr -d '[]' > ~/capstone-spring-2018-team-7/collect_data/JSON/free_100.json
    i=$(grep -c 'Error: Error' ~/capstone-spring-2018-team-7/collect_data/JSON/free_100.json)
    until [ $i -eq 0 ]
    do
        node ~/capstone-spring-2018-team-7/collect_data/gplay_free.js -c $country -i 100 | tr -d '[]' > ~/capstone-spring-2018-team-7/collect_data/JSON/free_100.json 
        i=$(grep -c 'Error: Error' ~/capstone-spring-2018-team-7/collect_data/JSON/free_100.json)
    done   
    
    node ~/capstone-spring-2018-team-7/collect_data/gplay_free.js -c $country -i 200 | tr -d '[]' > ~/capstone-spring-2018-team-7/collect_data/JSON/free_200.json
    i=$(grep -c 'Error: Error' ~/capstone-spring-2018-team-7/collect_data/JSON/free_200.json)
    until [ $i -eq 0 ]
    do
        node ~/capstone-spring-2018-team-7/collect_data/gplay_free.js -c $country -i 200 | tr -d '[]' > ~/capstone-spring-2018-team-7/collect_data/JSON/free_200.json 
        i=$(grep -c 'Error: Error' ~/capstone-spring-2018-team-7/collect_data/JSON/free_200.json)
    done   
    
    node ~/capstone-spring-2018-team-7/collect_data/gplay_free.js -c $country -i 300 | tr -d '[]' > ~/capstone-spring-2018-team-7/collect_data/JSON/free_300.json
    i=$(grep -c 'Error: Error' ~/capstone-spring-2018-team-7/collect_data/JSON/free_300.json)
    until [ $i -eq 0 ]
    do
        node ~/capstone-spring-2018-team-7/collect_data/gplay_free.js -c $country -i 300 | tr -d '[]' > ~/capstone-spring-2018-team-7/collect_data/JSON/free_300.json 
        i=$(grep -c 'Error: Error' ~/capstone-spring-2018-team-7/collect_data/JSON/free_300.json)
    done 
    
    node ~/capstone-spring-2018-team-7/collect_data/gplay_free.js -c $country -i 400 | tr -d '[]' > ~/capstone-spring-2018-team-7/collect_data/JSON/free_400.json
    i=$(grep -c 'Error: Error' ~/capstone-spring-2018-team-7/collect_data/JSON/free_400.json)
    until [ $i -eq 0 ]
    do
        node ~/capstone-spring-2018-team-7/collect_data/gplay_free.js -c $country -i 400 | tr -d '[]' > ~/capstone-spring-2018-team-7/collect_data/JSON/free_400.json 
        i=$(grep -c 'Error: Error' ~/capstone-spring-2018-team-7/collect_data/JSON/free_400.json)
    done 
    
    echo '[' > ~/capstone-spring-2018-team-7/collect_data/JSON/${country}_free.json 
    cat ~/capstone-spring-2018-team-7/collect_data/JSON/free_0.json >> ~/capstone-spring-2018-team-7/collect_data/JSON/${country}_free.json 
    echo ',' >> ~/capstone-spring-2018-team-7/collect_data/JSON/${country}_free.json 
    cat ~/capstone-spring-2018-team-7/collect_data/JSON/free_100.json >> ~/capstone-spring-2018-team-7/collect_data/JSON/${country}_free.json 
    echo ',' >> ~/capstone-spring-2018-team-7/collect_data/JSON/${country}_free.json 
    cat ~/capstone-spring-2018-team-7/collect_data/JSON/free_200.json >> ~/capstone-spring-2018-team-7/collect_data/JSON/${country}_free.json 
    echo ',' >> ~/capstone-spring-2018-team-7/collect_data/JSON/${country}_free.json 
    cat ~/capstone-spring-2018-team-7/collect_data/JSON/free_300.json >> ~/capstone-spring-2018-team-7/collect_data/JSON/${country}_free.json 
    echo ',' >> ~/capstone-spring-2018-team-7/collect_data/JSON/${country}_free.json 
    cat ~/capstone-spring-2018-team-7/collect_data/JSON/free_400.json >> ~/capstone-spring-2018-team-7/collect_data/JSON/${country}_free.json 
    echo ']' >> ~/capstone-spring-2018-team-7/collect_data/JSON/${country}_free.json 
    rm ~/capstone-spring-2018-team-7/collect_data/JSON/free_0.json ~/capstone-spring-2018-team-7/collect_data/JSON/free_100.json ~/capstone-spring-2018-team-7/collect_data/JSON/free_200.json ~/capstone-spring-2018-team-7/collect_data/JSON/free_300.json ~/capstone-spring-2018-team-7/collect_data/JSON/free_400.json
done

#au gross
#node gplay_gross.js -c 'au' -i 0 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_0.json
#node gplay_gross.js -c 'au' -i 100 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_100.json
#node gplay_gross.js -c 'au' -i 200 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_200.json
#node gplay_gross.js -c 'au' -i 300 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_300.json
#node gplay_gross.js -c 'au' -i 400 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_400.json
#cat ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_0.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_100.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_200.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_300.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_400.json > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross.json
#rm ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_0.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_100.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_200.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_300.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_400.json

#au trend
#node gplay_trend.js -c 'au' -i 0 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_0.json
#node gplay_trend.js -c 'au' -i 100 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_100.json
#node gplay_trend.js -c 'au' -i 200 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_200.json
#node gplay_trend.js -c 'au' -i 300 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_300.json
#node gplay_trend.js -c 'au' -i 400 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_400.json
#cat ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_0.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_100.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_200.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_300.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_400.json > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend.json
#rm ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_0.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_100.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_200.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_300.json ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_400.json
