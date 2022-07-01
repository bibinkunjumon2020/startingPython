# If the child has no init fn then the object of child created pass the argmnts to parent class without any super() call.
#But if child also has init then condition differs

class Vehicle:
    def __init__(self,name,mil,cap):
        self.name=name
        self.mil=mil
        self.cap=cap
    def fare(self):
        return self.cap*100
class Bus(Vehicle):
    def printVal(self):
        print("I am here")
school_bus=Bus("Honda",24,50)
print(school_bus.fare())

class Vehicle1:
    def __init__(self,name,mil,cap):
        self.name1=name
        self.mil1=mil
        self.cap1=cap
    def fare(self):
        return self.cap1*100
class Bus1(Vehicle1):
    def __init__(self, name, mil, cap):
        self.name = name
        self.mil = mil
        self.cap = cap
        super().__init__(name,mil,cap) # This line is must otherwise it wont work

school_bus=Bus1("Honda",24,50)
print(school_bus.fare())

class Vehicle2:
    def __init__(self,name,mil,cap):
        self.name1=name
        self.mil1=mil
        self.cap1=cap
    def fare(self):
        return self.cap1*100
class Bus2(Vehicle2):
   pass        # This also works

school_bus=Bus2("Honda",24,50)
print(school_bus.fare())

