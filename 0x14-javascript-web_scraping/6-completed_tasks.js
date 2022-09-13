#!/usr/bin/node
const { get } = require('axios').default;
const urlBase = process.argv[2];


get(urlBase)
  // data es un array de objetos
  .then(({ data }) => {
    const finalObj = {};
    data.forEach(({ userId, completed }) => {
      if (completed) {
        if (finalObj[userId] === undefined) {
          finalObj[id] = 1;
        } else {
          finalObj[id] += 1;
        }
      }
    })
    console.log(finalObj);
  })
  .catch((err) => console.log(err));
