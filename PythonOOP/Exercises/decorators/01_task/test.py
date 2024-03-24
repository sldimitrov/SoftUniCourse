from unittest import TestCase, main
from project.computer_store_app import ComputerStoreApp


class TestComputerStoreAppClass(TestCase):
    def test_practice(self):
        self.store = ComputerStoreApp()

        build_result = self.store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64)
        sell_result = self.store.sell_computer(10000, "Apple M1 Pro", 32)

        self.assertEqual(build_result, "Created Apple Macbook with Apple M1 Pro and 64GB RAM for 1800$.")
        self.assertEqual(sell_result, "Apple Macbook with Apple M1 Pro and 64GB RAM sold for 10000$.")


if __name__ == '__main__':
    main()