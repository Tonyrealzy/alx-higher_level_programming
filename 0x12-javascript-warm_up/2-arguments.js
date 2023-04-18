#!/usr/bin/node

//It starts on 2 because process.argv contains the whole command-line invocation
//process.argv = ['node', 'yourscript.js', ...]
//Elements 0 and 1 are not "arguments" from the script's point of view, but they are for the shell that invoked the script.

if (process.argv <= 2) {
    console.log("No argument");
}
if (process.argv === 3) {
    console.log("Argument found");
}
if (process.argv > 3) {
    console.log("Arguments found");
}