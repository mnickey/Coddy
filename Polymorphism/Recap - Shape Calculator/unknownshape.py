class UnknownShape:
    def __init__(self, name, size):
        # TODO: Initialize the UnknownShape with the given name and size
        # Store name and size as instance attributes
        self.name = name
        self.size = size
    
    def area(self):
        # TODO: Implement the area method for an unknown shape
        # Formula: size²
        return self.size ** 2
    
    def perimeter(self):
        # TODO: Implement the perimeter method for an unknown shape
        # Formula: 4 * size
        return self.size * 4
    
    def describe(self):
        # TODO: Implement the describe method for an unknown shape
        # The description should be exactly: "This is a [name] shape with area [area] and perimeter [perimeter]"
        # Use self.area() and self.perimeter() to get the values
        return f"This is a {self.name} shape with area {self.area()} and perimeter {self.perimeter()}"
    
    def __str__(self):
        # TODO: Override the __str__ method to return a description
        # The description should be exactly: "[name] with size [size]"
        return f"{self.name} with size {self.size}"
