# selecting max temp form list

dict={}
f=open("temp","r")

fout=open("outputfile.txt","w")

for data in f:
    data=data.rstrip("\n").split(",")
    dist=data[0]
    temp=data[1]
    if temp not in dict:
      dict[dist]=(temp)
    else:
      maxval=max(temp)
      dict[dist]=maxval
# print(dict)
list=[]
for k,v in dict.items():
    list.append((v,k))
    list=sorted(list,reverse=True)
# for item in list:
#     print(item)
    #
for val in list:
    fout.write(str(list))
