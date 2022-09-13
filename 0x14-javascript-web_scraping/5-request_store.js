#!/usr/bin/node

const { writeFile } = require('fs').promises;
const { get } = require('axios').default;
const [, , url, file] = process.argv;

get(url)
  .then(({ data }) => {
    writeFile(file, data, 'utf8');
  })
  .catch((err) => console.log(err));
