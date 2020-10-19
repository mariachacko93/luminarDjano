# polymorphism
#
#
# method overloading
# methodoverrriding
# operateroverloading

class Parent:
     def phone(self):
         print("nokia")

class Child(Parent):
    def phone(self):
        print("iphone")

c=Child()
c.phone()
