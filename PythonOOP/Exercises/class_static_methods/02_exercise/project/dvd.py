
class DVD:

    def __init__(self, name: str, _id: int, creation_year: int, creation_month: str, age_restriction: int):
        # Constructor - attach attributes to the instance
        self.name = name
        self.id = _id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, _id: int, name: str, date: str, age_restriction: int):
        # Extract the month and the year of creation
        day, month, year = date.split('.')

        # Initialise a new instance of the class
        return cls(name, _id, year, month, age_restriction)

    def __repr__(self):
        # Override the repr method in order to improve the presentation of the printed instances
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction"
                f" {self.age_restriction}. Status: {self.is_rented}")

