#create proper member variables inside the task if required and use them when necessary.For example 
#for this task create a class private variable named pi = 3.141

class Circle:
    # Private class variable for π (pi)
    __pi = 3.141

    def __init__(self, radii_list):
        """Initialize the Circle class with a list of radii."""
        self.radii = radii_list  # Store the list of radii

    def calculate_areas(self):
        """Returns a dictionary with radius as key and corresponding area as value."""
        return {r: round(self.__pi * r ** 2, 2) for r in self.radii}

    def calculate_circumferences(self):
        """Returns a dictionary with radius as key and corresponding circumference as value."""
        return {r: round(2 * self.__pi * r, 2) for r in self.radii}

# Given list of radii
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Create Circle instance
circle = Circle(radii_list)

# Calculate and display areas
areas = circle.calculate_areas()
print("Areas:", areas)

# Calculate and display circumferences
circumferences = circle.calculate_circumferences()
print("Circumferences:", circumferences)
