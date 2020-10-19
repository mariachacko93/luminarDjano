# multilevel inheritance

class Parent:
    def m1(self):
        print("parent")

class Child(Parent):
    def m2(self):
        print("child")

class Subchild(Child):
    def m3(self):
        print("subchild")

sb=Subchild()
sb.m3()
sb.m2()
sb.m1()


sb1=Child()
sb1.m1()
sb1.m2()
# sb1.m3()#show error
parent=Parent()
parent.m1()
# parent.m2() #shows error
# parent.m3() #shows error