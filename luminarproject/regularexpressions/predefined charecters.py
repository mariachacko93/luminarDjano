import re

#predefined charecter sets:

x="[abc]" #it will check for either a,b,c is present in the string
# x="[a-z]"
# x="[0-9]"
# x="[A-Z]"
# x="[a-zA-Z]"
# x="[a-z0-9]"
#x=[a-zA-Z0-9]" #will check for all words exept special charecters
# x="[^a-zA-Z0-9]" all special charecters exept words
# x="[^0-9]" exept numbers

#predefined charecters:

# x="\s" #to check for space[^
# x="\d" # to check for digits
# x="\D" #print all exept digit ie. [^0-9]
# x="\w" # chek for words both lower and upper and numbers also no special charecter in it [a-zA-Z0-9]
# x="\W" #check for special charecters only ie exept words [^a-zA-Z0-9]

matcher=re.finditer(x,"ab7 c@KZ")
for match in matcher:
    print(match.start(),"position")
    print(match.group())