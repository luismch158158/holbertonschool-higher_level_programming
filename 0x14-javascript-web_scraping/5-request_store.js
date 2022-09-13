#!/usr/bin/node

const { writeFile } = require('fs');
const { get } = require('axios').default;
const [, , url, file] = process.argv;

get(url)
  .then(({ data }) => {
    writeFile(file, data, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  })
  .catch((err) => console.log(err));
