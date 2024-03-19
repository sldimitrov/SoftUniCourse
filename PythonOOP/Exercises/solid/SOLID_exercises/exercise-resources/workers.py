from abc import ABC, abstractmethod
from typing import List


class BaseWorker(ABC):
    @staticmethod
    @abstractmethod
    def work():
        ...


class Worker(BaseWorker):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(BaseWorker):
    @staticmethod
    def work():
        print("I work very hard!!!")


class UltraWorker(BaseWorker):
    @staticmethod
    def work():
        print(f"I work extremely hard!!!")


class Manager:

    def __init__(self):
        self.workers: List[BaseWorker] = []

    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), f'`worker` must be of type {worker}'

        self.workers.append(worker)

    def manage(self):
        if self.workers is not None:
            [worker.work() for worker in self.workers]


# Initialise instances
normal_worker = Worker()
super_worker = SuperWorker()
ultra_worker = UltraWorker()
my_manager = Manager()

# Set the workers
my_manager.set_worker(normal_worker)
my_manager.set_worker(super_worker)
my_manager.set_worker(ultra_worker)

# Manage them
my_manager.manage()

# Manager set the worker and manage him
# my_manager.set_worker(normal_worker)
# my_manager.set_worker(super_worker)
# my_manager.manage()
#
#
# try:
#     my_manager.set_worker(super_worker)
#     my_manager.manage()
# except AssertionError:
#     print("manager fails to support super_worker....")
