from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        # Initialization attributes
        self.name: str = name
        self.__budget: int = budget
        self.__animal_capacity: int = animal_capacity
        self.__workers_capacity: int = workers_capacity
        # Instance attributes
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return f"Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker.name} fired successfully"
        except ValueError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salary = sum([s.salary for s in self.workers])
        if self.__budget >= workers_salary:
            self.__budget -= workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_care = sum([c.money_for_care for c in self.animals])
        if self.__budget >= animals_care:
            self.__budget -= animals_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):

        lions_amount = [lion for lion in self.animals if lion.__class__.__name__ == "Lion"]
        tigers_amount = [tiger for tiger in self.animals if tiger.__class__.__name__ == "Tiger"]
        cheetahs_amount = [cheetah for cheetah in self.animals if cheetah.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals\n"

        result += f"----- {len(lions_amount)} Lions:\n"
        for lion in lions_amount:
            result += f"{lion}\n"

        result += f"----- {len(tigers_amount)} Tigers:\n"
        for tiger in tigers_amount:
            result += f"{tiger}\n"

        result += f"----- {len(cheetahs_amount)} Cheetahs:\n"
        for cheetah in cheetahs_amount:
            result += f"{cheetah}\n"

        return result[:-1]

    def workers_status(self):
        keepers_amount = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers_amount = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets_amount = [v for v in self.workers if v.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers\n"

        result += f"----- {len(keepers_amount)} Keepers:\n"
        for keeper in keepers_amount:
            result += f"{keeper}\n"

        result += f"----- {len(caretakers_amount)} Caretakers:\n"
        for caretaker in caretakers_amount:
            result += f"{caretaker}\n"

        result += f"----- {len(vets_amount)} Vets:\n"
        for vet in vets_amount:
            result += f"{vet}\n"

        return result[:-1]

