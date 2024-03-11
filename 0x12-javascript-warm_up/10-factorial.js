#!/usr/bin/node

function fact (num) {
  if (num === 0 || isNaN(num)) {
    return (1);
  } else {
    return (num * fact(num - 1));
  }
}

const args = process.argv.slice(2);
const args1 = parseInt(args[0], 10);
console.log(fact(args1));
