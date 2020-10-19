# def person(**args):
#     print(args)
# person(name="ajay",location="ekm",city="varapuzha")


f=open("C:\\Users\\sanal francis\\PycharmProjects\\luminarproject\\fileinputoutput\\employee","r")
emp={}
for data in f:
    data=data.rstrip("\n").split(",")
    id=data[0]
    name=data[1]
    sal=data[2]
    exp=data[3]
    pos=data[4]
    if id not in emp:
        emp[id]={"id":id,"name":name,"sal":sal,"pos":pos}
    else:
        pass

print(emp)

for k,v in emp.items():
    print(k,v)

#
# def empdetails(eid):
#     # # print(args)
#
#     if eid in emp:
#       print(emp[eid]["name"])
#     else:
#       print("employee doesnot exist")
#

# empdetails("1001")   #or we can write as empdetails(eid="1001")


def empdetails(**args):
   print(args)
   eid=args["id"]

   print(eid)
   if eid in emp:
       print("name=",emp[eid]["name"])

       if "prop" in args:
           prope = args["prop"]
           print("values",emp[eid][prope])
   else:
       print("doesnot exist" )

empdetails(id="1001")
# empdetails(id="1001",prop="sal")
empdetails(id="1002",prop="pos")


# def empdetails(**args):
#    print(args)
#    eid=args["id"]
#
#    if "prop" in args:
#        prope = args["prop"]
#
#        print("name=",emp[eid]["name"])
#
#            print("values",emp[eid][prope])
#
# # empdetails(id="1001 ")
# empdetails(id="1001",prop="salary")