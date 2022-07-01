class Child:
    def setValue(self,name,age):
        self.name=name
        self.age=age
class Person(Child):
    def setValue2(self,color):
        self.color=color
class Student(Person):
    def printValue(self):
        print(self.name,self.age,self.color)

st1=Student()
st1.printValue()