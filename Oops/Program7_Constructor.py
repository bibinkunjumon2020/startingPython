
# instance variable defined inside a object  variable

# pass __init inside object


class Person:
        def __init__(self,name,age):  # Constructor used to initilize object on creation
            self.name=name
            self.age=age
        def printValue(self):
            print(self.name,self.age)
p1=Person("Bibin",23)
p1.printValue()