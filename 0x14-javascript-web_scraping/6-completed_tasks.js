#!/usr/bin/node

const request = require('request');
const api = process.argv[2];
const store = {};

request.get(api, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  data.forEach((result) => {
    if (result.completed === true) {
      const userid = result.userId;
      if (!(userid in store)) {
        store[userid] = 0;
      }
      store[userid] += 1;
    }
  });
  console.log(store);
});
