#!/usr/bin/node
// a class square that inherits from a rectangle

class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
