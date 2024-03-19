from abc import ABC, abstractmethod
import time


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Worker, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")


class LazyPerson(Eatable):

    def eat(self):
        print(f"I am lazy person and eating is my favorite thing in the world")


class BaseManager(ABC):

    def __init__(self):
        self.workers: list = []

    @abstractmethod
    def set_worker(self, worker):
        ...


class WorkerManager(BaseManager):

    def set_worker(self, worker):
        assert isinstance(worker, Workable), f"`worker` must be of type {Workable}"

        self.workers.append(worker)

    def manage(self):
        [worker.work() for worker in self.workers]


class EatManager(BaseManager):

    def set_worker(self, worker):
        assert isinstance(worker, Eatable), f"`worker` must be of type {Eatable}"

        self.workers.append(worker)

    def lunch_break(self):
        [worker.eat() for worker in self.workers]


# Initialise the managers
work_manager = WorkerManager()
eat_manager = EatManager()

# Set each worker
work_manager.set_worker(Worker())
eat_manager.set_worker(Worker())

work_manager.set_worker(SuperWorker())
eat_manager.set_worker(SuperWorker())

work_manager.set_worker(Robot())
# The robot do NOT eat anything

# Manage all
work_manager.manage()
eat_manager.lunch_break()




