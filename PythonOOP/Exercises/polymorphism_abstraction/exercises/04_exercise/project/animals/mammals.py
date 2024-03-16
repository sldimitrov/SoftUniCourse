from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    @property
    def food_to_consume(self):
        return [Vegetable, Fruit]

    @property
    def weight_increase(self) -> float:
        return 0.10

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):

    @property
    def food_to_consume(self):
        return [Meat]

    @property
    def weight_increase(self) -> float:
        return 0.4

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):

    @property
    def food_to_consume(self):
        return [Vegetable, Meat]

    @property
    def weight_increase(self) -> float:
        return 0.30

    def make_sound(self) -> str:
        return "Meow"


class Tiger(Mammal):

    @property
    def food_to_consume(self):
        return [Meat]

    @property
    def weight_increase(self) -> float:
        return 1

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"
