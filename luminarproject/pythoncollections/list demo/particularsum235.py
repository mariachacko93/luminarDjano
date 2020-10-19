#2,3,5 ...o/p--->8,7,5
#
# list=[2,3,5]
# for item in list:
#     list1=list[1]+list[2]
#     list2= list[0]+list[2]
#     list3 = list[0]+list[1]
#
# print(list1,list2,list3)


#
# list=[2,3,5]
# total=sum(list)
# for i in list:
#     print(total-i)

#
list=[2,3,5]
total=sum(list)
# print(total)
for item in list:
   list1=total-item
   item+=1
   print(list1)


