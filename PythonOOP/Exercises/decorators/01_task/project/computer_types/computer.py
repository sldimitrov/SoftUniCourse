from abc import ABC, abstractmethod


class Computer(ABC):
    VALID_TYPES = ["Laptop", "Desktop Computer"]

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str or None = None
        self.ram: int = 0
        self.price: int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        if not manufacturer.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = manufacturer

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        if not model.strip():
            raise ValueError("Model name cannot be empty.")

        self.__model = model

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    def __repr__(self):
        return f"{self.__manufacturer} {self.__model} with {self.processor} and {self.ram}GB RAM"



