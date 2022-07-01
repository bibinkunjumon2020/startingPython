class Employee:

    def setValue(self):
        self.Emp_Name=input("Employee Name")
        self.Emp_ID=input("Employee ID")
        self.Emp_Desig=input("Employee Designation")  # Reading inputs from console
        self.Emp_Salary=input("Employee Salary")
        self.Emp_Company=input("Employee Company")

    def printValue(self):
        print(self.Emp_Name+" "+self.Emp_ID+" "+self.Emp_Desig+" "+self.Emp_Salary+" "+self.Emp_Company)

E1=Employee()    # Object creation of class
E2=Employee()
E3=Employee()


E1.setValue()
E1.printValue()

E2.setValue()
E2.printValue()

E3.setValue()
E3.printValue()