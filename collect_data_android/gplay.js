var gplay = require('google-play-scraper');

gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.TOP_FREE,
  num: 120
  })
  .then(console.log, console.log);

gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.GROSSING,
  num: 120
  })
  .then(console.log, console.log)