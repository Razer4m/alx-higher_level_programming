#!/usr/bin/env node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId]++;
    }
  });
  console.log(completedTasks);
});
