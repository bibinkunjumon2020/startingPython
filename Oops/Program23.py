
# Using constructor in multi inheritance --- Parent class.init (self ,)... difference is there in single and multi inhertance

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print("Inside Person")
class Employee:
    def __init__(self,id,phone_no):
        self.id=id
        self.phn=phone_no
        print("Inside Employee")
class Student(Person,Employee):
    def __init__(self,roll,blood,classroom,name,age,place,id,phn):
        Person.__init__(self,name,age,place)  # No () only Class name and 'self' is must
        Employee.__init__(self,id,phn)
        self.roll=roll
        self.blood=blood
        self.cls=classroom
        print(self.roll,self.blood,self.cls)

ob=Student(23,"A","V","Bibin",34,"Kollm",89,9087)