from project.dough import Dough
from project.topping import Topping


class Pizza:

    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name: str = name
        self.dough: Dough = dough
        self.max_number_of_toppings: int = max_number_of_toppings
        self.toppings: dict[str: float] = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == '':
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value: Dough):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value: int):
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) >= self.__max_number_of_toppings:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type not in self.toppings:
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        toppings_weight = sum([w for w in self.toppings.values()])
        total_weight = self.__dough.weight + toppings_weight
        return total_weight






