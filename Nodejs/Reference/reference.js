/*
MODULES

let stuff = require("./stuff");
console.log(stuff.func1);
console.log(stuff.func2);
console.log(stuff.func3);
*/

/*
EVENT EMITTER

let events = require("events");
let myEmitter = new events.EventsEmitter();
myEmitter.on("someEvent", function(mssg) {
    console.log(mssg);
});
myEmitter.emit("someEvent", "MESSAGE");
*/


/*
READING ,WRTING, AND DELETING FILES

/* Synchronous
let fs = require("fs");
let myReadFile1 = fs.readFileSync("FILENAME", "utf8");
let myWriteFile1 = fs.writeFileSync("FILENAME", "DATA");

/* Asynchronous
let myReadFile2 = fs.readFile("FILENAME", "utf8", function (err, data) { });
let myWriteFile2 = fs.writeFile("FILENAME", "DATA", function (err, data) { });

fs.unlink("FILENAME");
*/


/*
CREATING AND REMOVING DIRS

let fs = require("fs");
fs.mkdir("PATH");
fs.rmdir("PATH");
*/

/*
CREATING A SERVER

let http = require("http");
let server = http.createServer(function (req, res) {
  console.log("request was made" + req.url);
  res.end("");
});
server.listen(3000, "127.0.0.1");
console.log("listening to port 3000");
*/

/*
STREAMS, BUFFERES, AND PIPES

let fs = require("fs");
let myReadStream = fs.createReadStream(__dirname + "/readme.txt", "utf8");
let myWriteStream = fs.createReadStream(__dirname + "/readme.txt", "utf8");
myReadStream.pipe(myWriteStream);
*/

/*
BASIC ROUTING PLUS RETURING HTML AND JSON

let http = require("http");
let fs = require("fs");

let server = http.createServer(function (req, res) {
  console.log("request was made" + req.url);
  if (req.url === "/home" || req.url === "/") {
    res.writeHead(200, { "Content-Type": "text/html" })
    fs.createReadStream(__dirname + "/index.html").pipe(res);
  }
  else if (req.url === "/contact") {
    res.writeHead(200, { "Content-Type": "text/html" })
    fs.createReadStream(__dirname + "/contact.html").pipe(res);
  }
  else if (req.url === "/api") {
    res.writeHead(200, { "Content-Type": "application/json" })
    let people = [{ "name": "ali" }, { "name": "ali" }, { "name": "ali" }];
    res.end(JSON.stringify(people));
  }
  else {
    res.writeHead(200, { "Content-Type": "text/html" })
    fs.createReadStream(__dirname + "/404.html").pipe(res);
  }
});

server.listen(3000, "127.0.0.1");
console.log("listening to port 3000");
*/