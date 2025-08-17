# TODO: Import the Shape class from shape.py
# Use format: from shape import Shape
from shape import Shape
from math import sqrt

class Triangle(Shape):
    # TODO: Implement the Triangle class that inherits from Shape
    
    def __init__(self, a, b, c):
        # TODO: Initialize the Triangle with three sides a, b, and c
        # TODO: Store a, b, and c as instance attributes
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # TODO: Override the area method to calculate the triangle's area
        # TODO: Use Heron's formula: sqrt(s * (s-a) * (s-b) * (s-c))
        # TODO: where s = (a + b + c) / 2 (semi-perimeter)
        semi_perimeter = (self.a + self.b + self.c) / 2
        return sqrt(semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b) * (semi_perimeter- self.c))
    
    def perimeter(self):
        # TODO: Override the perimeter method to calculate the triangle's perimeter
        # TODO: Use the formula: a + b + c (sum of all sides)
        return (self.a + self.b + self.c)
