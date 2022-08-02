#!/usr/bin/node

const process = require('process');

const args = process.argv;
const longitude = args.length - 2;

if (longitude === 0) {
  console.log('No argument');
} else if (longitude === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
