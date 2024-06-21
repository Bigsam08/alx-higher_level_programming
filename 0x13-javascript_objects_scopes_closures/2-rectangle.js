#!/usr/bin/node
// create a class Rectangle
// return empty class if w or h <= 0

class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger || !Number.isInteger || w <= 0 || h <= 0) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
