
list=[10,11,12,13,14,15]
oddsum=0
evensum=0

for item in list:
 if(item%2==0):
    evensum=evensum+item
 else:
     oddsum=oddsum+item

print(oddsum)
print(evensum)