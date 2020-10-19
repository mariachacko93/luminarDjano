# import re
# # mariachacko93@gmail.com
#
# # gmail=input("enter the gmail ID")
#
# rule="\w*@gmail.com"
# # rule="[a-zA-Z0-9]*@gmail.com"
#
# list=[]
#
# f=open("gmailtext","r")
# fout=open("gmailop.txt","w")
#
# for data in f:
#     data=data.rstrip("\n")
#
#     match=re.fullmatch(rule,data)
#     if(match==None):
#         print(data,"is invalid")
#     else:
#      print(data,"is Valid")
#      list.append(data)
#
# # for val in list:
# #      print(val)
# fout.write(str(list))
#

# validate ids only to new txt doc
#
# import re
# # mariachacko93@gmail.com
#
# rule="\w*@gmail.com"
# # rule="[a-zA-Z0-9]*@gmail.com"
#
# list=[]
#
# f=open("gmailtext","r")
# fout=open("gmailop.txt","w")
#
# for data in f:
#     data=data.rstrip("\n")
#
#     match=re.fullmatch(rule,data)
#     if(match!=None):
#      list.append(data)
#
# fout.write(str(list))