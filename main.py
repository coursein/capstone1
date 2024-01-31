import mysql.connector as connector
# To create a connection pool, import MySQLConnectionPool class from MySQL Connector/Python.
from mysql.connector.pooling import MySQLConnectionPool
# To find the information on the error, import the Error class from MySQL Connector/Python.
from mysql.connector import Error
from mysql.connector import errorcode

dbconfig = {"user": "mario", "password": "cuisine", "port": 3306, "host": "localhost"}
#db connect
try:
    connection = connector.connect(**dbconfig)
except connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("connection user or password are incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database does not exist")
    else:
        print(err)

create_database_query = """CREATE DATABASE little_lemon"""
use_database_query = """USE little_lemon"""
cursor = connection.cursor()
try:
    cursor.execute(use_database_query)
except connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        cursor.execute(create_database_query)
        cursor.execute(use_database_query)
