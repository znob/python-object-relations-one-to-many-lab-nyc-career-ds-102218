# import car class here
from car import Car

class Owner:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def name():
        doc = "The name property."
        def fget(self):
            return self._name
        def fset(self, value):
            self._name = value
        def fdel(self):
            del self._name
        return locals()
    name = property(**name())

    def age():
        doc = "The age property."
        def fget(self):
            return self._age
        def fset(self, value):
            self._age = value
        def fdel(self):
            del self._age
        return locals()
    age = property(**age())

    def find_my_cars(self):
        my_cars = [car for car in Car.all() if car.owner == self]
        return [f"{car.make} {car.model}" for car in my_cars]
