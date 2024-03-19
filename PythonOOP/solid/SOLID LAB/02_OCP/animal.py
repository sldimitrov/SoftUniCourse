from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "woof woof"


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "meow"


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


"""
2nd principle of Solid : OPEN CLOSE 
--- classes, funcs. should be opened for extension but closed for modification
"""


animal_list = [Cat('cat'), Dog('dog')]
animal_sound(animal_list)

