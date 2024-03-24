from project.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS_AVAILABLE = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200,
    }
    RAM_AVAILABLE = {2 ** i: (i) * 100 for i in range(7)}

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
        self.processor: str or None = None
        self.ram: int = 0
        self.price: int = 0

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS_AVAILABLE:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram not in self.RAM_AVAILABLE:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        # Attach pieces to the laptop
        self.processor = processor
        self.ram = ram

        # Add their prices to the computer's price
        self.price += (self.PROCESSORS_AVAILABLE[processor] + self.RAM_AVAILABLE[ram])

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."
