class Employee:
    def __init__(self,id,name,salary,exp,des):
        self.id=id
        self.name=name
        self.salary=salary
        self.exp=exp
        self.des=des

    def printDetails(self):
        print("id=",self.id)
        print("name=",self.name)
        print("salary=",self.salary)
        print("exp=",self.exp)
        print("des=",self.des)

    def __str__(self):
        return self.name

lst=[]
f=open("empdetails","r")
for data in f:
    data=data.rstrip("\n").split(",")
    id=data[0]
    name=data[1]
    salary=int(data[2])
    exp=int(data[3])
    des=data[4]

    obj=Employee(id,name,salary,exp,des)
    lst.append(obj)

maxlist=[]
for obj in lst:
    if(obj.salary>28000):
      print(obj.name,obj.salary)

    maxlist.append(obj.salary)
    maxvalue = max(maxlist)

for obj in lst:

    if(maxvalue==obj.salary):
        print("highest salary",obj.id,"-",obj.name,"-",obj.salary)


#
# # employees whose des is developer
#
#
# develop=list(filter(lambda obj:obj.des=="developer",lst))
# for d in develop:
#  print(d,"developer")
#
#
#  # convert all employeename to upper case:
#
# up=list(map(lambda obj:obj.name.upper(),lst))
# print(up)
# #
# #highest salary
# from functools import*
#
# sal=reduce(lambda salary1,salary2:salary1 if salary1>salary2 else salary2,list(map(lambda obj:obj.salary,lst)))
# print(sal)
#
# #total sal of employees:
# tot=reduce(lambda salary1,salary2:salary1+salary2,list(map(lambda obj:obj.salary,lst)))
# print(tot)


#employees whose des is developer

dev=list(filter(lambda obj:obj.des=="developer",lst))
for obj in dev:
  print(obj.name,obj.des)


# convert all employee to upper case

up=list(map(lambda obj:obj.name.upper(),lst))

print(up)

# find max of salary
from functools import*
maxsal=reduce(lambda  salary1,salary2:salary1 if salary1>salary2  else salary2,list(map(lambda obj:obj.salary,lst)))
print(maxsal)

# find sum of all employees

tot=reduce(lambda salary1,salary2:salary1+salary2,list(map(lambda obj:obj.salary,lst)))
print(tot)

