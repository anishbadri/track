class book:
    def __init__(self, isbn, nameOfBook, authorObj):
        self.isbn = isbn
        self.nameOfBook = nameOfBook
        self.authorList = authorObj
        # self.authorList.extend(authorObj)

    def printBook(self):
        print(self.nameOfBook, self.authorList.name)