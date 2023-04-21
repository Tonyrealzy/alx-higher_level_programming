#!/usr/bin/node

//class Square that defines a square and inherits from Square of 5-square.js

const Square1 = require('/.5-square')

class Square1 extends Square {
    charPrint(c) {
        if (c === undefined) {
            let printout = 'X';
            for (var i = 0; i < w - 1; i++) {
                printout += 'X';
            }
        }
        else {
            let printout = 'c';
            for (var i = 0; i < w - 1; i++) {
                printout += 'c';
            }
        }
        for (var j = 1; j < h; j++) {
            console.log(printout);
        }
    }
}

module.exports = Square;