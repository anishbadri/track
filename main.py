# import Model.author as author
# import Model.book as book
from flask import Flask



app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()



# author1 = author.authorClass("anish", 25)
# book1 = book.book(123, "Named", author1)

# book1 = book(123,"Bio of Anish", author1)
# author1.printAuthor()
# book1.printBook()

# if __name__ == "__main__":
    # name,age = input("Enter Name and Age").split()
    # # print("Hello")
    # author1 = author.authorClass(name,age)
    # isbn,bookName = input("Enter Name and Age").split()
    # # print("Hello")
    # author1 = author.authorClass(name,age)
    # book1 = book.book(isbn,bookName,author1)
    # print(book1.authorList.name)

    # books = []
    # author = [] 

    # for k in range(3):


    # for i in range(3):

    #     newBook = book.book(i,"Bio" + str(i), "Anish")
    #     books.append(newBook)

    # for j in range(3):
    #     print(books[j].nameOfBook)







