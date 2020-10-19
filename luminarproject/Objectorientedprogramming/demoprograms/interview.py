# # #
# # # string="HEY" o/p-HEEYYY
# # # cnt=1
# # # data=""
# # # for char in string:
# # #     data+=cnt*char
# # #     cnt+=1
# # # print(data)
# #
# # #
# x=5
# nlist=[]
# list=[3,1,4,6,5,7,10,2]
# for i in list:
#     if(i<x):
#         i-=1
#         nlist.append(i)
#     elif(i>x):
#         i+=1
#         nlist.append(i)
#
# print(nlist)
#
# # string = "HEYMAN"
# # # o / p - HEEYYY
# # i=1
# # data=""
# # for char in string:
# #    data+=char*i
# #    i+=1
# # print(data)
#
# #
# # #/********my method****#
# # string = "HEYMAN"
# # # o / p - HEEYYY
# # i=1
# # for char in string:
# #    char=char*i
# #    i+=1
# #    print(char)
#
#
#
#
# # to [rint 5 also in list]
# list=[4,1,2,5,6,7]
#
# nlist=[]
# for i in list:
#    if(i<5):
#       i-=1
#       nlist.append(i)
#    elif(i>5):
#       i+=1
#       nlist.append(i)
#    elif(i==5):
#        nlist.append(i)
# print(nlist)
#

# # print all pairs
# lst=[]
# l=[1,2,3]
# l2=[4,5,6]
# for i in l:
#    for j in l2:
#       lst.append((i,j))
# print(lst)
#
# data="hhhppsdaaa"
# dict={}
#
# for char in data:
#  if char not in dict:
#
#     dict[char]=1
#  else:
#      dict[char]+=1
#
# print(dict)
#
# op=""
# for k,v in dict.items():
#     op=op+str(v)+k
#     # list.append((k,v))
# print(op)

dict={}
data="hhhppsdaaa"
for char in data:
    if char not in dict:
        dict[char]=1
    else:
        dict[char]+=1
print(dict)
op=""
for k,v in dict.items():
    op=op+str(v)+k
print(op)







