#!/usr/bin/node
// prints a str 'C is fun' in x times(user given times in argv)
// using a loop and convert string if possible

const msg = 'C is fun';
const x = Number(process.argv[2]);
let i = 0;
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (i < x) {
    console.log(msg);
    i++;
  }
}
