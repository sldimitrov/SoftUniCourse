from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):

    def __init__(self, name: str, weight: float, food_eaten: int = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @property
    @abstractmethod
    def food_to_consume(self):
        pass

    @property
    @abstractmethod
    def weight_increase(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        if type(food) not in self.food_to_consume:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        gained_weight = self.weight_increase * food.quantity
        self.food_eaten += food.quantity
        self.weight += gained_weight


class Bird(Animal, ABC):

    def __init__(self, name: str, weight: float, wing_size, food_eaten: int = 0):
        super().__init__(name, weight, food_eaten)
        self.wing_size: float = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, food_eaten)
        self.living_region: str = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.name}, {self.living_region}, {self.food_eaten}]"




