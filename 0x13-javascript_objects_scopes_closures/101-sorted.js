#!/usr/bin/node

//script that imports a dictionary of occurrences by user id
//and computes a dictionary of user ids by occurrence

dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];

const newdict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === valsUniq[j]) {
      list.unshift(totalist[k][0]);
    }
  }
  newdict[valsUniq[j]] = list;
}
console.log(newdict);