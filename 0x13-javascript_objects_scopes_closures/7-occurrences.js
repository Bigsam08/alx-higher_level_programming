#!/usr/bin/node

// number of occurence

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let count = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      count++;
    }
    i++;
  }
  return count;
};
