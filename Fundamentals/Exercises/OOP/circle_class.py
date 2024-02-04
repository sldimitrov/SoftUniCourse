# Create a Circle class
class Circle:
    __pi = 3.14

    # Define __init__ method
    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    # Define the following methods
    def calculate_circumference(self):
        circumference = 2 * Circle.__pi * self.radius
        return circumference

    def calculate_area(self):
        area = Circle.__pi * self.radius ** 2
        return area

    def calculate_area_of_sector(self, angle):
        sur_area = (Circle.__pi * self.radius ** 2) * (angle / 360)
        return sur_area


# Test Code
circle = Circle(10)
angle_circle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle_circle):.2f}")

