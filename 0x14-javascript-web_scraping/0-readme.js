#!/usr/bin/node

const fs = require('fs');
const FilePath = process.argv[2];

fs.readFile(FilePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
