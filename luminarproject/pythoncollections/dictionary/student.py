#student dictionary

student={"rollno":1,"name":"ajay","total":55}
print(student)

print(student["name"])

print("college" in student)
student["college"]="luminar technolab"
print(student)

student["total"]+=10
print(student)

for key in student:
    print(key,":",student[key])
