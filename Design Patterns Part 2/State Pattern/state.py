class State:
    def __init__(self, name):
        # TODO: Initialize the state with the name parameter
        # TODO: Use proper encapsulation by making name a private attribute with '_' prefix
        self._name = name
    
    @property
    def name(self):
        # TODO: Implement the getter property for the name attribute
        # TODO: Return the private name attribute
        return self._name
    
    def display_info(self):
        # TODO: Implement the display_info method
        # TODO: Print the state name in the format: "State: {name}"
        print(f"State: {self.name}")
