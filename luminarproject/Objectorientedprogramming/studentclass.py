class Student:
    def setStudent(self,rollno,nam,cours,tot):
        self.roll=rollno
        self.name=nam
        self.course=cours
        self.total=tot
    def printStudent(self):
        print(self.roll)
        print(self.name)
        print(self.course)
        print(self.total)

obj=Student()
obj.setStudent(100,"amal","mcs",100)
obj.printStudent()

