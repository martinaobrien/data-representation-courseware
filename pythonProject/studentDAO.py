import mysql.connector

class StudentDAO:
    db = ""

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            # user="datarep",  # this is the user name on my mac
            # passwd="password" # for my mac
            database="school"
        )

    def create(self, values):
        cursor = self.db.cursor()
        sql = "insert into students (name, age) values (%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from students"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))

        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from students where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql = "update students set name= %s, age=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from students where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames = ['id', 'name', 'age']
        item = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value

        return item


studentDAO = StudentDAO()