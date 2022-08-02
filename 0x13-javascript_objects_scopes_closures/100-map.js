#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);

const map1 = list.map(element => element * list.indexOf(element));
console.log(map1);
