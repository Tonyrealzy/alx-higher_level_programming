#!/usr/bin/node

//script that computes and prints a factorial

const x = process.argv[2];

function factorial(n) {
    if (n === 0) {
        return 1;
    }
    else if (isNaN(n)) {
        return 1;
    }
    else {
        return(n * factorial(n - 1))
    }
}
console.log(factorial(Number(x)));