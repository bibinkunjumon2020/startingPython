# Initialising class varibales using constructor with out creating object of parent class. super()


class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
        print(self.name,self.age,self.place)
class Student(Person):
    def __init__(self,roll,dep,college,name,age,place):
        self.roll=roll
        self.dep=dep
        self.college=college
        print(self.roll,self.dep,self.college)

        super().__init__(name,age,place)  # Calling the parent init with args.. dont forget () since super class & No (self required)



ob=Student(23,"Manager","CEA","Bibin",34,"Ottumala")


