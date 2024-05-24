// imports
const express = require("express");
const redirectapi = require("../api-files/redirect");

// setting up server
const server = express();
server.listen(3000, "localhost");
console.log("server now live");

// routes
server.get("/", (req, res) => {
  if (req.query.url != "") {
    if (redirectapi.api(req.query.url) != "error") {
      res.status(301).redirect(redirectapi.api(req.query.url));
    } else {
      res.status(404).send("NOT FOUND");
    }
  } else {
    res.status(404).send("NOT FOUND");
  }
});
