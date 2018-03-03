// npm install app-store-scraper
// npm install command-line-args

var store = require('app-store-scraper');
const commandLineArgs = require('command-line-args')

const optionDefinitions = [
  {name: 'country_code', alias: 'c', type: String}
]

const options = commandLineArgs(optionDefinitions)

var top = function(var_country_code) {
  store.list({
    collection: store.collection.NEW_GAMES_IOS,
    num : 100,
    country: var_country_code,
  })
  .then(console.log, console.log);
} 

top(options.country_code);