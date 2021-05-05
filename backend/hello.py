
import datetime
from datetime import date
import mysql.connector
from mysql.connector import Error

# testing the connection of the database to the mySQL workbench


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


# my information for my AWS database. friend is the name of the table in mySQL workbench
connection = create_connection(
    "cis3368.ckqbw9vznfzb.us-east-2.rds.amazonaws.com", "anwaters", "Chrisbrown3318!", "CIS3368db")
select_results = "SELECT * FROM friend"
# reads and executes the query table of friend, using the connection code as well
friend_table = execute_read_query(connection, select_results)
