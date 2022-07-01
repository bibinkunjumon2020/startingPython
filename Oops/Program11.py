class Person:
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
        print("Inside A")
class Student(Person):

    def __init__(self,roll,dept):

        self.roll=roll
        self.dept=dept
    def printValue(self):
        print(self.name,self.age,self.place,self.roll,self.dept)

s2=Student(23,"ert")  # This is correct
#S1=Student(Person("Bibin",34,"Ottumala"))       """  Cannot do this because object of Person not created---only its parameters inherited by the Student class"""



