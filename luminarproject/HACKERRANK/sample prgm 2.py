
def merge(list1,list2):
    list = []
    for i in list1:
        if(i%2==0):
            list.append(i)


    for j in list2:
        if(j%2==0):
            list.append(j)

    print("list",list)
list1=[10,22,33,12,1,3]
list2=[5,6,11,2,99,54,34]


merge(list1,list2)