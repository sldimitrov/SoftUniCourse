from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3
    fuel_consumption = DEFAULT_FUEL_CONSUMPTION

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        fuel_required = kilometers * self.fuel_consumption

        if self.fuel >= fuel_required:
            self.fuel -= fuel_required

