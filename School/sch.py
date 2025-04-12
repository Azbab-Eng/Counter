
class Account:
    total_amount = 0





class Stuent:
    total_student = 0
    def __init__(self,name,age,classBe,gender,fee):
        self.age = age
        self.name = name
        self.classBe = classBe
        self.gender = gender
        self.fee = fee
        self.dept = ""
        self.students = []

        Stuent.total_student += 1


class Course:
    def __init__(self,name,max_student):
        self.name = name
        self.no = max_student
        self.students = []
        self.subject = []

    def add_student(self,student):
        if len(self.students) < self.no:
            self.students.append(student)
            print("Successful Added")
        else: print("The Course is already full")
            


class EmployeeDetails:
    total_staff = 0
    def __init__(self,name,Emdate,gender,salary,role):
        self.name = name
        self.Emdate = Emdate
        self.gender = gender
        self.salary = salary
        self.role = role
        self.staff = []

        EmployeeDetails.total_staff += 1


class Staff(EmployeeDetails):
    def __init__(self, name, Emdate, gender, salary, role,position):
        super().__init__(name, Emdate, gender, salary, role)
        self.position = position

class Teacher(Staff):
    def __init__(self, name, Emdate, gender, salary, role, position):
        super().__init__(name, Emdate, gender, salary, role, position)
        self.classBe = ""

class Management(Staff): 
    def add_student(self,name,age,classBe,gender,fee):
        Stuent(name,age,classBe,gender,fee)
        print("Student is admitted to the school")


    def add_student_to_course(self,student,course):
        if len(course.students) < course.no:
            course.students.append(student)
            print("Successful Added")
        else: print("The Course is already full")


    def add_course(self,name,max_student):
        Course(name,max_student)
        print("Successfully added")


        


