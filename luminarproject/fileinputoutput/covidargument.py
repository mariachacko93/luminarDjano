

f=open("completecovid","r")
covid={}
for data in f:
  # print(data)

  data=data.rstrip("\n").split(",")
  # print(data)
  state=data[1]
  death=[4]
  cases=float(data[3])
  cured=(data[5])

  if state not in covid:
      covid[state]={"state":state,"death":death,"cases":cases,"cured":cured }
  else:
      pass
for k,v in covid.items():
      print(k,"->",v)


def getdetails(cstate):
    if cstate in covid:
      print(covid[state]["cases"])


getdetails("kerala")








