
class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25
    fuel_consumption: float = DEFAULT_FUEL_CONSUMPTION

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        fuel_required = self.fuel_consumption * kilometers
        if self.fuel >= fuel_required:
            self.fuel -= fuel_required
