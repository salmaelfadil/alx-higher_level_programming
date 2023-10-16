#!/usr/bin/node
const argsL = process.argv.length;
console.log(argsL === 2 ? 'No argument' : argsL === 3 ? 'Argument found' : 'Arguments found');
