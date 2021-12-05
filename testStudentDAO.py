from studentsDAO import studentDAO
#create

latestid = studentDAO.create(('mark,45))

result = studentDAO,findByID(latestid);
print (result)

#update
studentDAO.update(('Fred', 21, lastestid))
result = studentDAO.findByID(latestid);
print (result)

#get all
allStudents - studentDAO.getAll()
for student in allStudents:
print(student)

# delete

studentDAO.delete(latestid)