from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_COMPUTER_TYPES = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop,
    }

    def __init__(self):
        self.warehouse: [Computer, DesktopComputer, Laptop] = []
        self.profits: int = 0

    def build_computer(self, type_computer: VALID_COMPUTER_TYPES, manufacturer: str, model: str, processor: str,
                       ram: int):
        if type_computer not in self.VALID_COMPUTER_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        # Find the computer's type
        computer_type = self.VALID_COMPUTER_TYPES[type_computer]

        # Initialise the computer
        computer = computer_type(manufacturer, model)

        # Configure the computer and save information
        information = computer.configure_computer(processor, ram)

        # Add the computer to the warehouse
        self.warehouse.append(computer)

        # Return configuration info
        return information

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            # Client requirements
            if computer.price > client_budget and computer.processor != wanted_processor and computer.ram < wanted_ram:
                continue  # if not suitable

            # Calculate profit from the sell
            profit = client_budget - computer.price

            # Add profit to the whole
            self.profits += profit

            # Return information
            return f"{computer} sold for {client_budget}$."
        





