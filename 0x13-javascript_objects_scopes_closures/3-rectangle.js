#!/usr/bin/node
// create a class with w, h with a method that prints X

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let k = 0; k < this.width; k++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
