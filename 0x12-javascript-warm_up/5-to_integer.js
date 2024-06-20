#!/usr/bin/node
// convert string to integer using '+' 'Number' 'math.floor' or 'parseInt'

const arg = Math.floor(process.argv[2]);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
