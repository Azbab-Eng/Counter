
class Student():
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade


    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_student):
        self.name = name
        self.max_student = max_student
        self.students = []
        self.is_func = True


    def add_student(self,student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        print( "The class is already full")    

    def get_student(self):
        name = [student.name  for student in self.students ]
        age = [student.age for student in self.students ]
        grade = [student.grade for student in self.students ]
        # print(f"{name } {age} {grade}")
        for i in range(self.max_student):
            print(f"Name:{name[i]} , Age:{age[i]} , Grade:{grade[i]}")
        # return f"Student {self.students.} : age {self.age} : grade {self.grade}"

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()

        return total /  len(self.students) #self.max_student



# course = Course()
# student = Student()
s1 = Student("Az",20,89)
s2 = Student("Af",21,99)
s3 = Student("Us",19,79)

c1 = Course("Science",2)


c1.add_student(s1)
c1.add_student(s2)
c1.get_student()
print(c1.get_average_grade())













