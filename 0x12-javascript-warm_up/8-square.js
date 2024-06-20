#!/usr/bin/node
// print square in the number of times given in argv[2]
// print char 'x'

const symbol = 'x';
const times = Number(process.argv[2]);
let i = 0;
let k = 0;
if (isNaN(times)) {
  console.log('Missing size');
} else {
  while (i < times) {
    let row = '';
    k = 0;
    while (k < times) {
      row += symbol;
      k++;
    }
    console.log(row);
    i++;
  }
}
