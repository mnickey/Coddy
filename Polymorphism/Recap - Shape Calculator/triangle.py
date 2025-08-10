# TODO: Import the Shape class from shape.py
from shape import Shape

# TODO: Import the math module for sqrt
import math

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        # TODO: Initialize the Triangle with the given sides
        # Store side1, side2, and side3 as instance attributes
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # TODO: Implement the area method for a triangle using Heron's formula
        # Step 1: Calculate the semi-perimeter s = (side1 + side2 + side3) / 2
        s = (self.side1 + self.side2 + self.side3) / 2
        # Step 2: Calculate area using: sqrt(s * (s - side1) * (s - side2) * (s - side3))
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        # Use math.sqrt for the square root
        return area
    
    def perimeter(self):
        # TODO: Implement the perimeter method for a triangle
        # Formula: side1 + side2 + side3
        return self.side1 + self.side2 + self.side3
    
    def __str__(self):
        # TODO: Override the __str__ method to return a description
        # The description should be exactly: "Triangle with sides [side1], [side2], and [side3]"
        return f"Triangle with sides {self.side1}, {self.side2}, and {self.side3}"
