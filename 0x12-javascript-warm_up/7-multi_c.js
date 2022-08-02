#!/usr/bin/node

const process = require('process');

const args = process.argv;
let numberTimes = Number.parseInt(args[2]);

if (Number.isNaN(numberTimes)) {
  console.log('Missing number of occurrences');
}

while (numberTimes > 0) {
  console.log('C is fun');
  numberTimes--;
}
