#!/usr/bin/node

const process = require('process');

const args = process.argv;

function add (a, b) {
  console.log(`${a + b}`);
}

const a = parseInt(args[2]);
const b = parseInt(args[3]);

add(a, b);
