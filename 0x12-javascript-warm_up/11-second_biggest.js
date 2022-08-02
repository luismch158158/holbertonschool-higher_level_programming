#!/usr/bin/node

const process = require('process');
const args = process.argv;
const longitude = process.argv.length - 2;

const newArray = [];
let arraySet;
let finalArray;

for (let i = 0; i < longitude; i++) {
  newArray[i] = parseInt(args[i + 2]);
}

if (longitude === 1 || longitude === 0) {
  console.log(0);
} else {
  arraySet = new Set(newArray);
  finalArray = Array.from(arraySet).sort(function (a, b) {
    return b - a;
  });
  if (finalArray.length === 1) {
    console.log(finalArray[0]);
  } else {
    console.log(finalArray[1]);
  }
}
