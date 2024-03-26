from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_init(self):
        # Triple A principal:

        # Arrange
        name, salary, energy = "Pesho", "1000", 50

        # Act
        worker = Worker(name, salary, energy)

        # Assert
        self.assertEqual("Pesho", worker.name)
        self.assertEqual("1000", worker.salary)
        self.assertEqual(50, worker.energy)
        self.assertEqual(0, worker.money)

    def test_work_without_enough_energy(self):
        # Arrange
        name, salary, energy = "Samuil", "2000", -10

        # Act
        worker = Worker(name, salary, energy)

        # Assert
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_with_increase_money_and_decrease_energy(self):
        # Arrange
        name, salary, energy = "Petko", 5000, 100

        # Act
        worker = Worker(name, salary, energy)

        # Assert
        worker.work()
        worker.work()

        self.assertEqual(10000, worker.money)
        self.assertEqual(98, worker.energy)

    def test_rest_with_increasing_energy(self):
        # Arrange
        name, salary, energy = "Nam", 500, 45

        # Act
        worker = Worker(name, salary, energy)

        worker.rest()
        worker.rest()

        # Assert
        self.assertEqual(47, worker.energy)

    def test_get_info_representation(self):
        # Arrange
        name, salary, energy = "Nam", 500, 45

        # Act
        worker = Worker(name, salary, energy)

        expectations = f'{worker.name} has saved {worker.money} money.'
        result = worker.get_info()

        # Assert
        self.assertEqual(expectations, result)


if __name__ == '__main__':
    main()
