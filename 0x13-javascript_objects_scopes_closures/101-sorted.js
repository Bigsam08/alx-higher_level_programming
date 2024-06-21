#!/usr/bin/node
// import dictionsry

const dict = require('./101-data.js').dict;
const newDico = {};
for (const key in dict) {
  if (newDico[dict[key]] === undefined) {
    newDico[dict[key]] = [key];
  } else {
    newDico[dict[key]].push(key);
  }
}
console.log(newDico);
