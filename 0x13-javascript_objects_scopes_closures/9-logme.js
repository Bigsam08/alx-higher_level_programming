#!/usr/bin/node
// print list

let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
