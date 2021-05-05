import datetime
import time
import flask
from flask import jsonify
from flask import request, make_response
import mysql.connector
from mysql.connector import Error
import hello
import random

# setting up an application name
app = flask.Flask(__name__)  # sets up the application
app.config["DEBUG"] = True  # allow to show errors in browser

# CRUD FUNCTIONS for friend table

# output all friends in table


@app.route('/api/friends', methods=['GET'])
def listoffriends():
    connection = create_connection(
        "cis3368.ckqbw9vznfzb.us-east-2.rds.amazonaws.com", "anwaters", "Chrisbrown3318!", "CIS3368db")
    cb = connection.cursor()
    sql_db = "SELECT * FROM friend"
    # execute allows the mySQL query parameter to be accepted and then executes the query
    cb.execute(sql_db)
    # fetchall() captures all the records/rows from the cursor object
    table = cb.fetchall()
    # for loop to print all the contacts
    for x in table:
        print(x)
    return jsonify(table)

# adding user to the database


@app.route('/api/addfriend', methods=['POST'])
def addfriend():
    request_data = request.get_json()
    # Requesting the data in postman. input the values and within the brackets are the table columns on the database
    idnum = request_data['id']
    firstname = request_data['firstname']
    lastname = request_data['lastname']
    # database connection code and execution statement
    conn = create_connection("cis3368.ckqbw9vznfzb.us-east-2.rds.amazonaws.com",
                             "anwaters", "Chrisbrown3318!", "CIS3368db")
    query = "INSERT INTO friend (id,firstname, lastname) VALUES ('" + \
        idnum+"','"+firstname+"','"+lastname+"')"
    execute_query(conn, query)
    # return if query successfully executed
    return 'ADDED FRIEND'

# Delete friend from database


@app.route('/api/deletefriend/<int:id>', methods=['DELETE'])
def deletefriend(id):
    # request data
    request_data = request.get_json()
    # connection to the database and sql delete method
    conn = create_connection("cis3368.ckqbw9vznfzb.us-east-2.rds.amazonaws.com",
                             "anwaters", "Chrisbrown3318!", "CIS3368db")
    sql = "DELETE FROM movielist WHERE friendid='%s'" % (id)
    execute_query(conn, sql)
    sql = "DELETE FROM friend WHERE id='%s'" % (id)
    execute_query(conn, sql)
    # return if query successfully executed
    return 'DELETED FRIEND'

# Update friend database


@app.route('/api/updatefriend/<string:id>', methods=['PUT'])
def updatefriend(id):
    # Requesting the data in postman. input the values and within the brackets are the table columns on the database
    request_data = request.get_json()
    firstname = request_data['firstname']
    lastname = request_data['lastname']
    # connection to database code
    conn = create_connection("cis3368.ckqbw9vznfzb.us-east-2.rds.amazonaws.com",
                             "anwaters", "Chrisbrown3318!", "CIS3368db")
    sql = "UPDATE friend SET firstname='%s', lastname='%s' WHERE id='%s'" % (
        firstname, lastname, id)
    execute_query(conn, sql)
    # return if query successfully executed
    return 'UDPATED FRIEND'

# CRUD functions for movielist table

# output all movies


@app.route('/api/movies', methods=['GET'])
def listofmovies():
    connection = create_connection(
        "cis3368.ckqbw9vznfzb.us-east-2.rds.amazonaws.com", "anwaters", "Chrisbrown3318!", "CIS3368db")
    cb = connection.cursor()
    sql_db = "SELECT * FROM movielist"
    # execute allows the mySQL query parameter to be accepted and then executes the query
    cb.execute(sql_db)
    # fetchall() captures all the records/rows from the cursor object
    table = cb.fetchall()
    # for loop to print all the contacts
    for x in table:
        print(x)
    return jsonify(table)


# output all movies


@app.route('/api/movies/<string:friendid>', methods=['GET'])
def listOfMoviesOfFriend(friendid):

    connection = create_connection(
        "cis3368.ckqbw9vznfzb.us-east-2.rds.amazonaws.com", "anwaters", "Chrisbrown3318!", "CIS3368db")
    cb = connection.cursor()
    sql_db = "SELECT firstname,lastname FROM friend WHERE id='%s'" % (
        friendid)
    # execute allows the mySQL query parameter to be accepted and then executes the query
    cb.execute(sql_db)
    # fetchall() captures all the records/rows from the cursor object
    table = cb.fetchall()
    # for loop to print all the contacts
    for x in table:
        print(x)
    return jsonify(table)


# Add movies to the table


