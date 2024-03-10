from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str):
        super().__init__(name)
        self.__caffeine: float = 0

    @property
    def caffeine(self):
        return self.__caffeine

