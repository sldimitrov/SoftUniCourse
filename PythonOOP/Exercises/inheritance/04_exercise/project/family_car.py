from project.car import Car


class FamilyCar(Car):

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)

    def drive(self, kilometers):
        fuel_required = self.fuel_consumption * kilometers
        if self.fuel >= fuel_required:
            self.fuel -= fuel_required

