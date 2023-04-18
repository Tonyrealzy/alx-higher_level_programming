#!/usr/bin/node

//script that prints a square

const mySize = process.argv[2];
let rows = 'X';

if (isNaN(Number(mySize))){
    console.log("Missing size")
}
else {
    for (let i = 0; i < mySize - 1; i++){
        rows += 'X';
        for (let j =0; j < mySize; j++){
            console.log(rows);
        }
    }
}