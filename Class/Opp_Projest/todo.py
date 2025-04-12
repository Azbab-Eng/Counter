class Day:
    def __init__(self,day):
        self.day = day
        self.todo = []

    def list_todo(self):
        list = [f"{lst.title} : {lst.describe}" for lst in self.todo]
        # print([i for i in list] )
        
        for i in list:
            print(i)

    def add_todo(self,todo):
        self.todo.append(todo)
        print("Successful Added")


class Todo:
    def __init__(self,title,describe):
        self.title = title
        self.describe = describe

        print(title + " : " + describe)


td1 = Todo("Bank Management System","I want to write a program for create Bank Management system OOP")
td = Todo("TodoList","I want to write todo list for OOP")

d1 = Day("Sunday")
d1.add_todo(td)
d1.add_todo(td1)
d1.list_todo()