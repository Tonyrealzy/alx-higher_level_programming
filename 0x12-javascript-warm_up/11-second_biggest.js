#!/usr/bin/node

//script that searches the second biggest integer in the list of arguments

let n = process.argv.length;

if (n < 4) {
    console.log('0');
}
else {
    const args = [];
    for (let i = 2; i < n; i++) {
        args[i - 2] = process.argv[i];
    }
    args.sort(function (a, b) {
        return b - a;
    });
    console.log(args[1]);
}