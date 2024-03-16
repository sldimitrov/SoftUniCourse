from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    @property
    def food_to_consume(self):
        return [Vegetable, Fruit]

    @property
    def weight_increase(self):
        return 0.1

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):

    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    @property
    def food_to_consume(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 0.4

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):

    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    @property
    def food_to_consume(self):
        return [Vegetable, Meat]

    @property
    def weight_increase(self):
        return 0.3

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):

    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten)

    @property
    def food_to_consume(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 1

    def make_sound(self):
        return "ROAR!!!"

