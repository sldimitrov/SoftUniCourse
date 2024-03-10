from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    def __init__(self, name: str):
        super().__init__(name, 3.50, 50)
