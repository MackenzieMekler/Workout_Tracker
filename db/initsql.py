import mysql.connector
import os

cnx = mysql.connector.connect(
    user=os.environ["user"],
    password=os.environ["password"],
    host='db',
    port='3307',
    auth-plugin='mysql_native_password'
)

cursor = cnx.cursor()


