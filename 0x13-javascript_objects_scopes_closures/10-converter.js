#!/usr/bin/node
// converts a number to base 10

exports.converter = function (base) {
  return function (x) {
    return x.toString(base);
  };
};
