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
console.log('Success');