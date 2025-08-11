class Rectangle:
    def __init__(self, width, height):
        # TODO: Initialize private attributes _width and _height with default values
        # NOTE: Set initial values to 0 before using the property setters
        self._width = 0
        self._height = 0
        
        # TODO: Use property setters to set width and height (for validation)
        # This ensures validation happens during initialization
        self.width = width
        self.height = height
    
    # TODO: Implement width property getter
    @property
    def width(self):
        # TODO: Return the private _width attribute
        pass
    
    # TODO: Implement width property setter
    @width.setter
    def width(self, value):
        # TODO: Validate that value is positive (greater than 0)
        # TODO: If value is not positive, raise ValueError with message "Width must be positive"
        # TODO: If value is valid, set the _width attribute
        pass
    
    # TODO: Implement height property getter
    @property
    def height(self):
        # TODO: Return the private _height attribute
        pass
    
    # TODO: Implement height property setter
    @height.setter
    def height(self, value):
        # TODO: Validate that value is positive (greater than 0)
        # TODO: If value is not positive, raise ValueError with message "Height must be positive"
        # TODO: If value is valid, set the _height attribute
        pass
    
    # TODO: Implement read-only area property
    @property
    def area(self):
        # TODO: Calculate and return the area (width * height)
        pass
    
    # TODO: Implement read-only perimeter property
    @property
    def perimeter(self):
        # TODO: Calculate and return the perimeter (2 * (width + height))
        pass
    
    # TODO: Implement dimensions property getter
    @property
    def dimensions(self):
        # TODO: Return width and height as a tuple (width, height)
        pass
    
    # TODO: Implement dimensions property setter
    @dimensions.setter
    def dimensions(self, dimensions):
        # TODO: Unpack the tuple into width and height
        # TODO: Use the width and height setters to update values (for validation)
        pass
    
    # TODO: Implement dimensions property deleter
    @dimensions.deleter
    def dimensions(self):
        # TODO: Reset both width and height to 1
        # TODO: Use the property setters to ensure validation
        pass
