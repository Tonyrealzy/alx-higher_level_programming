#!/usr/bin/node

//class Rectangle that defines a rectangle

const Rectangle = require('./4-rectangle');

class Rectangle extends Square {
    constructor(size) {
        super(size, size)
    }
}

module.exports = Square;