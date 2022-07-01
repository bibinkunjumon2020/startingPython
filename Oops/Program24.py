class Student:
    def __init__(self,name,age,branch,place):
        self.name=name
        self.age=age
        self.branch=branch
        self.place=place
    def printVal(self):
        print(self.name,self.age,self.branch,self.place)
f=open("student")
for element in f:
    data=element.rstrip("\n").split()
    ob=Student(data[0],data[1],data[2],data[3])
    ob.printVal()
f.close()