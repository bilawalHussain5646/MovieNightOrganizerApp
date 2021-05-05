var express = require('express');   // Added Express
var router = express.Router();      // Added Router Module from Express to create routers
const axios = require('axios')    // added axios to fetch data from api


// IMPORTANT !!!!!
var bodyParser = require('body-parser');    // to fetch data in request.body we use bodyParser
// Compulsory to add so that we can get data

let lastId = 0;                     // Used lastId variable as the database has no autoincrement id 
let Friends;                  // To Store Friends List
let lastIDMovies = 0;       // To be in touch with last id of movies because the id was not autoincrementing in the api. As it was string and not int

async function getUser(url,res) {         // To get friends Data from api we use this function 
  let response
  try {
    response = await axios.get(url);    // used the keyword await so that promise gets complete and then store it to response variable
    Friends = response.data     // fetching response.data and storing in friends
    
    lastId = Friends[Friends.length-1][0];    // Storing lastId of Friend because there is no autoincrement in the api ids
    res.render("friends",{'Friends' : Friends});      // After fetching and storing we send the data to friends router
  } catch (error) {
    console.error(error);
  }
  
}
// Get Friends Request

// Called when we call Movies
async function getFriends(url,res,movies) {
  let response
  try {
    response = await axios.get(url);
    Friends = response.data

    lastId = Friends[Friends.length-1][0];
    res.render("movies",{'Movies' : movies,'Friends': Friends});
  } catch (error) {
    console.error(error);
  }
  
}
// Same for getting Friends for getting Movies Tab  



router.use(bodyParser.json())
.use(bodyParser.urlencoded({
    extended: true
}));
// bodyParser is necessary as it will us to display request.body data



async function getMovies(url,res) {
  let response
  try {
    response = await axios.get(url);
    movies = response.data
    lastIDMovies = movies[movies.length-1][0];
    let urlForFriends = "http://127.0.0.1:5000/api/friends";    // Here we pass the url of the api so that we can fetch the data
    getFriends(urlForFriends,res,movies)    // passing url to getFriends to get Friends and Movies data to Frontend

  } catch (error) {
    console.error(error);
  }
  
}



async function getFriendsForNight(url,res,movies) {
  let response
  try {
    response = await axios.get(url);
    Friends = response.data

    
    res.render("movie-night",{'Movies' : movies,'Friends': Friends});
  } catch (error) {
    console.error(error);
  }
  
}
// This function will Get Friends And Movies Details for Movie Night



async function getMoviesForNight(url,res) {
  let response
  try {
    response = await axios.get(url);
    movies = response.data
    lastIDMovies = movies[movies.length-1][0];
    let urlForFriends = "http://127.0.0.1:5000/api/friends";
    getFriendsForNight(urlForFriends,res,movies)

  } catch (error) {
    console.error(error);
  }
  
}

// This Will Take Movies And Pass it to Friends and pass to Front end 


// Module: Get Friends 
// Status: Completed
router.get("/friends", function(req, res){
  let url = "http://127.0.0.1:5000/api/friends";
  getUser(url,res)
});
// Friends Router, when it is called the url for fetching friends will be passed to getUser Method to fetch friends

// Module: Post Friends 
// Status: Completed
router.post("/submit", function(req, res){
  let url = "http://127.0.0.1:5000/api/addfriend";
  var id= lastId + 1
  var updatedID = toString(id);     // Converting id to string as the api has id of string type
  var firstname = req.body.firstname; 
  var lastname = req.body.lastname;
  // First we take data from Frontend using req.body.firstname ... 

  axios.post(url, {
    id: updatedID,
    firstname: firstname,
    lastname: lastname
  })
  .then(function () {
    res.redirect('/friends');

  })
  .catch(function (error) {
    console.log(error);
  });
});
// Pass the data stored in variable to api and redirect the friends again

// Module: Edit And Delete Friend 
// Status: Completed

