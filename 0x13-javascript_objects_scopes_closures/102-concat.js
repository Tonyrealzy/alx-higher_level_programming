#!/usr/bin/node

//script that concats 2 files

const fs = require('fs');

const firstArg = fs.readFileSync(process.argv[2]).toString();
const secondArg = fs.readFileSync(process.argv[3]).toString();

fs.writeFileSync(process.argv[4], firstArg + secondArg);