let http = require('http');
let fs = require('fs');
let express = require('express');
let app = express();
let path = require('path');
var mysql = require("mysql")



app.use(express.static(path.join(__dirname, "public")));
// app.use(express.static(__dirname + '/vendor'));


app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

app.post('/m', (req, res) => {
    res.send("POST Request Called");
  });

app.listen(8000, () => {
    console.log("Server started and Listening on port 8000");
  }); 

  //*----------------------------------------------------- */
  var connection = mysql.createConnection({
    host: "127.0.0.1",
    user: "root",
    password: "",  
    // port:"3306",
    database: "techlegate"
})

connection.connect(function(error){
    if(error){
        console.log("error "+error.message)
    } else{
        console.log("Connected")
    } 
})
