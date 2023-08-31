# ABC -> Abstract Base Classes
from abc import ABC, abstractmethod


class Computer(ABC):
    def printer(self):
        print("This is Computer class' Printer")

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("This is Laptop's implementation of ABC")


# c = Computer()
# c.printer()
l = Laptop()
l.process()
l.printer()