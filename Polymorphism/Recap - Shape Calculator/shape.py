from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        # TODO: Define an abstract method for calculating area
        # This method will be implemented by child classes
        pass
    
    @abstractmethod
    def perimeter(self):
        # TODO: Define an abstract method for calculating perimeter
        # This method will be implemented by child classes
        pass
    
    def describe(self):
        # TODO: Implement a concrete method that returns a description
        # The description should be exactly: "This is a shape with area [area] and perimeter [perimeter]"
        # Use self.area() and self.perimeter() to get the values
        return f"This is a shape with area {self.area()} and perimeter {self.perimeter()}"
