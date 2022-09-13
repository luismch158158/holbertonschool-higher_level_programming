#!/usr/bin/node
const axios = require('axios').default;
const url = process.argv[2];

axios.get(url)
  // Antes:
  // .then((response) => console.log(`code: ${response.status}`))
  // Con destructuring seria asi:
  // Ya se sabe porque el objeto response esta dentro del response es
  // como hacer esto:
  // const { status } = response;
  .then(({ status }) => console.log(`code: ${status}`))
  // Otra forma de hacer es esta:
  //  .catch((err) => console.log(`code: ${err.response.status}`));
  // Pero con destructuring seria asi:
  // Ya se sabe porque el objeto err esta dentro del catch es
  // como hacer esto:
  // const { response } = err;
  .catch(({ response }) => console.log(`code: ${response.status}`));
