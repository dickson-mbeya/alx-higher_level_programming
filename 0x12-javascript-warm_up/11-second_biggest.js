#!/usr/bin/node
/*
  Searches second biggest integer in the list
  of arguments
*/
const arg = process.argv;
if (arg.length <= 3) {
  console.log(0);
} else {
  const sorted = arg.sort();
  const secondLargest = sorted[sorted.length - 2];
  console.log(secondLargest);
}
