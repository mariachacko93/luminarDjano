#print largest amoung 3 numbers


a=int(input("enter the value for a"))
b=int(input("enter the value for b"))
c=int(input("enter the value for c"))
if(a>b>c):
    print("a is greater")
elif(b>c>a):
    print("b is greater")
elif(c>b>a):
    print("c is greater")