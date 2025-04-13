
class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def all_books(self):
        books = [f"{book.title} by {book.author}" 
                 for book in self.books]
        for list in books:
            print(list)
        # return books

    def remove_book(self,book):
        self.books.remove(book)
        print(f"'{book.title} by {book.author}' is deleted from the list of the Books")
        self.all_books()

    def update_library(self,NewName = ""):
        self.name = NewName
    
    
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def update_book(self,NewTitle = "",NewAuthor = ""):
        self.title = NewTitle
        self.author = NewAuthor

        # all_books()


l1 = Library("Maktabal AAm")

b1 = Book("Nahwu","Usaimin")
b2 = Book("Tafseer","Inb Katheer")
b3 = Book("Hadith","Askholaani")

l1.add_book(b1)
l1.add_book(b2)
l1.add_book(b3)
l1.all_books()
# l1.remove_book(b3)
b3.update_book("Balaaqoh","Mudeer")
l1.all_books()