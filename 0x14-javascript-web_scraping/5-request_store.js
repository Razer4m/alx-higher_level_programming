#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(filePath, body, 'utf8', writeErr => {
    if (writeErr) {
      console.error(writeErr);
    }
  });
});
