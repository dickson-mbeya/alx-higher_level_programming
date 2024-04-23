#!/usr/bin/node
const arg = process.argv;
function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (arg.length > 2) {
  console.log(factorial(Number(arg[2])));
} else {
  console.log(factorial(1));
}
