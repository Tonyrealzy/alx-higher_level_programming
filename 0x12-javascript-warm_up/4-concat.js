#!/usr/bin/node

//script that prints two arguments passed to it, in the following format: “ is ”

var args = process.argv[2];
console.log(args[0] + " " + args[1]);