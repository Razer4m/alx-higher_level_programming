#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    fetchCharacterNames(characters, 0);
  }
});

function fetchCharacterNames (characters, index) {
  request(characters[index], (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        fetchCharacterNames(characters, index + 1);
      }
    }
  });
}
