#!/usr/bin/node

const process = require('process');

const args = process.argv;
let counter = 0;

const counterFunction = () => counter++;

args.forEach(counterFunction);

if (counter === 2) {
  console.log('No argument');
} else {
  console.log(`${args[2]}`);
}
