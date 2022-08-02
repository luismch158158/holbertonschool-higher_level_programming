#!/usr/bin/node

const process = require('process');
const args = process.argv;

const newNumber = Number.parseInt(args[2]);

if (Number.isNaN(newNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${newNumber}`);
}
