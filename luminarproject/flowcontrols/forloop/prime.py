
#prime or not
number=int(input("enter the number"))
flag=0
for i in range(2,number):
    if(number%i==0):
      flag=1
      break
    else:
      flag=0

if(flag>0):
    print("not prime")
else:
    print("prime")







