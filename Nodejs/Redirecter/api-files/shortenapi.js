//imports
const fs = require("fs");
const smallLetterAlphabet = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
];
const capitalLetterAlphabet = [
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
];

function generateURL() {
  generatedURL = "";
  for (i = 0; i < 8; i++) {
    if (Math.floor(Math.random() * 2) == 1) {
      generatedURL =
        generatedURL + smallLetterAlphabet[Math.floor(Math.random() * 25)];
    } else {
      generatedURL =
        generatedURL + capitalLetterAlphabet[Math.floor(Math.random() * 25)];
    }
  }
  return generatedURL;
}

function shortenURL() {
  // reading current urls
  const urlList = JSON.parse(fs.readFileSync("../assets/urls.json"));
  let isUnique = null;
  let url = "";
  let objectList = [];
  for (i = 0; i < Object.keys(urlList).length; i++) {
    objectList.push(urlList["url" + i]);
  }
  // checking uniqueness
  while (isUnique != true) {
    let generatedURL = generateURL();
    for (i = 0; i < Object.keys(urlList).length; i++) {
      if (generatedURL == urlList["url" + i].shortendURL) {
        isUnique = false;
      }
    }
    if (isUnique == false) {
      isUnique = false;
    } else {
      isUnique = true;
      url = generatedURL;
    }
  }
  return url;
}

shortenURL();
