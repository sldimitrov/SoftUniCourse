import calendar

class DVD:
    MONTHS = {
        1: "January", 2: "February", 3: "March",
        4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September",
        10: "October", 11: "November", 12: "December"
    }

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
        day, month, year = [int(x) for x in date.split('.')]
        month_str = calendar.month_name[month]

        # Initialise a new instance of the class
        return cls(name, _id, year, month_str, age_restriction)

    def __repr__(self):
        # Override the repr method in order to improve the presentation of the printed instances
        status = "rented" if self.is_rented else "not rented"  # Initialise the status of the DVD
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction"
                f" {self.age_restriction}. Status: {status}")

