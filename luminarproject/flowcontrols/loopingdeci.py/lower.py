#print  lower to upper limit numbers

low=int(input("enter lower"))
up=int(input("enter upper"))
if(low > up):
    print("up should be greater")
while(low <= up):
    print(low)
    low+=1


#if lower limit is 2 and upper limit is 6 .it will print 2,3,4,5,6.