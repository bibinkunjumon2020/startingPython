
#-------- abstract class & abstraction

from abc import ABC,abstractmethod
import Program34_Encapsulation as pg34

class Car(ABC):
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def filter(self):
        pass

class Honda(Car):
    def engine(self):
        print("I am a honda engine")
    def filter(self):
        print("I am filter")
obj=Honda()
obj.engine()
obj.filter()
#print(pg34.Employee().name)
#print(pg34.Employee()._salary)
print(pg34.obj3.name)
print(pg34.obj3._salary)