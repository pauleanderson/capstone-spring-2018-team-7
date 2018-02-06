var gplay = require('google-play-scraper');
gplay.app({appId: 'com.dxco.pandavszombies'})
  .then(console.log, console.log);