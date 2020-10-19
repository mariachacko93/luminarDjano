# #define dictionary
#
# dict={}
#
# values stored in dictionary in for of key:value pairs
#
# in list list=[101,"ajay",25000]
#
# here           ID  name   salary

# in dictionary-
employee={"id":101,"name":"ajay","salary":25000}

# duplicate key is not allowed
# store same and different datas
# duplicate value is allowed
print(employee)
# to acess any
# not use index position use inly keys
#
# print employee name only
print(employee["name"])
# if we want
# adding other
employee["gender"]="male"
print(employee)

# update salary

employee["salary"]+=5000
print(employee)

# checking for specific key

print("desig" in employee)