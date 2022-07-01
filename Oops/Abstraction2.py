"""
There is a lot to say here, but I’ll try to condense this to its essence.
An abstract base class is a class from which we want to create subclasses, but the base class is not something we can instantiate (create).
One canonical example is a vehicle.
A vehicle is an abstraction, whereas cars and motorcycles are specific examples of vehicles.
We would never want to create a “vehicle” in our code, but we certainly might want to create cars, motorcycles, bicycles, trucks, and other kinds of vehicles.

"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """This class inherits from (or subclasses) ABC"""
    @abstractmethod
    def number_of_wheels(self):
        #This method is abstract, so the class cannot be
        #instantiated. This method will be overridden in
        #subclasses of Vehicle.
       pass

class Car(Vehicle):
    """This class inherits from the abstract base class Vehicle"""
    def number_of_wheels(self):
        """Override the abstract method in the base class"""
        return 4

# create a car called c: SUCCEEDS
c = Car()
# print the number of wheels that c has: SUCCEEDS
print(c.number_of_wheels())

# Try to create a Vehicle: FAILS

"""

v = Vehicle()

TypeError: Can't instantiate abstract class Vehicle with abstract methods number_of_wheels 
"""