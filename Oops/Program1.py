class Person: # Class is defined
    def setValue(self,name,age,place):  #method inside class   self stored address where object is being created
        self.newName=name  #instance variable
        self.newAge=age
        self.newPlace=place
    def printValue(self):
        print(self.newAge)
        print(self.newName)
        print(self.newPlace)
        print(self)
    def trialValue(different,go): # i used different variable for self
        print(go)
        print(different)

p1=Person()
p1.setValue("bibin",23,"hi")
p1.printValue()
p1.trialValue(45)
