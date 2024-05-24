const fs = require("fs");

module.exports.readApi = (fileName) => {
  const fileContent = JSON.parse(
    fs.readFileSync("./users/" + fileName + ".json")
  );
  return {
    name: fileContent.name,
    age: fileContent.age,
    job: fileContent.job,
  };
};

module.exports.WriteApi = (name, age, job, filename) => {
  fs.writeFile("./users/" + filename + ".json", "", (err) => {
    if (!err) {
      fs.writeFileSync(
        "./users/" + filename + ".json",
        JSON.stringify({
          name: name,
          age: age,
          job: job,
        })
      );
    }
  });
};
