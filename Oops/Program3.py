class Employee:

    """
    Emp_Name=""
    Emp_ID=0
    Emp_Desig=""            I can even initiate varible like this... but unnecessary code length
    Emp_Salary=""
    Emp_Company=""

    """
    def setValue(self,name,id,designation,salary,company):
        self.Emp_Name=name
        self.Emp_ID=id
        self.Emp_Desig=designation
        self.Emp_Salary=salary
        self.Emp_Company=company
    def printValue(self):
        print(self.Emp_Name+" "+str(self.Emp_ID)+" "+self.Emp_Desig+" "+str(self.Emp_Salary)+" "+self.Emp_Company)

E1=Employee()    # Object creation of class
E2=Employee()
E3=Employee()


E1.setValue("Bibin",123,"Manager",23456,"Tata")
E1.printValue()

E2.setValue("Alfi",999,"Servant",12000,"BPL")
E2.printValue()

E3.setValue("Suban",504,"Cook",50000,"LG")
E3.printValue()