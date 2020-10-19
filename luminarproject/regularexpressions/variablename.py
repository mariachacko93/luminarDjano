# first word should be for a to z
# second should be divisible by 3
# 3rd  should be any word



import re
rule="[a-k][3,6,9][a-z0-9A-z]*"
pattern=input("enter the pattern")

match=re.fullmatch(rule,pattern)
if(match==None):
    print("Invalid")
else:
    print("Valid")