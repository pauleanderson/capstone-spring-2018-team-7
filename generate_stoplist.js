var store = require('app-store-scraper');

store.list({
    collection: store.collection.TOP_GROSSING_IOS,
    num : 75,
    country: 'us',
})
.then(console.log, console.log);

//node generate_stoplist.js | jsonlint -f -q -S > stoplist.json
