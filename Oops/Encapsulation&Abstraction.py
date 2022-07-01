


# Encapsulation - Bundling data and methods within a single unit.ex: Class
# A class is an example of encapsulation as it binds all the data members (instance variables) and methods into a single unit.

# Wrapping data and methods that work on data within ine unit

class Employee:
    def __init__(self,name,salary):
        self.name=name              # Data member
        self.salary=salary          #Data member

    def printDetail(self):
        print("Employee Name : ",self.name)    # Method

#Advantages
#1 by using Encapsulation we can hide the object's internal structure from outside.This is called information hiding
#2. Data protection - By controlling the accessibility of data members and methods from outside.

#Access Modifiers - Public,Private,Protected
#Access modifiers limit access to the variables and methods of a class.
#Default all data members and methods are public
#

class Employee1:
    def __init__(self):
        self.name="name"              # Public
        self._salary=35000         #Protected
        self.__dob="11-09-1995"           #Private

    def _printDetail(self): #protected methos
        print("Employee Name : ",self.name,self._salary)    # Method
        self.__showSecret() #Can access private fn from with in a public inside fn
        print(self.__dob)

    def __showSecret(self): #Private Method
        print("DOB : ",self.__dob)


employee1_obj=Employee1()
employee1_obj._printDetail()
print(employee1_obj.name)
print(employee1_obj._salary)
print(Employee1().name)         #Public
print(Employee1()._salary)   #Protected can be accessed
# print(Employee1().__dob)   Its an error bcs private variable not accessible outside
#employee1_obj.showSecret()
print(employee1_obj._Employee1__dob)  # I am accessing private data directly using (objname._Classname__Var)

print("*****")
employee1_obj._Employee1__showSecret()  # Name Mangling

employee1_obj._Employee1__dob="23-04-2091"   # I am changing value of a private variable by data mangling
employee1_obj._Employee1__showSecret()       #Printing by private method