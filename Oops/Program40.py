
# Example of encapsulation
class Person:
    def __init__(self):
        self.name="arun"   #Public
        self._salary=3000 # Protected
        self.__age=25 # Private
    def printVal(self):
        print(" Im in class Person")
        print(self.name)
        print(self._salary)
        print(self.__age)
class Employee(Person):
    def __init__(self):
        Person.__init__(self)
        #super().__init__()
    def printVal2(self):
        print(" Im in class Employee")
        print(self.name)
        print(self._salary)
        #print(self.__age)  It is hidden to get o/p




obj=Employee() # Object Created
obj.printVal() # Succesful O/P bcs printVal is Person function
obj.printVal2() # Error bcs printVal2 cannt access __age / name and salary printed then error
