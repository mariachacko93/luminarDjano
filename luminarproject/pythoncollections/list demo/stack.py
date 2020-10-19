# stack

#  
# stack full program

stack=[]
size=int(input("enter the size"))
top=0
element=0
def push(element):
 global top
 if(top>=size):
     print("stack is full")
 else:
    stack.append(element)
    top+=1

def pop():
    global top
    if(top<0):
        print("stack is empty")
    else:
        top=top-1
        print(stack[top])

def display():
    for i in range(0,top):
      print(stack[i])
n=1
while(n!=0):
 option=int(input("choose option 1.push 2. pop 3.display"))
 if(option==1):

     element=int(input("enter the element"))
     push(element)
 elif(option==2):
     print(" poped")
     pop()
 elif(option==3):
     display()
n=int(input("do you want to continue 0/1"))