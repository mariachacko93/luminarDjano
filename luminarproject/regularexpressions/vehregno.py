import re
#kl22bb1111
vehno=(input("enter the no"))
rule="kl[0-9]{2}[a-z]{1,2}\d{4}"

match=re.fullmatch(rule,vehno)

if(match==None):
    print("Invalid")
else:
    print("Valid")
