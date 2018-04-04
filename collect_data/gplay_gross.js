// npm install google-play-scraper
// npm install command-line-args

var gplay = require('google-play-scraper');
const commandLineArgs = require('command-line-args')

const optionDefinitions = [
  {name: 'country_code', alias: 'c', type: String},
  {name: 'start_index', alias: 'i', type: Number}
]

const options = commandLineArgs(optionDefinitions)

var top = function(var_country_code, var_start_index) {
  gplay.list({
    category: gplay.category.GAME,
    collection: gplay.collection.GROSSING,
    num : 50,
    country: var_country_code,
    start : var_start_index,
  })
  .then(console.log, console.log);
} 

top(options.country_code, options.start_index);