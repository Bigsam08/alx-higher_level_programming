#!/usr/bin/node

// print a list in réverse order

exports.esrever = function (list) {
  const newList = [];
  let i = list.length - 1;
  while (i >= 0) {
    newList.push(list[i]);
    i--;
  }
  return newList;
};
