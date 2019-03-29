class authorClass:
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
    
    def printAuthor(self):
        print(self.name, self.age)