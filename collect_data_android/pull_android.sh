#!/bin/bash
# A bash script to download all the top 500 free, grossing, and trending games from the android marketplace
# Countries: au, nz, se, dk, no, at, ph
# Must enable execute permission for this file with chmod u+x pull_android.sh
# Run by calling bash ~/capstone-spring-2018-team-7/collect_data_android/pull_android.sh

#au free
node gplay_free.js -c 'au' -i 0 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_free_0.json
node gplay_free.js -c 'au' -i 100 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_free_100.json
node gplay_free.js -c 'au' -i 200 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_free_200.json
node gplay_free.js -c 'au' -i 300 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_free_300.json
node gplay_free.js -c 'au' -i 400 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_free_400.json

#au gross
node gplay_gross.js -c 'au' -i 0 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_0.json
node gplay_gross.js -c 'au' -i 100 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_100.json
node gplay_gross.js -c 'au' -i 200 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_200.json
node gplay_gross.js -c 'au' -i 300 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_300.json
node gplay_gross.js -c 'au' -i 400 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_gross_400.json

#au trend
node gplay_trend.js -c 'au' -i 0 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_0.json
node gplay_trend.js -c 'au' -i 100 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_100.json
node gplay_trend.js -c 'au' -i 200 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_200.json
node gplay_trend.js -c 'au' -i 300 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_300.json
node gplay_trend.js -c 'au' -i 400 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_trend_400.json

