#ABABCCC
#find first recursive charecter from list

dict={}
word="ACCCBBABCCC"
let=word.split(",")
for char in word:
    if(char not in dict):
        dict[char]=1
    else:
        print(char, "is the rec value")
        break
