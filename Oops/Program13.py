class Person:



    def getValue(hai,name,age):
        hai.name=name
        hai.age=age
class Parent:
    def getValueP(self,place,phone):
        self.place=place
        self.phone=phone
class Employee(Person,Parent):
    def getValueE(self,id,design,salary):
        self.id=id
        self.design=design
        self.salary=salary
    def printValue(vazha):
        print(vazha.name,vazha.age,vazha.place,vazha.phone,vazha.id,vazha.design,vazha.salary)

e1=Employee()
e1.getValue("bibin",32)
e1.getValueP("Ottumala",7867889)
e1.getValueE(123,"Manager",500000)
e1.printValue()