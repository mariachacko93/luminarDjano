# display name and corresponding salary

f=open("employee","r")
namelist=[]
sallist=[]
for employees in f:
    # print(employees)
    line=employees.rstrip("\n")
    data=line.split(",")
    # employee=employees.name
        # print(data)
    name=data[1]
    sal=data[2]
    namelist.append(name)
    sallist.append(sal)
print(namelist)
print(sallist)
