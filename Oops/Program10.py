class Person:
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
        print("Inside A")

class Student(Person):
    def setValue1(self,roll,dept):
        self.roll=roll
        self.dept=dept
        print(self.name,self.age,self.place,self.roll,self.dept)


S1=Student("Bibin",34,"Ottumala")

S1.setValue1(99,"Computer Science")

