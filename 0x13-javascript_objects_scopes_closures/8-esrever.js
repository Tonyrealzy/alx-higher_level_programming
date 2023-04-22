#!/usr/bin/node

//function that returns the reversed version of a list

exports.esrever = function (list) {
    for (let i = 0; i < list.length; i++) {
        list[i] = list[list.length - 1]
    }
}