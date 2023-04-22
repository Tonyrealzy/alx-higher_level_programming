#!/usr/bin/node

//function that returns the reversed version of a list

exports.esrever = function (list) {
    let newList = []; 
    for (let j = 0; i = list.length - 1; j++, i--) {
        newList[j] = list[i];
    }
    return newList;
}