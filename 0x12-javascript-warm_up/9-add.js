#!/usr/bin/node
/*
  The script prints the addition of 2 integers
  which are command line arguments
*/
const arg = process.argv;
if (arg.length < 4) {
  console.log(NaN);
} else {
  function add (a, b) {
    return a + b;
  }
  console.log(add(Number(arg[2]), Number(arg[3])));
}
