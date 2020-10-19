#print all even numbers btwn lower and upper


low=int(input("enter lower limit"))
up=int(input("enter the upper limit"))
if(low>up):
    print("up limit should be greater")
while(low<=up):
    if(low%2==0):
     print(low)
    low+=1