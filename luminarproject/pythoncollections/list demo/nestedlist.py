# nested list


employees=[
    [100,"ajay",25000],
    [101,"vijay",22000],
    [102,"binoy",27000],
    [103,"jino",30000]
]

# for data in employees: #to print all data
#     print(data)

# for data in employees:  #to print names only
#     print(data[1])

# calculate sum of salary
total=0
for data in employees:
    total=total+data[2]
print(total)

# # print employee anme slary>25000
# salary=0
# for data in employees:
#      if(data[2]>25000):
#          print(data[1])
#          print(data[2])
