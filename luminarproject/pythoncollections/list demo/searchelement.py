#linear search


list=[1,2,3,4,5,6,7,8,9]
search=int(input("serach element"))
flag=0
for item in list:
    if(item==search):
      flag+=1
      break
    else:
      flag=0


if(flag>0):
    print("element found")
else:
    print("element not found")
