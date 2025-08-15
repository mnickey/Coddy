def add_counter(cls):
    # TODO: Initialize the call_counts dictionary with keys "add" and "subtract" both starting at 0
    cls.call_counts = {"add": 0, "subtract": 0}
    
    # TODO: Store original methods
    # Store the original add method from the class
    original_add = cls.add  # Replace with actual code
    
    # Store the original subtract method from the class
    original_subtract = cls.subtract  # Replace with actual code
    
    # TODO: Define wrapped methods that increment counters and preserve original functionality
    def wrapped_add(self, a, b):
        # TODO: Increment the "add" counter in call_counts
        # HINT: Use self.__class__.call_counts to access the class attribute
        self.__class__.call_counts["add"] += 1
        # TODO: Call the original add method and return its result
        return original_add(self, a, b)
    
    def wrapped_subtract(self, a, b):
        # TODO: Increment the "subtract" counter in call_counts
        # HINT: Use self.__class__.call_counts to access the class attribute
        self.__class__.call_counts["subtract"] += 1
        # TODO: Call the original subtract method and return its result
        return original_subtract(self, a, b)
    
    # TODO: Replace original methods with wrapped versions
    # Replace the add method with wrapped_add
    cls.add = wrapped_add
    # Replace the subtract method with wrapped_subtract
    cls.subtract = wrapped_subtract
    # TODO: Return the modified class
    return cls
