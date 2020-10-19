class Student:
    def setStudent(self,roll,name,total):
        self.roll=roll
        self.name=name
        self.total=total
    def printStudent(self):
        print("roll=", self.roll)
        print("name=",self.name)
        print("total=",self.total)

obj=Student()
obj.setStudent(1,"amal",200)
obj.printStudent()
