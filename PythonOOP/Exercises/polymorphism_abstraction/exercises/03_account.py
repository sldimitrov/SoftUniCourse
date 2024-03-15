
class Account:

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self.self_transactions: list = []


    def handle_transaction(self, transaction_amount: int):
        if transaction_amount >= self.amount:
            raise ValueError("sorry cannot go in debt!")

        self.amount = transaction_amount
        # TODO: add transaction
        return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            return f"please use int for amount"

        # TODO: check the balance
        ...

    def balance(self):
        ...


