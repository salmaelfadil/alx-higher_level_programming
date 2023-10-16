#!/usr/bin/node
const argLength = process.argv.length;
if (argLength <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number).slice(2, argLength).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
