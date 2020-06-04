import pytest
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
def test_author():
    exc="Author[name=Tan Ah Teck,email=ahTeck@somewhere.com,gender=m]"
    act=author.toString()
    assert exc==act
