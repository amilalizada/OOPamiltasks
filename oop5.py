class Author():
    def __init__(self,name,email,gender):
        self.name = name
        self.email=email
        self.gender=gender
    def getName(self):
        return f'name :{self.name}'
    def getEmail(self):
        return f'email :{self.email}'
    def setEmail(self):
        return f'update email: {self.email}'
    def getGender(self):
        return self.gender
    def toString(self):
        return f'Author[name={self.name},email={self.email},gender={self.gender}]'

author =Author('Tan Ah Teck','ahTeck@somewhere.com','m')
print(author.toString())

class Book(Author):
    def __init__(self,name,author,price,qty):
        self.name=name
        self.author=author
        self.price=price
        self.qty=qty

    def getName(self):
        return self.name
    def getAuthor(self):
        return self.author
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getQty(self):
        return self.qty
    def setQty(self,qty):
        self.qty=qty
    def toString(self):
        return f"Book[name={self.name},Author[name={author.name},email={author.email},gender={author.gender},price={self.price},qty={self.qty}]"
book = Book('tan',author,3,4,)
print(book.toString())
