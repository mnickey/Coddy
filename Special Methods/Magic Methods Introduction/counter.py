class Counter:
    def __init__(self, initial_value=0):
        # TODO: Initialize the counter with the initial_value parameter
        # TODO: Store the initial_value as an instance attribute named 'count'
        self.count = initial_value
    
    def __str__(self):
        # TODO: Return a string representation of the counter
        # TODO: Format should be exactly "Count: {self.count}"
        return f"Count: {self.count}"
    
    def __add__(self, other):
        # TODO: Implement addition between a Counter and a number
        # TODO: Return a new Counter instance with count = self.count + other
        # TODO: This allows expressions like: counter + 5
        count = self.count + other
        return Counter(count)
