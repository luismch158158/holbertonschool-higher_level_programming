#!/usr/bin/node

exports.converter = function (base) {
  return function myConverter(a) {
    return (a.toString(base));
  }
}
