#!/usr/bin/node

exports.esrever = function (list) {
  const newArray = [];

  for (const value of list) {
    newArray.unshift(value);
  }
  return newArray;
};
