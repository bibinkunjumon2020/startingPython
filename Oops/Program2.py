class Student:
    salary=0
    color=""
    def getValue(self,name,rollno,dept,colg_name):
        self.name=name
        self.rollno=rollno
        self.dept=dept
        self.clg_name=colg_name
    def printValue(self):
        print(self.name+" "+str(self.rollno)+" "+self.dept+" "+self.clg_name)
        print(self.salary)
    def getLook(self,salary1,color1):
        self.salary=salary1
        self.color=color1

Student1=Student()
Student2=Student()
Student3=Student()
Student1.getValue("Bibin 1",23,"EC","CEA")
Student2.getValue("Bibin 2",24,"CS","CEA")
Student3.getValue("Bibin 3",28,"Mech","CEA")
Student1.printValue()
Student2.printValue()
Student3.printValue()


Student1.getLook(123343,"Black")
Student1.printValue()