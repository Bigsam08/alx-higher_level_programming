#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const api = process.argv[2];
const file = process.argv[3];

request.get(api, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(file, body, 'utf-8', (error, data) => {
    if (error) {
      console.error(error);
    }
  });
});
