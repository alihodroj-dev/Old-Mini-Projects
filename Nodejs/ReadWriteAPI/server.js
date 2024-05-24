const express = require("express");
const api = require("./api");
const server = express();
server.listen(3000, "localhost");
console.log("server now live");

server.get("/api", (req, res) => {
  res.send("");
});
