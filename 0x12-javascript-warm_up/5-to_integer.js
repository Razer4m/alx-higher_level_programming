#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Not a number');
} else {
  const num = parseInt(args[0]);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${num}`);
  }
}
