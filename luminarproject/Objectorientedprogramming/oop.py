


class Person:
    def setValues(self,nam,ag):
     self.name=nam
     self.age=ag

    def printValues(self):
      print("age=",self.age)
      print("name=",self.name)

obj=Person()

obj.setValues("ajay",26)
obj.printValues()
