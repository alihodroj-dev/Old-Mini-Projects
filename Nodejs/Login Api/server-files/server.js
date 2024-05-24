// imports
const express = require("express");
const loginapi = require("../loginapi-files/api");

// setting up the server
const server = express();
server.listen(3000, "localhost");
console.log("server is now listening on port 3000");

// api route
server.get("/loginapi", (req, res) => {
  console.log("api requested");
  res.send(loginapi.api("wdwd", "wdwd"));
});
