f=open("completecovid","r")
dict = {}
for data in f:

    data=data.rstrip("\n").split(",")
    # print(data)

    cases=float(data[4])
    state=data[1]
    if state not in dict:
        dict[state]=cases
    else:
        dict[state]+=cases
# print(dict)
list=[]
for k,v in dict.items():
    list.append((v,k))
    list=sorted(list,reverse=True)
print(list[0])