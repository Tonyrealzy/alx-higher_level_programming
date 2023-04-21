#!/usr/bin/node

//class Rectangle that defines a rectangle

class Rectangle {
    constructor(width, height){
        this.width = w;
        this.height = h;
        if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
        }
    }
    print() {
        let printout = 'X';
        for (var i = 0; i < w - 1; i++) {
            printout += 'X';
        }
        for (var j = 1; j < h; j++) {
            console.log(printout);
        }
    }
    rotate() {
        const spec = this.width;
        this.width = this.height;
        this.height = spec;
    }
    double() {
        this.width *= 2;
        this.height *= 2;
    }
}

module.exports = Rectangle;