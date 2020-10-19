import re

mobile=input("enter the mobile nunmber")
# rule="[0-9]{10}"
rule="(91)?\d{10}"
#
match=re.fullmatch(rule,mobile)
if(match==None):
  print("Invalid")
else:
  print("Valid")