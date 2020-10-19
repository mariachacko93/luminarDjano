

num=int(input("enter the number"))
res=0
while(num!=0):   #123!=0

     digit=num%10   #123%10
     res=res+digit**3
    # print(digit)   #12.3
     num=num//10     #12
print(res)