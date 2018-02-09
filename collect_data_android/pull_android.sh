#!/bin/bash
# A bash script to download all the top 500 free, grossing, and trending games from the android marketplace
# Run by calling ~/capstone-spring-2018-team-7/collect_data_android/pull_android.sh

node gplay_free.js -c 'au' -i 0 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_free_0.json
node gplay_free.js -c 'au' -i 100 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_free_100.json
node gplay_free.js -c 'au' -i 200 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_free_200.json
node gplay_free.js -c 'au' -i 300 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_free_300.json
node gplay_free.js -c 'au' -i 400 > ~/capstone-spring-2018-team-7/collect_data_android/JSON/au_free_400.json
