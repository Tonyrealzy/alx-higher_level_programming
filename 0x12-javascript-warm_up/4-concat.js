#!/usr/bin/node

//script that prints two arguments passed to it, in the following format: “ is ”

let arg1 = process.argv[2];
let arg2 = process.argv[3];
console.log(arg1 + " " + arg2);