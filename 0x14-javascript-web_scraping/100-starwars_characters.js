#!/usr/bin/node
const { get } = require('axios').default;
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

get(url)
  .then(({ data: { characters } }) => {
    characters.forEach(element => {
      get(element)
        .then(({ data: { name } }) => {
          console.log(name);
        })
        .catch((err) => console.log(err));
    });
  })
  .catch((err) => console.log(err));
