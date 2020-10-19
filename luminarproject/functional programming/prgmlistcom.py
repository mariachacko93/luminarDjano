# program posssible pairs.

# lst=[]
# l=[1,2,3]
# l2=[4,5,6]
# ### for i in l:
###    for j in l2:
###       lst.append((i,j))
### print(lst)
#
# op=[(i,j) for i in l for j in l2]
# print(op)

lst=[1,2,3,4,5]
sq=[num**2 for num in lst]
print(sq)

even=[num for num in lst if num%2==0]
print(even)


out=[i+1 if i>5 else i-1 for i in lst]
print(out)

# if element <5 minus 1 and greater than 5 add 1 using map
nu=[1,4,2,6,7,4]

op=list(map(lambda i:i-1 if i<5 else i+1,nu))
print(op)

# using listcomre
nu=[1,4,2,6,7,4]
op=[x-1 if x<5 else x+1 for x in nu]
print(op)
