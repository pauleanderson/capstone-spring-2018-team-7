// au, nz, se, dk, no, at, ph

var gplay = require('google-play-scraper');

au_free = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.TOP_FREE,
  num: 120,
  country: 'au'
  });

au_gross = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.GROSSING,
  num: 120,
  country: 'au'
  });

  console.log('Success');