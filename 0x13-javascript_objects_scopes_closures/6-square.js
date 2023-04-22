#!/usr/bin/node

//class Square that defines a square and inherits from Square of 5-square.js

const Square1 = require('./5-square')

class Square extends Square1 {
    charPrint(c) {
        let printout = ' ';
        for (let i = 0; i < this.width; i++) {
            printout += 'c';
        }
        if (c === undefined) {
            c = 'X';
        }
        for (let j = 0; j < this.height; j++) {
            console.log(printout);
        }
    }
}

module.exports = Square;