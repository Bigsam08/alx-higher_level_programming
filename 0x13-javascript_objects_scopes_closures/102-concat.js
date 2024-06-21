#!/usr/bin/node
// add two files data and save it into a 3rd file using command-line
const fs = require('fs');
const fileA = fs.readFileSync(process.argv[2], 'utf8');
const fileB = fs.readFileSync(process.argv[3], 'utf8');
const fileC = process.argv[4];
const concatData = fileA + fileB;
fs.writeFileSync(fileC, concatData);
