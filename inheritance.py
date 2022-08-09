class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
            #use the python class to create an object, and then execute the programm
x=person("cse","pfsd")
x.printname()