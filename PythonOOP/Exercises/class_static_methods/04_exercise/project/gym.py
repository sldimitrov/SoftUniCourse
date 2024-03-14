from typing import List

from project.trainer import Trainer
from project.customer import Customer
from project.equipment import Equipment
from project.subscription import Subscription
from project.exercise_plan import ExercisePlan


class Gym:

    def __init__(self):
        self.trainers: List[Trainer] = []
        self.customers: List[Customer] = []
        self.plans: List[ExercisePlan] = []
        self.equipment: List[Equipment] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = next(filter(lambda s: s.id == subscription_id, self.subscriptions))
        customer = next(filter(lambda c: c.id == subscription.customer_id, self.customers))
        trainer = next(filter(lambda t: t.id == subscription.trainer_id, self.trainers))
        plan = next(filter(lambda p: p.id == subscription.exercise_id, self.plans))
        equipment_id = plan.equipment_id

        equipment = next(filter(lambda e: e.id == equipment_id, self.equipment))

        result = [subscription, customer, trainer, equipment, plan]

        return "\n".join(str(x) for x in result)

