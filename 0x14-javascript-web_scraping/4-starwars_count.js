#!/usr/bin/node
const { get } = require('axios').default;
const url = process.argv[2];

get(url)
  .then(({ data }) => data)
  .then(({ results }) => {
    let count = 0;
    for (const film of results) {
      film.characters.forEach(urls => {
        if (urls.includes('18')) {
          count += 1
        }
      });
    }
    console.log(count);
  })
  .catch((err) => console.log(err));
