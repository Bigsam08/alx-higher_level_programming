#!/usr/bin/node

// factorial with command line arguments

function fact (n) {
  if (isNaN(n) || n === 0 || n < 0 || n === 1) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

const num = parseInt(process.argv[2]);
console.log(fact(num));
