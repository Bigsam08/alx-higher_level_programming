#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/films/' + id;

request.get(api, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const chara = data.characters;
  for (const i of chara) {
    request.get(i, (error, response, bodyNew) => {
      if (error) {
        console.log(error);
      }
      const content = JSON.parse(bodyNew);
      console.log(content.name);
    });
  }
});
