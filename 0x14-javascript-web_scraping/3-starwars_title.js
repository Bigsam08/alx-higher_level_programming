#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request.get(api, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});
