from unittest import TestCase, main
# from car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car( "BMW", "i3", 18, 200)

    def test_correct_init(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("i3", self.car.model)
        self.assertEqual(18, self.car.fuel_consumption)
        self.assertEqual(200, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_if_empty_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_if_empty_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_consumption_setter_if_zero_or_negative_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_if_zero_or_negative_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_if_zero_or_negative_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_or_negative_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_positive_value(self):
        self.car.fuel_capacity = 75
        self.car.refuel(80)
        self.assertEqual(75, self.car.fuel_amount)

    def test_drive_without_enough_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.car.fuel_amount = 200
        self.car.drive(1000)
        self.assertEqual(20, self.car.fuel_amount)


if __name__ == '__main__':
    main()