# patternmatching:
string="ababbababababa"
 # count no of ab in given string


import re
pattern="ab"
matcher=re.finditer(pattern,string)
count=0
for match in matcher:

    print(match.start())#will return position of ab
    print(match.group())
    count += 1
print("count=",count)
