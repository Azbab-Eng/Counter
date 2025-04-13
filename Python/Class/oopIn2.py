class Staff():
    def __init__(self,name,salary):
        self.name = name
        # self.position = position
        self.salary = salary

    def show(self):
        print(f"{self.name},i entitle to #{self.salary}")



class Teacher(Staff):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

    def show(self):
        print(f"{self.name}, I am taking {self.
        department} class department,i entitle to  #{
        self.salary}")

    def get_dept(self):
        return self.department

class Manager(Staff):
    def __init__(self, name, salary,position):
        super().__init__(name, salary)
        self.position = position

    def show(self):
        print(f"{self.name}, I am the {self.
        position},i entitle to #{self.salary}")

    def assign_dept(self,dept):
        self.dept = dept
        print(f"{teacher1.department} {self.dept}")
        # print(f"{teacher1.get_dept() = }")
        # teacher1.get_dept() == self.dept


cleaner1 = Staff("Momo",30000)
cleaner1.show()
manager1 = Manager("Mr. Alaka",120000,"Principal")
manager1.show()
teacher1 = Teacher("Miss Basheeroh",100000,"Art")
teacher1.show()
manager1.assign_dept("Science")
# print(teacher1.get_dept())
# teacher1.show()

