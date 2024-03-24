from computer_types.computer import Computer
from computer_types.desktop_computer import DesktopComputer
from computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTER_TYPES = ["Desktop Computer", "Laptop"]

    def __init__(self):
        self.warehouse: [Computer, DesktopComputer, Laptop] = []
        self.profits: int = 0

    def build_computer(self, type_computer: VALID_COMPUTER_TYPES, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTER_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        # Initialise the computer
        computer = type_computer(manufacturer, model)

        # Configure the computer
        return computer.configure_computer(processor, ram)





