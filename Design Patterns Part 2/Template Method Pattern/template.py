class Template:
    def __init__(self, name):
        # TODO: Initialize the Template class with a name parameter
        # TODO: Store the name as a private attribute with underscore prefix (_name)
        self._name = name
    
    @property
    def name(self):
        # TODO: Implement a property getter that returns the private _name attribute
        # This provides read-only access to the name attribute
        return self._name
    
    def display_info(self):
        # TODO: Implement a method that prints the template information
        # Format should be exactly: "Template: {self._name}"
        print(f"Template: {self._name}")
