#!/usr/bin/node
// print the arg passed to the commandline without using the length function

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
