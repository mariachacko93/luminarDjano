# #statewise confirmed cases:
#
# f=open("completecovid","r")
# dict={}
# for lines in f:
#
#     data=lines.rstrip("\n").split(",")
#     state=data[1]
#     cases=float(data[4])
#     if(state not in dict):
#         dict[state]=cases
#     else:
#         dict[state]=cases
# # print(dict)
# list=[]
# for k,v in dict.items():
#     # print(k,",",v)
#
#     list.append((v,k))
#     list=sorted(list,reverse=True)
# print(list[0])


#statewise confirmed cases: to write o/p in seperate file:


f=open("completecovid","r")
fout=open("covideoutputfile.txt","w")
dict={}
for lines in f:

    data=lines.rstrip("\n").split(",")
    state=data[1]
    cases=float(data[4])
    if(state not in dict):
        dict[state]=cases
    else:
        dict[state]=cases
# print(dict)
list=[]
for k,v in dict.items():
    # print(k,",",v)

    list.append((v,k))
    list=sorted(list,reverse=True)
print(list[0])
for val in list:
    fout.write(str(list))





