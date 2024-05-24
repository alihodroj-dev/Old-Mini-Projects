// imports
const fs = require("fs");

module.exports.api = function (givenCode) {
  const urlList = JSON.parse(fs.readFileSync("../assets/urls.json"));
  redirectURL = "";
  for (i = 0; i < Object.keys(urlList).length; i++) {
    let key = Object.keys(urlList)[i];
    if (key == givenCode) {
      redirectURL = urlList[key];
    }
  }
  if (redirectURL != "") {
    return redirectURL;
  } else {
    return "error";
  }
};
