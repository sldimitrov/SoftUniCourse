from typing import List

from project.dvd import DVD

class Customer:

    def __init__(self, name: str, age: int, _id: int):
        self.name = name
        self.age = age
        self.id = _id
        self.rented_dvds: List[DVD] = []

    def __repr__(self):
        return (f"{id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's"
                f" ({', '.join(dvd.name for dvd in self.rented_dvds)})")