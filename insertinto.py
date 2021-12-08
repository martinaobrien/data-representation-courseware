import mysql.connector
# This Database is created when you add the name to the last word in cursor execute
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="martinatest"

)
cursor = db.cursor()
sql="insert into student(name, age) values (%s,%s)"
values = ("Mary", 20)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)