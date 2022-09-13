#!/usr/bin/node
const { get } = require('axios').default;
const urlBase = process.argv[2];
// const complement = "?userId=1&completed=true"

get(`${urlBase}?completed=true`)
  .then(({ data }) => {
    const finalObj = {};
    for (const element of data) {
      const id = element.userId;
      if (finalObj[id]) {
        finalObj[id] += 1;
      } else {
        finalObj[id] = 1;
      }
    }
    console.log(finalObj);
  })
  .catch((err) => console.log(err));
