class Parent:
    def __init__ (self,txt):
        self.message=txt
    def printmessage(self):
        print(self.message)
class child(Parent):
    def __init__(self,txt):
       super().__init__(txt)


x=child("hello, and welcome!")
x.printmessage()