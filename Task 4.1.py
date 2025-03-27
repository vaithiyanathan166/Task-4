#create a python class called circle with constructor which will take a list as an argument for the task.
#The List is [10,501,22,37,100,999,87,351]

import math

class Circle:
    def __init__(self, radii_list):
        """Initialize the Circle class with a list of radii."""
        self.radii = radii_list

    def calculate_areas(self):
        """Returns a dictionary with radius as key and corresponding area as value."""
        return {r: round(math.pi * r ** 2, 2) for r in self.radii}

    def calculate_circumferences(self):
        """Returns a dictionary with radius as key and corresponding circumference as value."""
        return {r: round(2 * math.pi * r, 2) for r in self.radii}

# Given list
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Create Circle instance
circle = Circle(radii_list)

# Calculate and display areas
areas = circle.calculate_areas()
print("Areas:", areas)

# Calculate and display circumferences
circumferences = circle.calculate_circumferences()
print("Circumferences:", circumferences)
