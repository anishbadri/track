import author 

class book:
    def __init__(self, isbn, nameOfBook, authorObj):
        self.isbn = isbn
        self.nameOfBook = nameOfBook
        self.authorList = authorObj
        # self.authorList.extend(authorObj)

    def printBook(self):
        print(self.nameOfBook, self.authorList.name)





author1 = author.authorClass("anish", 25)
book1 = book(123, "Named", author1)

# book1 = book(123,"Bio of Anish", author1)
author1.printAuthor()
book1.printBook()






