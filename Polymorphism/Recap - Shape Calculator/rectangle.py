# TODO: Import the Shape class from shape.py
from shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        # TODO: Initialize the Rectangle with the given width and height
        # Store width and height as instance attributes
        self.height = height
        self.width = width
    
    def area(self):
        # TODO: Implement the area method for a rectangle
        # Formula: width * height
        return self.height * self.width
    
    def perimeter(self):
        # TODO: Implement the perimeter method for a rectangle
        # Formula: 2 * (width + height)
        return 2 * (self.height + self.width)
    
    def __str__(self):
        # TODO: Override the __str__ method to return a description
        # The description should be exactly: "Rectangle with width [width] and height [height]"
        return f"Rectangle with width {self.width} and height {self.height}"
