# import functionsandmodules.mathmodule
#
# data=functionsandmodules.mathmodule.add(10,20)
# print(data)

from functionsandmodules.mathmodule import *

data=add(10,20)
data1=sub(100,10)
data2=mul(2,3)
data3=div(10,2)
print("add=",data)
print("sub=",data1)
print("mul=",data2)
print("div=",data3)

# module and package
# module:single python file
# package:collection of modules