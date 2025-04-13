
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and {self.age}years")

    def speak(self):
        print(f"I dont know language i say")

class Cat(Pet):

    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def show(self):
        print(f"i am {self.name} and {self.age} and also {self.color} in color")


    def speak(self):
        print(f"Meow")


class Dog(Pet):
    def speak(self):
        print(f"Bark")


class Fish(Pet):
    pass




p = Pet("Bill",23)
p.show()
p.speak()
c = Cat("Jill",20,"Brown")
c.show()
c.speak()
f = Fish("Fishy",15)
f.speak()
f.show()