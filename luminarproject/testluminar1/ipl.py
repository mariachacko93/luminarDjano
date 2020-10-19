f=open("ipl.txt","r")
team={}
for data in f:
    # print(data)
    data=data.rstrip("\n").split(",")
    no=data[0]
    name=data[1]
    match=data[2]
    win=data[3]
    loss=data[4]
    pts=data[5]
    if(no not in team):
        team[no]={"no":no,"name":name,"match":match,"win":win,"loss":loss,"pts":pts}
    else:
        pass


def teamdetails(**args):
    print(args)
    tno=args["no"]
    print(tno)
    if tno in team:
         print("name=",team[tno]["name"])
         if("prop" in args):
             prope = args["prop"]
             print("property",team[tno]["prope"])

    else:
          print("doesnot exist")



teamdetails(no="2")
teamdetails(no="1",prope=pts)