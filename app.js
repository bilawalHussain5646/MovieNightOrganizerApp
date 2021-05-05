var express = require("express");   // Added Express 
var path = require("path");     // Added Path to join views with app
var app = express();            // created app variable 
var routes = require("./routes/routes");      // Created Routes variable & attach routes with the app.js


app.set("port", process.env.PORT || 3000);    // Setup port : 3000


app.set("views",path.join(__dirname,"views"));  // set path views to get ejs files 
app.set("view engine","ejs"); // set ejs to app


app.use(routes)     // add routes to app
app.listen(app.get("port"),function(){      // starting the server at port and console logging message Server is running on port 3000
  console.log("Server is running on port " + app.get("port"))
});