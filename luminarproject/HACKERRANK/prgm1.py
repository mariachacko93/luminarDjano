# Given an integer, perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 5 to 20 , print Weird
# If  is even and greater than 20, print Not Weird


# num=int(input("enter the number"))
#
# if(num%2==0):
#      if(2<num<5):
#         print("not weird")
#      elif (5<num<20):
#         print(" weird")
#      elif(num>20):
#          print("not weird")
# elif(num%2!=0):
#     print("weird weird")
#
#
# num=[0,1,2,3,4,5]
# square=[i**2 for i in num]
# print(square)
#
# square=list(map(lambda num:num**2,num))
# print(square)
#
# # leap year
# leap=int(input("enter the year"))
# if(leap%4==0):
#     if(leap%100==0):
#         if(leap%400==0):
#             print("leap year")
# else:
#     print("not leap year")

# # leap year using fun:
# leap=int(input("enter the year"))
# def year(leap):
#  if(leap%4==0):
#     if(leap%100==0):
#         if(leap%400==0):
#             print("leap year")
#  else:
#     print("not leap year")
# year(leap)
#
# #
# i=0
# n=int(input("enter the number"))
# for i in range(0,n):
#  if(n>=0):
#      i+=1
#      print(i)
#

# prime numbers in function in between limits:
def prime(lower,upper):
    flag=0
    for i in range(lower,upper):
        for j in range(2,i):
            if(i%j==0):
                flag=1
                break
            else:
                flag=0
        if(flag==0):
             print(i)

lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
prime(lower,upper)

