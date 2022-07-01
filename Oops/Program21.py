class Person:
    def setValue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printVal(self):
        print(self.name,self.age,self.place)
class Student(Person):
    def setValue2(self,roll,dep,college):
        self.roll=roll
        self.dep=dep
        self.college=college
        print(self.roll,self.dep,self.college)
ob=Student()
ob.setValue2(12,"cs","CEA")
