#!/usr/bin/node

const fs = require('fs');
// const { argv } = require('process');

const args = process.argv;

const content1 = fs.readFileSync(args[2], 'utf8', (err, data) => {
  if (err) console.error(err);
});

const content2 = fs.readFileSync(args[3], 'utf8', (err, data) => {
  if (err) console.error(err);
});

const finalContent = content1 + content2;

fs.writeFileSync(args[4], finalContent, 'utf8', err => {
  if (err) console.error(err);
});
