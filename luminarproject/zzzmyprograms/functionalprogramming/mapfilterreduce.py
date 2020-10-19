



numbers=[1,2,3,4,5,6]
data=list(map(lambda num:num*num,numbers))
print(data)

data=list(filter(lambda num:num%2==0,numbers))
print(data)

from functools import*
data=list(reduce(lambda num:max(num),numbers))
print(data)


names=["kkc","rrc","mmc"]
data=list(map(lambda names:names.upper(),names))
print(data)






