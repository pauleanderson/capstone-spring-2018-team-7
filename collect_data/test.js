var gplay = require('google-play-scraper');

gplay.list({
    category: gplay.category.GAME_ACTION,
    collection: gplay.collection.TOP_FREE,
    country: 'au',
    num: 50,
  })
  .then(console.log, console.log);
  
// gplay.list({
//     category: gplay.category.GAME_ACTION,
//     collection: gplay.collection.TOP_FREE,
//     country: 'nz',
//     num: 50,
//     fullDetail : true
//   })
//   .then(console.log, console.log);
  
// gplay.list({
//     category: gplay.category.GAME_ACTION,
//     collection: gplay.collection.TOP_FREE,
//     country: 'se',
//     num: 50,
//     fullDetail : true
//   })
//   .then(console.log, console.log);
  
// gplay.list({
//     category: gplay.category.GAME_ACTION,
//     collection: gplay.collection.TOP_FREE,
//     country: 'dk',
//     num: 50,
//     fullDetail : true
//   })
//   .then(console.log, console.log);
  
// gplay.list({
//     category: gplay.category.GAME_ACTION,
//     collection: gplay.collection.TOP_FREE,
//     country: 'no',
//     num: 50,
//     fullDetail : true
//   })
//   .then(console.log, console.log);
  
// gplay.list({
//     category: gplay.category.GAME_ACTION,
//     collection: gplay.collection.TOP_FREE,
//     country: 'at',
//     num: 50,
//     fullDetail : true
//   })
//   .then(console.log, console.log);
  
// gplay.list({
//     category: gplay.category.GAME_ACTION,
//     collection: gplay.collection.TOP_FREE,
//     country: 'ph',
//     num: 50,
//     fullDetail : true
//   })
//   .then(console.log, console.log);