// npm install google-play-scraper

//'use strict';
var gplay = require('google-play-scraper');

var top = function(country_code, collection_code, start_index) {
  gplay.list({
    category: gplay.category.GAME,
    collection: collection_code,
    num : 100,
    country: country_code,
    start : start_index
  })
  .then(console.log, console.log);
}

top('au', gplay.collection.TOP_FREE, 0);