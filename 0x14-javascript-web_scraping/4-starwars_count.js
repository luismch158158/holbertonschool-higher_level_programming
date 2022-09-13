#!/usr/bin/node
const { get } = require('axios').default;
const url = process.argv[2];
const urlChar = 'https://swapi-api.hbtn.io/api/people/18/';

get(url)
  .then(({ data }) => data)
  .then(({ results }) => {
    let count = 0;
    for (const film of results) {
      if (film.characters.some(person => urlChar === person)) { count += 1; }
    }
    console.log(count);
  })
  .catch((err) => console.log(err));
