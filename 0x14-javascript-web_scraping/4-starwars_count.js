#!/usr/bin/node

const request = require('request');
const api = process.argv[2];

request.get(api, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movies = JSON.parse(body).results;
  const wedge = movies.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0);
  console.log(wedge);
  // }
});
