
f=open("ipl.txt","r")

ipl={}
for data in f:
    data=data.rstrip("\n").split(",")
    no=data[0]
    name=data[1]
    match=data[2]
    win=data[3]
    loss=data[4]
    points=data[5]
    if no not in ipl:
        ipl[no]={"no":no,"name":name,"match":match,"win":win,"loss":loss,"points":points}
    else:
        pass

def ipldetails(**args):
    no=args["no"]
    prop=args["prop"]
    print("values", ipl[no]["name"])
    print("values",ipl[no][prop])

# ipldetails(no="3")
ipldetails(no="3",prop="loss")