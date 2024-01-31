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
try:
    cursor.execute("select * from Bookings")

except connector.Error as err:
    if err.errno == 1146:
        exec(open('table_builder.py').read())

#procedure push
get_max_query ="""
 CREATE PROCEDURE GetMaxQuantity()
BEGIN
SELECT max(Quantity) FROM little_lemon.orders;
END
 """


get_manager_query ="""
CREATE PROCEDURE ManageBooking()
BEGIN
SELECT "There is no description of what manage does?? lol.";
END
 """

get_update_query ="""
CREATE PROCEDURE UpdateBooking()
BEGIN 
UPDATE bookings SET guestfirstname = 'Update', guestlastname = 'here' WHERE bookingid = 1;
END
 """

get_cancel_query ="""
CREATE PROCEDURE CancelBooking()
BEGIN 
DELETE FROM bookings where bookingid = 1;
END
 """
#execute create scripts
cursor.execute(get_max_query)
cursor.execute(get_manager_query)
cursor.execute(get_update_query)
cursor.execute(get_cancel_query)

#cursor.callproc('getmaxquantity')
#cursor.callproc('managebooking')
#cursor.callproc('updatebooking')
#cursor.callproc('cancelbooking')
#connection.commit()