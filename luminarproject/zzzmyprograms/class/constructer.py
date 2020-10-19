class Employee:
    company_name="Luminar Technolab"
    def __init__(self,id,name,salary,des):
        self.id=id
        self.name=name
        self.salary=salary
        self.des=des
    def printEmp(self):
        print("id=",self.id)
        print("name=",self.name)
        print("salary=",self.salary)
        print("des=",self.des)
        print("Bankname=",Employee.company_name)

emp=Employee(1001,"maria",5000,"developer")
# emp.setEmp(1001,"maria",5000,"developer")
emp.printEmp()
