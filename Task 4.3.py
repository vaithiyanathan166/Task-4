#From the given List create two class Methods Area and perimeter which will be going to calculate the area and perimeter.

class Circle:
    # Private class variable for π (pi)
    __pi = 3.141

    def __init__(self, radii_list):
        """Initialize the Circle class with a list of radii."""
        self.radii = radii_list  # Store the list of radii

    @classmethod
    def area(cls, radius):
        """Class method to calculate the area of a circle for a given radius."""
        return round(cls.__pi * radius ** 2, 2)

    @classmethod
    def perimeter(cls, radius):
        """Class method to calculate the perimeter (circumference) of a circle for a given radius."""
        return round(2 * cls.__pi * radius, 2)

    def calculate_all_areas(self):
        """Returns a dictionary with radius as key and corresponding area as value."""
        return {r: self.area(r) for r in self.radii}

    def calculate_all_perimeters(self):
        """Returns a dictionary with radius as key and corresponding perimeter as value."""
        return {r: self.perimeter(r) for r in self.radii}

# Given list of radii
radii_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Create Circle instance
circle = Circle(radii_list)

# Calculate and display areas using the class method
areas = circle.calculate_all_areas()
print("Areas:", areas)

# Calculate and display perimeters using the class method
perimeters = circle.calculate_all_perimeters()
print("Perimeters:", perimeters)

# Example: Directly calling the class methods
print("\nExample of Direct Class Method Calls:")
print(f"Area of a circle with radius 50: {Circle.area(50)}")
print(f"Perimeter of a circle with radius 50: {Circle.perimeter(50)}")
