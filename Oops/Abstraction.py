"""In Python, an abstraction is used to hide the irrelevant data/class in order to reduce the complexity.
It also enhances the application efficiency.
In Python abstraction can be achieved by using abstract classes and interfaces.
A class that consists of one or more abstract method is called the abstract class.
Abstract methods do not contain their implementation.
Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass.
Abstraction classes are meant to be the blueprint of the other class.
An abstract class can be useful when we are designing large functions.
An abstract class is also helpful to provide the standard interface for different implementations of components.
Python provides the abc module to use the abstraction in the Python program.
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def features(self):
        pass

    def justforFun(self):
        print("hi")

class Car(Vehicle):
    def engine(self):
        self.capacity=1000
        self.rpm=7000
        print(self.capacity,self.rpm)
    def features(self):
        self.color="grey"
        self.tyre=4
        print(self.color,self.tyre)
class Bike(Vehicle):
    def engine(self):
        self.capacity=300
        self.rpm=1000
        print(self.capacity, self.rpm)
    def features(self):
        self.color="white"
        self.tyre=2
        print(self.color,self.tyre)
c=Car()
c.engine()
c.features()

b=Bike()
b.engine()
b.features()


