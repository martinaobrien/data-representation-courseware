import mysql.connector
# This Database is created when you add the name to the last word in cursor execute
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="martinadatarepresentation"

)
cursor = db.cursor()
sql="CREATE TABLE student2(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), AGE iNT)"
cursor.execute(sql)

