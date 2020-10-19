
#program to count words:

f=open("wordcount","r")
dict={}
for lines in f:

    lines = lines.rstrip("\n")
    words = lines.split(" ")  #instead we can use
    print(words)
    for word in words:
        word=word.lower()
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
print(dict)