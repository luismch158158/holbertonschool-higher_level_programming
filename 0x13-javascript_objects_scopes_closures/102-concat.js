#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

// const args = process.argv;

let content = '';

content += fs.readFileSync(argv[2], 'utf8', (err, data) => {
  if (err) console.error(err);
});

content += '\n';

content += fs.readFileSync(argv[3], 'utf8', (err, data) => {
  if (err) console.error(err);
});

content += '\n';

fs.writeFileSync(argv[4], content, 'utf8', err => {
  if (err) console.error(err);
});
