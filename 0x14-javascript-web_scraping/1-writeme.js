#!/usr/bin/node
const fs = require('fs');
const [, , file, data] = process.argv;

fs.writeFile(file, data, (err) => {
  if (err) {
    console.log(err);
  }
});
