# use arguments and print datas in covid list

#def print details()


f=open("employee","r")
employee={}
# employee={
#            1001:{id:1001,"name"="ajay","salary"=25000,"exp"=2,"desig"="developer"}
#            1002:{id:1001,"name"="ajay","salary"=25000,"exp"=2,"desig"="developer"}
#            }

for line in f:
    data=line.rstrip("\n").split(",")
    print(data)

    id=data[0]
    name=data[1]
    salary=data[2]
    exp=data[3]
    des=data[4]
    if id not in employee:
        employee[id]={"id":id,"name":name,"salary":salary,"exp":exp,"des":des }

    else:
        pass
# for k ,v in employee.items():
#     print(k,"->",v)

# def getdetails(eid):#not needed
#     if eid in employee:
#         print(employee[id]["name"])
#     else:
#         print("doesnot exist")
# getdetails("1001")


