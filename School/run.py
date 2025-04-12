from sch import *


#Student
student1 = Stuent("Babalola",20,"JSS","male",23000)
student2 = Stuent("AAzeez",23,"SSS","male",30000)
student3 = Stuent("Azbab",25,"Basic","female",15000)
# print(Stuent.total_student)


#Course
course1 = Course("Science",3)
course2 = Course("Art",2)
# course2.add_student(student1)
# course2.add_student(student2)
# course2.add_student(student3)
# print(len(course2.students))

#Cleaner
cleaner1 = EmployeeDetails("Sekeenah","23/03/2023","female",35000,"Cook")
cleaner1 = EmployeeDetails("Tunde","20/01/2024","male",30000,"Cleaner")

#Staff
teacer = Teacher("Azeezah","23/03/2023","female",55000,"staff","teacher")
teacer = Teacher("Azeez","24/03/2024","male",57000,"staff","teacher")

#Manager
manager1 = Management("Roqeeb","28/03/2020","male",70000,"staff","principal")
manager2 = Management("Roqeebah","20/03/2021","female",68000,"staff","Head")
# print(EmployeeDetails.total_staff)
student4 = manager1.add_student("Baba",22,"JSS1","male",22000)
manager1.add_student_to_course(student1,course1)
print(Stuent.total_student)
print(len(course2.students))
print(len(course1.students))
