class Parent1:
    def m1(self):
        print("inside parent 1")

class Parent2:
    def m1(self):
        print("inside parent 2")


class Child(Parent1,Parent2):
    def c1(self):
        print("child")


c=Child()
c.c1()
c.m1()
# c.m2()



# if it has 2 methods of same name then it will calls only the first parent in child fn
