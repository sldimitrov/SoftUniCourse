from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, refuel: int):
        pass


class Car(Vehicle):
    INCREASING = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: int):
        fuel_needed = distance * (self.fuel_consumption + self.INCREASING)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, refuel: int):
        self.fuel_quantity += refuel


class Truck(Vehicle):
    INCREASING = 1.6
    TANK_FUELING = 0.95

    def drive(self, distance: int):
        fuel_needed = distance * (self.fuel_consumption + self.INCREASING)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, refuel: int):
        self.fuel_quantity += (refuel * self.TANK_FUELING)



