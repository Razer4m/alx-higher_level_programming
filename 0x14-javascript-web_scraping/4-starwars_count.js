#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = 'https://swapi-api.alx-tools.com/api/people/18/';

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body).results;
  const wedgeMoviesCount = films.filter(film => film.characters.includes(wedgeAntillesId)).length;
  console.log(wedgeMoviesCount);
});
