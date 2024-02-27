class Employee:
    def __init__(self, id: int, first_name: str, last_name: str, salary: int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"  # Return full name

    def get_annual_salary(self):
        annual_salary = self.salary * 12
        return annual_salary  # Return the annual salary number

    def raise_salary(self, amount: int):
        self.salary += amount  # Increase salary
