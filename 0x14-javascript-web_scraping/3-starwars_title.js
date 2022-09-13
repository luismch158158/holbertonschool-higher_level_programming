#!/usr/bin/node
// const axios = require('axios').default
const { get } = require('axios').default;
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;
get(url)
  .then(({ data: { title } }) => console.log(title))
  .catch((err) => console.log(err));
