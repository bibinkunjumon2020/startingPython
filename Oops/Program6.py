
#static variable defined here

class Luminar:
    # static variable defined here
    institute="CUSAT"
    fee=30000
    def setValue(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def printValue(self):
        print(self.name,self.rollno,self.age,self.institute,Luminar.fee)
student1=Luminar()
student1.setValue("bibin",23,34)
student1.printValue()

print(Luminar.institute)  # static variable can be accessed outside by using class name

