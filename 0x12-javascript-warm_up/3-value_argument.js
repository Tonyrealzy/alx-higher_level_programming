#!/usr/bin/node

//process.argv = ['node', 'yourscript.js', ...]
//Elements 0 and 1 are not "arguments" from the script's point of view, but they are for the shell that invoked the script.

if (process.argv[2]) {
    console.log(process.argv[2]);   
}
else {
    console.log("No argument");
}