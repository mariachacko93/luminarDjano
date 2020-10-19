# def add(num1,num2)
#     return num1+num2
#
# print(add(10,20))

f=lambda num1,num2:num1+num2
print(f(10,20))
f1=lambda num1,num2:num1-num2
print(f1(10,20))
f2=lambda num1,num2:num1*num2
print(f2(10,20))
f3=lambda num1,num2:num1//num2
print(f3(100,20))

cube=lambda num:num**3
print(cube(3))
