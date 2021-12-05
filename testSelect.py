import mysql.connector
# This Database is created when you add the name to the last word in cursor execute
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="martinadatarepresentation"

)
cursor = db.cursor()
sql="select * from student2 where id = %s"
values = (1,)
cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
    print(x)

