#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const result = list.filter(element => element === searchElement);
  return (result.length);
};
