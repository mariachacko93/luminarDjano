# #words store in below format:
#
# # while
# # the
# # afternoon
# # matches
# # will
# # start
# # at
# # 3.

f=open("words","r")
words=[]
for lines in f:
    word=lines.rstrip("\n").split(" ")
    for wrd in word:
        words.append(wrd)
# print(words)
    for word in words:
        print(word)
