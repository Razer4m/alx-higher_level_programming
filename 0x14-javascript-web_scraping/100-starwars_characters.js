#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
