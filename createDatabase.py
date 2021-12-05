import mysql.connector
# This Database is created when you add the name to the last word in cursor execute
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"

)
cursor = db.cursor()
cursor.execute("CREATE DATABASE DEF")

