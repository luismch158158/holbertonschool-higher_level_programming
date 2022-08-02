#!/usr/bin/node

const process = require('process');

const args = process.argv;
const numberTimes = Number.parseInt(args[2]);

if (Number.isNaN(numberTimes)) {
  console.log('Missing size');
}

for (let i = 0; i < numberTimes; i++) {
  for (let j = 0; j < numberTimes; j++) {
    process.stdout.write('X');
  }
  console.log();
}
