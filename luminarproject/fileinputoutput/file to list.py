file=open("C:\\Users\\sanal francis\\PycharmProjects\\luminarproject\\fileinputoutput\\numbers","r")
list=[]
for numbers in file:
    # print(numbers)

    numbers=int(numbers.rstrip("\n"))    # to remove \n
    list.append(numbers)
print(list)

total=sum(list)
print(total)

large=max(list)
print("largest=",large)

small=min(list)
print("smallest=",small)
