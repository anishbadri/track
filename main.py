class book:
    def __init__(self, isbn, nameOfBook, authorObj):
        self.isbn = isbn
        self.nameOfBook = nameOfBook
        self.authorname = author(authorObj.name, 15)

    def printBook(self):
        print(self.nameOfBook, self.authorname.name)


class author:
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
    
    def printAuthor(self):
        print(self.name, self.age)


author1 = author("anish", 25)

book1 = book(123,"Bio of Anish", author1)
# author1.printAuthor()
book1.printBook()






