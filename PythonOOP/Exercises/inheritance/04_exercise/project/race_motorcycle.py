from project.motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8
    fuel_consumption = DEFAULT_FUEL_CONSUMPTION

    def __init(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        fuel_required = self.fuel_consumption * kilometers
        if self.fuel >= fuel_required:
            self.fuel -= fuel_required
