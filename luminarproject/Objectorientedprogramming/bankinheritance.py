# bank with inheritance

class Person:
    def person(self,name,age):
     self.name=name
     self.age=age

    def personDetails(self):
        print("personname=",self.name)
        print("age=",self.age)


class Bank(Person):
    bank_name="SBI"
    def createBank(self,acc):
        self.acc=acc

        self.balance=3000


    def deposit(self,amount):
        self.balance+=amount
        print("your acc ",Bank.bank_name ,"is credited with amount",amount,"your availible balance=",self.balance)

    def withdraw(self,amount):

        if(amount>self.balance):
            print("insufficent fund")
        else:
            self.balance -= amount
            print("your acc",Bank.bank_name," is debited with amount", amount, "your availible balance is", self.balance)

    def balEnq(self):
        print("your availible balance is", self.balance)

obj=Bank()
obj.createBank(1001)
obj.person("maria",24)
obj.personDetails()
obj.deposit(1000)
obj.wipolthdraw(2000)
obj.balEnq()
