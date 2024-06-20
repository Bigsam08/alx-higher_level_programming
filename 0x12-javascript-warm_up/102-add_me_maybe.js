#!/usr/bin/node

// incrementing

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
