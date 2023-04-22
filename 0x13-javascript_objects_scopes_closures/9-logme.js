#!/usr/bin/node

//function that prints the number of arguments already printed and the new argument value

exports.logMe = function (item) {
    for (let i = 2; i < arguments.length; i++) {
        console.log('i: ' + arguments[i]);
    }
}