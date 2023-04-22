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
}

module.exports = Rectangle;