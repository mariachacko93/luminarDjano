# # # #binary search
# # #
# # # ar=[2,5,3,4,7,6,1]
# # #
# # #
# # # ar.sort()
# # # print(ar)
# # # low=0
# # # mid=0
# # # flag=0
# # # upper=len(ar)
# # # num=int(input("enter the number"))
# # # while(low<upper):
# # #    mid=(upper+low)//2
# # #    if(num>ar[mid]):
# # #       low=mid+1
# # #    elif(num<ar[mid]):
# # #     upper=mid-1
# # #    elif(num==ar[mid]):
# # #        flag=1
# # #        break
# # #    else:
# # #        flag=0
# # # if(flag==0):
# # #  print("match not found")
# # #
# # # else:
# # #      print(" found")
# # #
# # #
# #
# #
# # # stack
# #
# # stack=[]
# # size=int(input("enter the size"))
# # top=0
# # element=0
# # def push(element):
# #  global top
# #  if(top>=size):
# #      print("stack is full")
# #  else:
# #     stack.append(element)
# #     top+=1
# #
# # def pop():
# #     global top
# #     if(top<0):
# #         print("stack is empty")
# #     else:
# #         top=top-1
# #         print(stack[top])
# #
# # def display():
# #     for i in range(0,top):
# #       print(stack[i])
# # n=1
# # while(n!=0):
# #  option=int(input("choose option 1.push 2. pop 3.display"))
# #  if(option==1):
# #
# #      element=int(input("enter the element"))
# #      push(element)
# #  elif(option==2):
# #      print(" poped")
# #      pop()
# #  elif(option==3):
# #      display()
# # n=int(input("do you want to continue 0/1"))
# #
# #
# #
# #
# n=[]
# l1=[1,2,3,4]
# l2=[4,5,6]
# for i in l1:
#     for j in l2:
#         n.append((i,j))
# print(n)
#
#
# # for squares list comrehension
#
# lst=[1,2,3,4,5,6,7,12,24]
#
# op=[i**2 for i in lst]
# print(op)
# # using map
#
# o=list(map(lambda lst:lst**2,lst))
# print(o)
#
# # evennumbers and odd numbers
#
# odd=[i for i in lst if i%2!=0]
# print(odd)
# eve=[i for i in lst if i%2==0]
# print(eve)
#
# # using listcomre
# nu=[1,4,2,6,7,4]
# op=[x-1 if x<5 else x+1 for x in nu]
# print(op)
# import re
# string="aabababbabaabab"
# pattern="ab"
# matcher=re.finditer(pattern,string)
# count=0
# for match in matcher:
#     count+=1
# print(count)

import re
string="aaababababab"
pattern="ab"
matcher=re.finditer(pattern,string)

count=0
for match in matcher:
    count+=1
    print(match.start())
    print(match.group())
print("count=",count)
