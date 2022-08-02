#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

// const args = process.argv;

let content = '';

content += fs.readFileSync(argv[2], 'utf-8', (err, data) => {
  if (err) console.error(err);
});

content += '\n';

content += fs.readFileSync(argv[3], 'utf-8', (err, data) => {
  if (err) console.error(err);
});

fs.writeFileSync(argv[4], content, 'utf-8', err => {
  if (err) console.error(err);
});
