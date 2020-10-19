from re import*
pattern="aaaaaaaaabaaabbbbaabbaaaa"
# x="a+" #check single a and sequence of a
# x="a*"
# x="a?"
# x="^a" #check the pattern start with a or not
# x="a$" #check if the given pattern end with a
# x="a{2}" #will check for 2 number of a's
x="a{2,3}" #min 2 a's and max 3 a's

matcher=finditer(x,pattern)
for match in matcher:
 print(match.start(),"position")
 print(match.group())
