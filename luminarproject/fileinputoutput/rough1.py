# # to print words seperately with commas (in list) and word by word printing
#
# f=open("roughfile","r")
# list=[]
# for lines in f:
#     # print(lines)
#   lines=lines.rstrip("\n")
#   words=lines.split(" ")
#   list.append(words)
#   # print(list)
#
# # for words in list: ###all comes in one line
# #   print(list)
# #   break
#
# for words in list: #all come as paragraph sme like in file with comma seperated
#       print(words)
# for line in words:#word by word printing
#     print(line)
#

# program to count the words in file:




f=open("C:\\Users\\sanal francis\\PycharmProjects\\luminarproject\\fileinputoutput\\words","r")
words=[]
for lines in f:
    # print(lines)
    line=lines.rstrip("\n")

    word=line.split(" ")
    for wrd in word:


      words.append(word)
    for wrd in words:
       print(wrd)


#








# #words count###
#
#
# f=open("wordcount","r")
# dict={}
# for lines in f:
#     # print(lines)
#    words=lines.rstrip("\n").split(" ")
#    for word in words:
#      word=word.lower()
#      if(word not in dict):
#         dict[word]=1
#      else:
#         dict[word]+=1
# print(dict)

# display name of employee and corresponding salary:

# f=open("employee","r")
# for data in f:
#
#   data=data.rstrip("\n").split(",")
#   # print(data)
#   name=data[1]
#   salary=data[2]
#   print(name,",",salary)


# display name of employee and corresponding salary using list:
# f=open("employee","r")
# namelist=[]
# sallist=[]
# for data in f:
#
#   data=data.rstrip("\n").split(",")
#   # print(data)
#   name=data[1]
#   salary=data[2]
#   namelist.append(name)
#   sallist.append(salary)
# print(namelist)
# print(sallist)

# # movies selection yearwise count most repeated movies selection
# f=open("movies.csv","r")
# dict={}
# for data in f:
#     movies=data.rstrip("\n").split(",")
#
#     year=movies[2]
#
#     if(year not in dict):
#         dict[year]=1
#     else:
#         dict[year]+=1
#
# print(dict)
# list=[]
# for k,v in dict.items():
#     # print(k,",",v)
#    list.append((v,k))
# srt=sorted(list,reverse=True)
# print(srt) #print all data in descending order
# print(srt[0]) #print data[0]

#statewise confirmed cases:
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
# # print(list[0])
# #
#
# # print employeename whose id=1001
#
# f=open("employee","r")
# dict={}
# for data in f:
#     # print(data)
#     data=data.rstrip("\n").split(",")
#     id=data[0]
#     name=data[1]
#     salary=data[2]
#     exp=data[3]
#     designation=data[4]
#
#     if(id not in dict):
#      dict[id]={"id":id,"name":name,"salary":salary,"designation":designation}
# # print(dict)
#
# for k,v in dict.items():
#     print(k,"->",v)
#
# def getdetails(eid):
#     if eid in dict:
#         print(dict[eid]["name"])
#     else:
#         print("doesnot exist")
#
#
# getdetails("1001")