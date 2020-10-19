# bank without staticmethod

class Bank:
    def createAccount(self,accno,nam,banknam,bal):
        self.acc=accno
        self.name=nam
        self.bankname=banknam
        self.balance=bal

    def printBank(self):
        print(self.roll)
        print(self.name)
        print(self.bankname)
        print(self.balance)

    def deposit(self,amount):
     self.balance+=amount
     print("amount ",amount,"credited to your account. availible balance is",self.balance)

    def withdraw(self,amount):
        if(amount>self.balance):
          print("insufficent fund")
        else:
          self.balance-=amount
          print("amount ", amount, "credited to your account. availible balance is", self.balance)

    def balance(self):
        print("your account balance is",self.balance)

obj=Bank()
obj.createAccount(1001,"amal","SBI",5000)
obj.deposit(5000)
# obj.withdraw(10000)