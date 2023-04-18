#!/usr/bin/node

//script that prints the addition of 2 integers

a1 = process.argv[2];
b1 = process.argv[3];

function add(a, b) {
    return(a + b);
}
console.log(add(a1, b1));