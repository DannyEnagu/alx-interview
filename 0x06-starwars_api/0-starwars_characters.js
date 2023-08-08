#!/usr/bin/node
// A script that prints all characters of a Star Wars movie.

const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/';
const url = api + process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.error(err);
  } else {
    if (res.statusCode === 200) {
      const characters = JSON.parse(body).characters;
      const sortedCharacters = [];
      let j = 0; // J will keep track of the character loop

      for (const i in characters) {
        request(characters[i], function (error, resp, body) {
          if (resp.statusCode === 200) {
            // Add to sorted list
            sortedCharacters.push({ name: JSON.parse(body).name, index: i });
            // check that we are at the end of the characters
            if (j === characters.length - 1) {
              sortedCharacters.sort((a, b) => a.index - b.index);
              sortedCharacters.forEach(x => { console.log(x.name); });
            }
            j++; // Increase J after every success response
          } else {
            console.error(error);
          }
        });
      }
    }
  }
});
