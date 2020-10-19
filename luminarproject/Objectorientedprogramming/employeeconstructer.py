class Employee:
    company_name="Luminar Technolab"
    def __init__(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary

    def printEmp(self):
        print("eid=",self.id)
        print("designation=", self.desig)
        print("salary=", self.salary)
        print("companyname=",Employee.company_name)

emp=Employee(1001,"develops",30000)
emp.printEmp()
