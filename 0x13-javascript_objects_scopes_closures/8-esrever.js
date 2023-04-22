#!/usr/bin/node

//function that returns the reversed version of a list

exports.esrever = function (list) {
    const newList = [];
    const i = list.length - 1;
    for (let j = 0; i = 0; j++, i--) {
        newList[j] = list[i];
    }
    return newList;
}