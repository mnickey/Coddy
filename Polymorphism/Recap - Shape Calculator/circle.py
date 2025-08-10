# TODO: Import the Shape class from shape.py
from shape import Shape

# TODO: Import the math module for pi
import math

class Circle(Shape):
    def __init__(self, radius):
        # TODO: Initialize the Circle with the given radius
        # Store the radius as an instance attribute
        self.radius = radius
    
    def area(self):
        # TODO: Implement the area method for a circle
        # Formula: π * radius²
        # Use math.pi for the value of π
        return math.pi * (self.radius ** 2)
    
    def perimeter(self):
        # TODO: Implement the perimeter method for a circle
        # Formula: 2 * π * radius
        # Use math.pi for the value of π
        return 2 * math.pi * self.radius
    
    def __str__(self):
        # TODO: Override the __str__ method to return a description
        # The description should be exactly: "Circle with radius [radius]"
        return f"Circle with radius {self.radius}"
