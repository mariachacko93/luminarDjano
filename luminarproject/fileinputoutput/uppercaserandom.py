f=open("random","r")
for lines in f:
   # print(lines)
   line=lines.rstrip("\n")
   # print(line)
   words=line.split(" ")
   print(words)
   for wrd in words:
       print(wrd.upper())