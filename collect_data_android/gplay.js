// npm install google-play-scraper

'use strict';
var gplay = require('google-play-scraper');
const fs = require('fs');

var err_handler = function(err) {
  console.log(err);
}

au_free = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.TOP_FREE,
  num: 120,
  country: 'au'
  });
 // .then(JSON.stringify, err_handler)
 // .then(fs.writeFileSync('au_free.json'), err_handler);
data_au_free = JSON.stringify(au_free);
fs.writeFileSync('au_free.json', data_au_free);


au_gross = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.GROSSING,
  num: 120,
  country: 'au'
  });

nz_free = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.TOP_FREE,
  num: 120,
  country: 'nz'
  });

nz_gross = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.GROSSING,
  num: 120,
  country: 'nz'
  });

se_free = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.TOP_FREE,
  num: 120,
  country: 'se'
  }); 

se_gross = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.GROSSING,
  num: 120,
  country: 'se'
  });

dk_free = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.TOP_FREE,
  num: 120,
  country: 'dk'
  }); 

dk_gross = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.GROSSING,
  num: 120,
  country: 'dk'
  }); 

no_free = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.TOP_FREE,
  num: 120,
  country: 'no'
  }); 

no_gross = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.GROSSING,
  num: 120,
  country: 'no'
  });  

at_free = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.TOP_FREE,
  num: 120,
  country: 'at'
  }); 

at_gross = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.GROSSING,
  num: 120,
  country: 'at'
  });  

ph_free = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.TOP_FREE,
  num: 120,
  country: 'ph'
  }); 

ph_gross = gplay.list({
  category: gplay.category.GAME,
  collection: gplay.collection.GROSSING,
  num: 120,
  country: 'ph'
  });

