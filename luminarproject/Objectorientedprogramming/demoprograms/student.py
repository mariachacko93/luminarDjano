class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def printStudent(self):
        print("name=",self.name)
        print("course=", self.course)
        print("total=", self.total)

    def __str__(self):
        return (self.name)

f=open("student","r")
list=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    id=data[0]
    name=data[1]
    course=data[2]
    total=int(data[3])

    obj=Student(id,name,course,total)

    list.append(obj)
# ****to print total >450
# for obj in list:
#     if(obj.total>450):
#         # print(obj)
#        print(obj)
# ************* student with max marks*******
total=[]
for obj in list:
    total.append(obj.total)

maxi=max(total)
for obj in list:
    if obj.total==maxi:
        # print(obj)
       print(obj)



