
# Aggreation

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

    
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author


l1 = Library("Maktabal AAm")

b1 = Book("Nahwu","Usaimin")
b2 = Book("Tafseer","Inb Katheer")
b3 = Book("Hadith","Askholaani")

l1.add_book(b1)
l1.add_book(b2)
l1.add_book(b3)

print(l1.name)
print()
l1.all_books()

        