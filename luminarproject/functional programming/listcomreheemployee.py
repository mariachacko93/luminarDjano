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
f=open("C:\\Users\\sanal francis\\PycharmProjects\\luminarproject\\Objectorientedprogramming\\demoprograms\\empdetails","r")
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

# USING LIST COMREHENSION

# employees whose des is developer


#

develop=[obj.name for obj in lst if obj.des=="developer"]
print(develop)


 # convert all employeename to upper case:

em=[obj.name.upper() for obj in lst]
print(em)

#highest salary

high=max([obj.salary for obj in lst])
print(high)

#total sal of employees:
tot=sum([obj.salary for obj in lst])
print(tot)
