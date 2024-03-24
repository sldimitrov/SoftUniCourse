from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    PROCESSORS_AVAILABLE = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800
    }
    RAM_AVAILABLE = {2 ** i: (2 ** i) * 100 for i in range(8)}

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
        self.processor: str or None = None
        self.ram: int = 0
        self.price: int = 0

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS_AVAILABLE:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        if ram not in self.RAM_AVAILABLE:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        # Attach pieces to the laptop
        self.processor = processor
        self.ram = ram

        # Add their prices to the computer's price
        self.price += (self.PROCESSORS_AVAILABLE[processor] + self.RAM_AVAILABLE[ram])

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."


