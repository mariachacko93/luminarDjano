# input list or array

ar=[6,4,5,2,1,3]
flag=0

ar.sort()
print(ar)# sort fn is used to sort
low=0

upper=len(ar)
element=int(input("enter the number to be searched"))


while(low<upper):
  mid=(low+upper)//2  #(0+6)//2
  if(element>ar[mid]):
     low=mid+1

  elif(element<ar[mid]):
     upper=mid-1
  elif(element==ar[mid]):

      flag=1
      break

if(flag>0):
    print("found")
else:
    print(" not found")