router.post("/process", function(req, res){
  var buttonValue = req.body.butt;
    // We fetch the button name either it is edit or delete from frontend so that we can take actions accordingly
  if (buttonValue == "edit"){       // if it is edit
    var id= req.body.id;
    var firstname = req.body.firstname;
    var lastname = req.body.lastname;
    
    let url = "http://127.0.0.1:5000/api/updatefriend/"+id;
    
  // Fetch the data and store in variables 
  // store the api url in url variable for updating friend
  
    axios.put(url, {
      id: id,
      firstname: firstname,
      lastname: lastname
  
    })
    .then(function () {
      res.redirect('/friends');
  
    })
    .catch(function (error) {
      console.log(error);
    });
  }
  // Perform edit functionality

  else if (buttonValue == "remove"){      // if it is remove 
    var id= parseInt(req.body.id)
 
    let url = "http://127.0.0.1:5000/api/deletefriend/"+id;
    
  
   
  
    axios.delete(url, {
      id: id,
  
    })
    .then(function () {
      res.redirect('/friends');
  
    })
    .catch(function (error) {
      console.log(error);
    });
  }
  // we perform delete call from api and redirect to friends
  else{
    res.redirect('/friends');   // else if both are not we redirect it to friends
  }
});

// Module : Process Movies 
// Status : Completed

router.post("/process-movies", function(req, res){
  var buttonValue = req.body.action;
 
  if (buttonValue == "edit"){
    var id= req.body.id;
    var friendid = req.body.friendid;
    var movie1 = req.body.movie1;
    var movie2 = req.body.movie2;
    var movie3= req.body.movie3;
    var movie4= req.body.movie4;
    var movie5 = req.body.movie5;
    var movie6 = req.body.movie6;
    var movie7= req.body.movie7;
    var movie8= req.body.movie8;
    var movie9= req.body.movie9;
    var movie10= req.body.movie10;
    
    let url = "http://127.0.0.1:5000/api/updatemovie/"+id+"/"+friendid;
    
  

  
    axios.put(url, {
      id: id,
      friendid: friendid,
      movie1 : movie1,
      movie2 : movie2,
      movie3: movie3,
      movie4: movie4,
      movie5 : movie5,
      movie6 : movie6,
      movie7: movie7,
      movie8: movie8,
      movie9: movie9,
      movie10: movie10,
      
  
    })
    .then(function () {
      res.redirect('/movies');
  
    })
    .catch(function (error) {
      console.log(error);
    });
  }
  
  else{
    res.redirect('/movies');
  }
});
  // In this Router we used edit functionality for movies when clicked on edit button this Router is called and take movie names and store it in variable and pass it in api call for update
//----------------------------------

// Module: Post Movie 
// Status: Completed
router.post("/submit-movies", function(req, res){
  let url = "http://127.0.0.1:5000/api/addmovie";
  var id= lastIDMovies + 1
  var updatedID = toString(id);
  var friendid = req.body.friendid;
  if (friendid==-1){
    res.redirect('/movies');
  }
  else{
    var movie1 = req.body.movie1;
    var movie2 = req.body.movie2;
    var movie3= req.body.movie3;
    var movie4= req.body.movie4;
    var movie5 = req.body.movie5;
    var movie6 = req.body.movie6;
    var movie7= req.body.movie7;
    var movie8= req.body.movie8;
    var movie9= req.body.movie9;
    var movie10= req.body.movie10;
  
  var lastname = req.body.lastname;


  axios.post(url, {
      id: updatedID,
      friendid: friendid,
      movie1 : movie1,
      movie2 : movie2,
      movie3: movie3,
      movie4: movie4,
      movie5 : movie5,
      movie6 : movie6,
      movie7: movie7,
      movie8: movie8,
      movie9: movie9,
      movie10: movie10,
      
  })
  .then(function () {
    res.redirect('/movies');

  })
  .catch(function (error) {
    console.log(error);
  });
}
});
// This router is called when we click on add movie. It will call the api and store these variables in which we store data from frontend



router.get("/movies", function(req, res){
  let url = "http://127.0.0.1:5000/api/movies";
  getMovies(url,res)

  // Movies Router
});
router.get("/movie-night", function(req, res){
  let url = "http://127.0.0.1:5000/api/movies";
  getMoviesForNight(url,res)
  
  
});
 // Movie Night Router


router.post("/result", function(req, res){
  let url = "http://127.0.0.1:5000/api/movieselectionall";
  getRandomMovie(url,res)
  
});
// Result Router
async function getRandomMovie(url,res) {
  let response
  try {
    response = await axios.get(url);
    MovieName = response.data

    res.render("result",{'MovieName' : MovieName});
  } catch (error) {
    console.error(error);
  }
  
}
// Random Movie Function which which take the random movie from api and store in MovieName variable and pass to front end on result.ejs
router.use(bodyParser.json())
.use(bodyParser.urlencoded({
    extended: true
}));

router.get("/", function(req, res){

  res.redirect("friends");


});
// Default Router


module.exports = router;
