from studentsDAO import studentDAO

# create

latestid = studentDAO.create(("JUNE", 18))

result = studentDAO.findByID(latestid);
print(result)

#studentDAO.update(("Fred", 21, latestid))
#result = studentDAO.findByID(latestid)
#print(result)

# get all
#allStudents = studentDAO.getAll()
#for student in allStudents:
    #print(student)

# delete

studentDAO.delete(latestid)
