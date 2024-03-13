from project.customer import Customer
from project.dvd import DVD
from typing import List


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.dvds: List[DVD] = []
        self.customers: List[Customer] = []

    @classmethod
    def dvd_capacity(cls):
        """ This class method returns the capacity of the DVDs - constant value """
        return cls.DVD_CAPACITY

    @classmethod
    def customer_capacity(cls):
        """ This class method returns the capacity of the Customer's - constant value """
        return cls.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        """ This method add a customer to the list of customers if not exceeding the capacity """
        if len(self.customers) < self.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        """ This method add a DVD to the list of DVDs if not exceeding the capacity """
        if len(self.dvds) < self.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        """ This method rent a DVD  """
        # Find the objects of the dvd and the customer within the collections
        dvd = next(filter(lambda x: x.id == dvd_id, self.dvds))
        customer = next(filter(lambda x: x.id == customer_id, self.customers))

        if dvd in customer.rented_dvds:  # Customer has the DVD
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:  # DVD is rented
            return f"DVD is already rented"
        elif customer.age < dvd.age_restriction:  # Customer is age restricted
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:  # We actually rent the DVD
            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        """ This method checks if the DVD is in the Customer list and removes it if so """
        customer = next(filter(lambda x: x.id == customer_id, self.customers))
        dvd = next(filter(lambda y: y.id == dvd_id, self.dvds))

        if dvd in customer.rented_dvds:
            customer.rented_dvds.pop(dvd)
            self.dvds.append(dvd)
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):

        result = []

        customer_info = (c.__repr__() for c in self.customers)
        dvds_info = (d.__repr__() for d in self.dvds)

        result.append('\n'.join(customer_info))
        result.append('\n'.join(dvds_info))

        return "\n".join(result)


