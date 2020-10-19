
# method overriding override the parent class name printing with __str__

class Student:
    college_name="Luminar Technolab"
    def __init__(self,rollno,name,total):
        self.rollno=rollno
        self.name=name
        self.total=total

    def printStudent(self):
        print("rollno=",self.rollno)
        print("name=", self.name)
        print("total=", self.total)


    def __str__(self):
        return self.name



obj=Student(1001,"amal",30000)
obj1=Student(1001,"mukul",20000)
print(obj1)
print(obj)
#if we need to print objectname we dont need hexadecimel value
# instead we can assign name to it so we use __str and override the emthod