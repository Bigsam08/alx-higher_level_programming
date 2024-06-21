#!/usr/bin/node
// a JS that concatenate two files to a destination file.

const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', function (err, data1) {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  fs.readFile(fileB, 'utf8', function (err, data2) {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    const contData = data1 + data2;

    fs.writeFile(fileC, contData, function (err) {
      if (err) {
        console.error(err);
        process.exit(1);
      }

      console.log(`${fileC}`);
    });
  });
});
