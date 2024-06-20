#!/usr/bin/node

// look for the second biggest number in the argv list

const arg = process.argv.slice(2).map(Number);

if (arg.length === 0 || arg.length === 1) {
  console.log('0');
} else {
  const biggest = Math.max(...arg);
  const secondBiggest = Math.max(...arg.filter(x => x < biggest));
  console.log(secondBiggest);
}
