#!/usr/bin/node

const process = require('process');

const args = process.argv;

const number = parseInt(args[2]);

if (Number.isNaN(number)){
  console.log(1);
  return (0);
}

function factorial (number) {
  if (number <= 1){
    return 1;
  }
  return (number * factorial (number - 1));
}

console.log(factorial(number));
