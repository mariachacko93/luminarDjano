# input-->3...o/p-->1,2

list=[2,3,4,1,6]
element=int(input("enter the number"))
list.sort()
low=0
# print(len(list))
up=len(list)-1
while(low<up):
    total=list[low]+list[up]
    if(total==element):
        print("pairs=",list[low],",",list[up])
        break
    elif(total>element):
        up=up-1
    elif(total<element):
        low+=1




