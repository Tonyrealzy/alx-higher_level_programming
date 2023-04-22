#!/usr/bin/node

//class Rectangle that defines a rectangle

class Rectangle {
    constructor(w, h){
        if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
        }
    }
    print() {
        let printout = 'X';
        for (let i = 0; i < w - 1; i++) {
            printout += 'X';
        }
        for (let j = 1; j < h; j++) {
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