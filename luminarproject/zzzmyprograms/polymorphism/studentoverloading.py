class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total

    def printDetails(self):
        print("rollno=",self.rollno)
        print("name=",self.name)
        print("course=",self.course)
        print("total=",self.total)

    def __str__(self):
        return self.name

f=open("studdetails","r")
list=[]

for data in f:
    data=data.rstrip("\n").split(",")
    print(data)
    rollno=data[0]
    name=data[1]
    course=data[2]
    total=int(data[3])
    obj=Student(id,name,course,total)
    list.append(obj)
totlist=[]
for obj in  list:
    if(obj.total>450):
        print(obj.name,"-",obj.total)
    totlist.append(obj.total)
maxval=max(totlist)
for obj in list:
  if(obj.total==maxval):
     print(maxval,"-",obj.name)


