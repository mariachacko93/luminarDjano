


number=[1,2,3,4,5,6]
def squares(num):
     return num*num

#
data=list(map(squares,number))
print(data)
#

# filter even numbers from  list

# def even(num):
#     return num%2==0
# even=list(filter(even,number))
# print(even)
#
# data=list(map(lambda num:num*num,number)
# print(data)


#map function

names=["kkr","dc","kxp","mi","csk"]


data=list(map(lambda data:data.upper(),names))
print(data)


#reduce funstion

from functools import*
numbers=[10,11,12,13,14]
total=reduce(lambda num1,num2:num1+num2,numbers)
print(total)


numbers=[10,11,12,13,14]
max=reduce(lambda num1,num2:num1 if num1>num2 else num2,numbers)
print(max)