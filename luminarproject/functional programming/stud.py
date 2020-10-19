# class Student:
#     def __init__(self,rollno,name,course,total):
#         self.rollno=rollno
#         self.name=name
#         self.course=course
#         self.total=total
#     def printStudent(self):
#         print("name=",self.name)
#         print("course=", self.course)
#         print("total=", self.total)
#
#     def __str__(self):
#         return (self.name)
#
# f=open("studdet","r")
# lst=[]
# for lines in f:
#     data=lines.rstrip("\n").split(",")
#     print(data)
#     id=data[0]
#     name=data[1]
#     course=data[2]
#     total=int(data[3])
#
#     obj=Student(id,name,course,total)
#
#     lst.append(obj)
#
#
# names=list(map(lambda obj:obj.name.upper(),lst))
# print(names)
#
# # print all students whose total >450
#
# stud=list(filter(lambda obj:obj.total>450,lst))
#
# for st in stud:
#  print(st)
numb=[10,20,30,40]
from functools import*
f=reduce(lambda num1,num2:num1+num2,numb)
print(f)
#

m=reduce(lambda num1,num2:num1 if num1>num2 else num2,numb)
print(m)