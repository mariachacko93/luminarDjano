f=open("C:\\Users\\sanal francis\\PycharmProjects\\luminarproject\\fileinputoutput\\completecovid","r")
fout=open("outcovid.txt","w")
dict={}
for data in f:
    # print(data)
    data=data.rstrip("\n").split(",")
    state=data[1]
    cases=float(data[4])
    if state not in  dict:
        dict[state]=cases
    else:
        dict[state]=cases
# print(dict)
list=[]
for k,v in dict.items():
     # print((v,k))
     list.append((v,k))
     list=sorted(list,reverse=True)
print(list)
for val in list:
    fout.write(str(list))