@app.route('/api/addmovie', methods=['POST'])
def addmovie():
    # Requesting the data in postman. input the values and within the brackets are the table columns on the database
    request_data = request.get_json()
    idnum = request_data['id']
    friendid = request_data['friendid']
    movie1 = request_data['movie1']
    movie2 = request_data['movie2']
    movie3 = request_data['movie3']
    movie4 = request_data['movie4']
    movie5 = request_data['movie5']
    movie6 = request_data['movie6']
    movie7 = request_data['movie7']
    movie8 = request_data['movie8']
    movie9 = request_data['movie9']
    movie10 = request_data['movie10']
    # database connection code
    conn = create_connection("cis3368.ckqbw9vznfzb.us-east-2.rds.amazonaws.com",
                             "anwaters", "Chrisbrown3318!", "CIS3368db")
    query = "INSERT INTO movielist (id,friendid,movie1,movie2,movie3,movie4,movie5,movie6,movie7,movie8,movie9,movie10) VALUES ('"+idnum+"','" + \
        friendid+"','"+movie1+"','"+movie2+"','"+movie3+"','"+movie4+"','"+movie5 + \
            "','"+movie6+"','"+movie7+"','"+movie8+"','"+movie9+"','"+movie10+"')"
    execute_query(conn, query)
    # return if query successfully executed
    return 'ADDED MOVIES'

# update movie and delete based on friendid
# update can also be used to delete movies in the database in the event a friend does not want to include it anymore


@app.route('/api/updatemovie/<string:id>/<string:friendid>', methods=['PUT'])
def updatemovie(id, friendid):
    # Requesting the data in postman. input the values and within the brackets are the table columns on the database
    request_data = request.get_json()
    movie1 = request_data['movie1']
    movie2 = request_data['movie2']
    movie3 = request_data['movie3']
    movie4 = request_data['movie4']
    movie5 = request_data['movie5']
    movie6 = request_data['movie6']
    movie7 = request_data['movie7']
    movie8 = request_data['movie8']
    movie9 = request_data['movie9']
    movie10 = request_data['movie10']
    # connection code
    conn = create_connection("cis3368.ckqbw9vznfzb.us-east-2.rds.amazonaws.com",
                             "anwaters", "Chrisbrown3318!", "CIS3368db")
    sql = "UPDATE movielist SET movie1='%s', movie2='%s', movie3='%s',movie4='%s', movie5='%s',movie6='%s',movie7='%s',movie8='%s',movie9='%s',movie10='%s' WHERE friendid='%s'" % (
        movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, movie9, movie10, friendid)
    execute_query(conn, sql)
    # return if query executed successfully
    return 'UDPATED MOVIE'

# Random movie selection endpoint
# Randomly selects movie based on movies within the database pool that does not include empty strings


@app.route('/api/movieselection', methods=['GET'])
def movieselect():
    # connection to database code
    conn = create_connection("cis3368.ckqbw9vznfzb.us-east-2.rds.amazonaws.com",
                             "anwaters", "Chrisbrown3318!", "CIS3368db")
    friendsList = request_data['friendsList']
    movielist = []
    for friendid in friendsList:
        sql_db = "SELECT movie1,movie2,movie3,movie4,movie5,movie6,movie5,movie6,movie7,movie8,movie9,movie10 FROM movielist WHERE friendid='%s' ORDER BY rand() LIMIT 1" % (friendid)
        # reads the table to scan for movies
        movies = execute_read_query(conn, sql_db)

        # for loop that will append movies to the empty list
        for x in movies:
            for y in x:
                movielist.append(y)
    movielist_2 = list(filter(None, movielist))
    # random code used to take the length of the movie list - 1 therefore accounting for all 10 rows of movies
    ran_num = random.randint(0, len(movielist_2)-1)
    ran_movie = movielist_2[ran_num]
    # returns movie
    return f'{ran_movie}'


@app.route('/api/movieselectionall', methods=['GET'])
def movieselectAll():
    # connection to database code
    conn = create_connection("cis3368.ckqbw9vznfzb.us-east-2.rds.amazonaws.com",
                             "anwaters", "Chrisbrown3318!", "CIS3368db")
    sql_db = "SELECT movie1,movie2,movie3,movie4,movie5,movie6,movie5,movie6,movie7,movie8,movie9,movie10 FROM movielist ORDER BY rand() LIMIT 1"
    # reads the table to scan for movies
    movies = execute_read_query(conn, sql_db)
    movielist = []
    ran_movie = ""
    # for loop that will append movies to the empty list
    for x in movies:
        for y in x:
            movielist.append(y)
            # removes empty strings from the list so they are not included
            movielist_2 = list(filter(None, movielist))
            # random code used to take the length of the movie list - 1 therefore accounting for all 10 rows of movies
            ran_num = random.randint(0, len(movielist_2)-1)
            ran_movie = movielist_2[ran_num]
    # returns movie
    return jsonify(ran_movie)


# connection code
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    # the try block here is used to test code for errors
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    # except block allows the user to know an error has occured and to fix it
    except Error as e:
        print(f"The error '{e}' occurred")
# the connection code on to see if your DB credentials are correct. Host is the endpoint, user is our user name, password to the DB and Database is the name of the DB we created

    return connection
# executes the query


def execute_query(connection, query):
    cursor = connection.cursor()
    # the try block here is used to test code for errors
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    # except block allows the user to know an error has occured and to fix it
    except Error as e:
        print(f"The error '{e}' occurred")
# returns all the records from the table


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    # the try block here is used to test code for errors
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    # except block allows the user to know an error has occured and to fix it
    except Error as e:
        print(f"The error '{e}' occurred")


app.run()
