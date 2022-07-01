class Employee:
    def __init__(self):
        self.name="name"   #Public
        self._salary=3000 # Protected
        self.__age=25 # Private
    def printVal(self):
        print(self.name)
        print(self._salary)
        print(self.__age)
class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)
        #super(Manager, self).__init__(name,age,salary)
        #super().__init__(name,age,salary)


class Restaurent():
    def __init__(self):
        pass
    obj=Employee()
    #print(obj._salary)
    def printVal2(self):
        print(Employee().name,Employee()._salary)

#obj=Employee("Bibin",23,75000)
#obj2=Manager("Bibin",23,75000)
#obj3=Restaurent()
#obj3.printVal2()
#print(Employee().name)
#print(Employee()._salary)

obj=Restaurent()
#obj.printVal2()

obj3=Employee()
#print(obj.name)
#obj.printVal()
#obj2.myPrint()
#print(obj2.name)
#print(obj2._salary)
#print(obj._salary)

#print(obj._Employee__age)