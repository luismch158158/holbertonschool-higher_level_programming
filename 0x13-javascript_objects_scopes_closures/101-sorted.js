#!/usr/bin/node

const newDict = require('./101-data').dict;

const newArray = Object.entries(newDict);

const newObj = {};

for (const element of newArray) {
  if (newObj[element[1]]) {
    newObj[element[1]].push(element[0]);
  } else {
    newObj[element[1]] = [element[0]];
  }
}

console.log(newObj);
