"""Class Inheritance is a process of inheriting behaviour(functionality) or appearances (attributes)
from a class(Super Class)"""


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale", " exhale")

# TODO - 1 Class Fish inheriting from Super class
class Fish(Animal):
    def __init__(self):
        # TODO -2 initializing all attributes inherited from Super class
        super().__init__()

    def breathe(self):
        # TODO -3 calling Super class functionality inherited
        super().breathe()
        print("I have to breathe under water")

    def swim(self):
        print("Swimming under Ocean ooo oo !!!!")


nemo = Fish()
print(nemo.num_eyes)
nemo.breathe()
nemo.swim()

"""OUTPUT:
    2
inhale  exhale
I have to breathe under water
Swimming under Ocean ooo oo !!!!"""
