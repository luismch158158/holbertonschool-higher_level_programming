#!/usr/bin/node
const { get } = require('axios').default;
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

get(url)
  .then(({ data: { characters } }) => {
    const arrPromise = characters.map(element => get(element));
    Promise.all(arrPromise)
      .then((data) => data.forEach(({ data: { name } }) => console.log(name)));
  })
  .catch((err) => console.log(err));
