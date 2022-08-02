#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);

const map1 = list.map((element, idx) => element * idx);
console.log(map1);
