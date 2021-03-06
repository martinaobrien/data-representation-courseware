import mysql.connector
class StudentDAO:
    db =""
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            # user="datarep",  # this is the user name on my mac
            # passwd="password" # for my mac
            database="martinatest"
        )
    def create(self, values):
        cursor = self.db.cursor()
        sql = "insert into student (name, age) values (%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from student"
        cursor.execute(sql)
        results = cursor.fetchall()
        #return result
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            resultAsDict = self.convertToDictionary(result)
        #returnArray.append(self.convertToDictionary(result))
            returnArray.append(resultAsDict)
        return returnArray
        #return result
    
    def findByID(self, id):
        #return{}
        cursor = self.db.cursor()
        sql = "select * from student where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return result
        return self.convertToDictionary(result)

    def update(self, student):
        #return student
        cursor = self.db.cursor()
        sql = "update student set name= %s, age=%s  where id = %s"
        values = [
            student['name'],
            student['age'],
            student['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()

    def delete(self, id):
        #return{}
        cursor = self.db.cursor()
        sql = "delete from student where id = %s"
        values = (id,)
        cursor.execute(sql, values)

        #return {}
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