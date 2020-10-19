# creating bank operation using class #bank name is defined  as instance variable ie used everywhere to read

# class Bank:
#     def createBank(self,acc,name,bankname,balance):
#         self.acc=acc
#         self.name=name
#         self.bankname=bankname
#         self.balance=balance
#
#     def deposit(self,amount):
#         self.balance+=amount
#         print("your acc is credited with amount",amount,"your availible balance=",self.balance)
#
#     def withdraw(self,amount):
#
#         if(amount>self.balance):
#             print("insufficent fund")
#         else:
#             self.balance -= amount
#             print("your amount is debited with amount", amount, "your availible balance is", self.balance)
#
#     def balEnq(self):
#         print("your availible balance is", self.balance)
#
# #************no need to print details,you can if needed***********##
#     def printBank(self):
#         print("account=",self.acc)
#         print("name=",self.name)
#         print("bankname=",self.bankname)
#         print("availible balance=",self.balance)
# #**********************************************************#
#
# obj=Bank()
# obj.createBank(1001,"maria","SBI",3000)
# obj.deposit(1000)
# obj.withdraw(2000)
# obj.balEnq()
# obj.printBank()

# all operations works at same time but ..perform any one action at a time.. same llike in bank system


# we can use bank name as static, instead of writing  bank name everywhere,instead of calling evertime:

class Bank:
    bank_name="SBI"
    def createBank(self,acc,name):
        self.acc=acc
        self.name=name
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

#************no need to print details,you can if needed***********##
    def printBank(self):
        print("account=",self.acc)
        print("name=",self.name)
        print("bank name=",Bank.bank_name)
        # print("availible balance=",self.balance)
#**********************************************************#

obj=Bank()
obj.createBank(1001,"maria")
obj.deposit(1000)
obj.withdraw(2000)
obj.balEnq()
obj.printBank()

