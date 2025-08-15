# TODO: Import the add_counter decorator from decorator.py
# Use format: from decorator import add_counter
from decorator import add_counter

# TODO: Apply the add_counter decorator to the Calculator class
# Use the @add_counter syntax above the class definition
@add_counter
class Calculator:
    def __init__(self):
        pass
        
    def add(self, a, b):
        # TODO: Implement the add method that returns the sum of a and b
        return a + b
        
    def subtract(self, a, b):
        # TODO: Implement the subtract method that returns the difference of a and b
        return a - b
