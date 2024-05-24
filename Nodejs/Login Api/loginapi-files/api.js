// imports
const fs = require("fs");

// reading the users from users.json
const userList = JSON.parse(fs.readFileSync("../users/users.json"));

// exporting the api
module.exports.api = function api(givenEmail, givenPassword) {
  if (givenEmail != "" && givenPassword != "") {
    loggedIn = false;
    currentUserIndex = null;
    for (i = 0; i < Object.keys(userList).length; i++) {
      user = userList["user" + i];
      if (user.email == givenEmail) {
        if (user.password == givenPassword) {
          loggedIn = true;
          currentUserIndex = i;
        }
      }
    }
    if (loggedIn == true) {
      let loggedInUser = {
        username: userList["user" + currentUserIndex].username,
        role: userList["user" + currentUserIndex].role,
      };
      return loggedInUser;
    } else {
      return "the credentails entered are wrong";
    }
  } else {
    if (givenEmail != "" && givenPassword == "") {
      return "no password enetered";
    }
    if (givenPassword != "" && givenEmail == "") {
      return "no email enetered";
    }
    return "no credentials entered";
  }
};
