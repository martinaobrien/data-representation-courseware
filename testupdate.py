import mysql.connector
# This Database is created when you add the name to the last word in cursor execute
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="martinadatarepresentation"

)
cursor = db.cursor()
sql="update student2 set name= %s, age=%s where id = %s"
values = ("Joe", 33, 1)
cursor.execute(sql, values)

db.commit()
print("update done")
