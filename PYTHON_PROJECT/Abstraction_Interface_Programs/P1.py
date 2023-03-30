# To achieve in python we need a library/module which is called as ABC(Abstract base class )
from abc import ABC, abstractmethod


class Car:

    def milage(self):
        pass


class Maruti(Car):

    def milage(self):
        print("25km/hr")


class Audi(Car):

    def milage(self):
        print("15km/hr")


c1 = Maruti()
c1.milage()
c2 = Audi()
c2.milage()
