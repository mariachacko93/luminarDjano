# text="hello,hai,hello,hai,how"
#o/p--hello -2,hai-2,how-1


text="hello,hai,hello"
words=text.split(",")

dict={}

for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)