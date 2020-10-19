
# import re
# # mariachacko93@gmail.com
# gmail=input("enter the gmail ID")
# # rule="[a-zA-Z0-9]*@gmail.com"
# rule="\w*@gmail.com"
# match=re.fullmatch(rule,gmail)
# if(match==None):
#     print("Invalid")
# else:
#     print("Valid")


# gmail id validation

# mariachacko93@gmail.com
import re
rule="\w*@gmail.com"
gmail=input("enter the gmail id")
match=re.fullmatch(rule,gmail)
if(match==None):
    print("Invalid!!please enter valid mail id")
else:
    print("Valid")
