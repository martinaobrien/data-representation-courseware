from studentDAO import studentDAO

# create
latestid = studentDAO.create(("mark", 45))

result = studentDAO.findByID(latestid);
print(result)

studentDAO.update(("Fred", 21, latestid))
result = studentDAO.findByID(latestid)
print(result)

# get all
allStudents = studentDAO.getAll()
for student in allStudents:
    print(student)

# delete

studentDAO.delete(latestid)
