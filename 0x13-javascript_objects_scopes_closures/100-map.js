#!/usr/bin/node
// list
const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((item, idx) => item * idx));
