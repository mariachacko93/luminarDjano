# # # # # # # odd or even:
# # # # # #
# # # # # #
# # # # # # num=int(input("enter the number"))
# # # # # # flag=0
# # # # # # if(num>0):
# # # # # #   for i in range(2,num):
# # # # # #    if(num%i==0):
# # # # # #
# # # # # #     flag=1
# # # # # #     break
# # # # # #
# # # # # #    else:
# # # # # #     flag=0
# # # # # #
# # # # # # if(flag>0):
# # # # # #     print(" not prime")
# # # # # # else:
# # # # # #     print("  prime")
# # # # # #
# # # # # #
# # # # # # fibonaci series
# # # # #
# # # # # # 0,1,1,2,3,5
# # # # # #
# # # # # # limit=int(input("enter the limit"))
# # # # # # i=1
# # # # # # a=0
# # # # # # b=1
# # # # # # sum=0
# # # # # #
# # # # # # while(i<=limit):
# # # # # #   print(sum)
# # # # # #   i+=1
# # # # # #   a=b
# # # # # #   b=sum
# # # # # #   sum=a+b
# # # # # #
# # # # #
# # # # #
# # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # # search an elment
# # # # # # list=[2,3,4,1,6]
# # # # # # flag=0
# # # # # # search=int(input("enter the element to be searched"))
# # # # # # for item in list:
# # # # # #  if(item==search):
# # # # # #      flag=1
# # # # # #      break
# # # # # #  else:
# # # # # #      flag=0
# # # # # #
# # # # # # if(flag==0):
# # # # # #     print("not found")
# # # # # # else:
# # # # # #     print("found")
# # # # # #
# # # # # #
# # # # # # # square.. cubes:
# # # # # # limit=int(input("enter the limit"))
# # # # # # i=1
# # # # # # count=1
# # # # # #
# # # # # # while(i<=limit):
# # # # # #     count1=count*i
# # # # # #     i+=1
# # # # # #     count+=1
# # # # # #
# # # # # #     print(count1)
# # # # #
# # # # #
# # # # # #stack
# # # # # stack=[]
# # # # # i=0
# # # # # size=int(input("enter the size of stack"))
# # # # # top=0
# # # # # def push(element):
# # # # #     global top
# # # # #     if(top>=size):
# # # # #         print("stack is full")
# # # # #     else:
# # # # #      stack.append(element)
# # # # #      top+=1
# # # # # def pop():
# # # # #     global top
# # # # #     if(top<0):
# # # # #         print("stack is empty")
# # # # #     else:
# # # # #         top=top-1
# # # # #         print(stack[top])
# # # # # def display():
# # # # #     for i in range(0,top):
# # # # #         print(stack[i])
# # # # # n=1
# # # # # while(n!=0):
# # # # #  option=int(input("1.push 2.pop 3.display"))
# # # # #  if(option==1):
# # # # #     element=int(input("enter the element"))
# # # # #     push(element)
# # # # #
# # # # #  elif(option==2):
# # # # #     pop()
# # # # #     print("popped")
# # # # #  elif(option==3):
# # # # #   display()
# # # # # n=int(input("do you want to continue 1/0"))
# # # #
# # # # stack=[]
# # # # size=int(input("enter the size"))
# # # # top=0
# # # # def push(element):
# # # #     global top
# # # #     if(top>=size):
# # # #         print("stack is full")
# # # #
# # # #     else:
# # # #         stack.append(element)
# # # #         top+=1
# # # # def pop():
# # # #     global top
# # # #     if(top<0):
# # # #         print("stack is empty")
# # # #
# # # #     else:
# # # #         top=top-1
# # # #         print(stack[ top])
# # # #
# # # # def display():
# # # #     for i in range(0,top):
# # # #         print(stack[i])
# # # # n=1
# # # # while(n!=0):
# # # #     option=int(input("enter the option"))
# # # #     if(option==1):
# # # #         element=int(input("enter the element"))
# # # #         push(element)
# # # #     elif(option==2):
# # # #         pop()
# # # #     elif(option==3):
# # # #         display()
# # # #
# # # # n=int(input("do you want to continue"))
# # #
# # # stack=[]
# # # size=int(input("enter the size"))
# # # top=0
# # # def push(element):
# # #     global top
# # #     if(top>=size):
# # #         print("stack is full")
# # #     else:
# # #         stack.append(element)
# # #         top+=1
# # # def pop():
# # #     global top
# # #     if(top<0):
# # #         print("stack is empty")
# # #     else:
# # #         top=top-1
# # #         print(stack[top])
# # # def display():
# # #     for i in range(0,top):
# # #         print(stack[i])
# # #
# # # n=1
# # # while(n!=0):
# # #     option=int(input("enter the option 1.push 2.pop 3.display"))
# # #     if(option==1):
# # #        element=int(input("enter the element"))
# # #        push(element)
# # #     elif(option==2):
# # #         pop()
# # #     elif(option==3):
# # #         display()
# # #
# # # n=int(input("do you want to continue 1/0"))
# # #
# # #
# # # binary search
# #
# # ar=[1,5,2,3,8,9]
# #
# # flag=0
# # low=0
# # ar.sort()
# # up=len(ar)-1
# # element=int(input("enter the element"))
# # while(low<up):
# #      mid=(low+up)//2
# #      if(element>ar[mid]):
# #          low=mid+1
# #      elif(element<ar[mid]):
# #          up=mid-1
# #      elif(element==ar[mid]):
# #       flag=1
# #       break
# #
# # if(flag>0):
# #     print("found")
# # else:
# #     print("not found")
# #
# # list=[-1,1,2,4,5]
# # cnt=1
# # for t in list:
# #     if cnt in list:
# #         pass
# #     else:
# #         print(cnt)
# #         break
# #     cnt+=1
# #
# # list=[1,3,2,5,4]
# # item=0
# # search=int(input("enter the number to be searched"))
# # for item in list:
# #     if(item==search):
# #         print("item found")
#
# # employee file:
# f=open("C:\\Users\\sanal francis\\PycharmProjects\\luminarproject\\fileinputoutput\\employee","r")
#
# esal=[]
# ename=[]
# for data in f:
#     data=data.rstrip("\n").split(",")
#     # name=data[1]
#     sal=data[2]
#     # esal.append(sal)
#     ename.append(name)
# print(esal)
# print(ename)

