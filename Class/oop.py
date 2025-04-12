
print(" ********CLASS OBJECT ORIENTATION PROGRAMMING********   ")

class School:

    def __init__(self,name,age,gender,date):
        self.name = name
        self.age = age
        self.gender = gender
        self.date = date

    def employ(self):
        print("I want to employ Teachers")


    def resign(self,name):
        self.name = name
        print(f"I remove {self.name} from my staff")


s = School("ABD",23,"male","23/03/2000")
s.employ()
s.resign("ABC")