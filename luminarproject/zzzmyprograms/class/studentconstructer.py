class Student:
    college_name="VJCET"
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total

    def printStudent(self):
        print("rollno=",self.rollno)
        print("name=",self.name)
        print("course=",self.course)
        print("total=",self.total)
        print("college=",Student.college_name)

stud=Student(1001,"maria","BCA",300)
stud.printStudent()