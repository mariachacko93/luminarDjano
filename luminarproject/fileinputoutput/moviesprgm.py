# movies selection yearwise count most repeated movies selection
f=open("movies.csv","r")
dict={}
for data in f:
    movies=data.rstrip("\n").split(",")

    year=movies[2]

    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1

# print(dict)
list=[]
for k,v in dict.items():
    # print(k,",",v)
   list.append((v,k))
srt=sorted(list,reverse=True)
print(srt) #print all data in descending order
print(srt[0]) #print data[0]




#movies rating largest count
#
# f=open("movies.csv","r")
# dict={}
# rating=[]
# for data in f:
#     data=data.rstrip("\n").split(",")
#     rating=data[3]
#
#     if(rating not in dict):
#         dict[rating]=1
#     else:
#         dict[rating]+=1
# list=[]
# for k,v in dict.items():
#     list.append((v,k))
# srt=sorted(list,reverse=True)
# print(srt[0])
#
# #### o/p;
# ###(38776, '')  no rating has highest count
