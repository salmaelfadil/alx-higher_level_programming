#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  const elem = list.length - 1;
  for (let i = elem; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
