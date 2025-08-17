# TODO: Import all shape classes
# Use format: 
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle

class ShapeFactory:
    # TODO: Implement the ShapeFactory class
    
    def create_shape(self, shape_type, *args):
        # TODO: Implement the create_shape method that creates and returns different shapes
        # TODO: The method should take shape_type as the first parameter and dimensions as additional arguments
        # TODO: Handle the following shape types (case-insensitive):
        #       - "circle": Create a Circle with radius (args[0])
        #       - "rectangle": Create a Rectangle with length (args[0]) and width (args[1])
        #       - "triangle": Create a Triangle with sides a (args[0]), b (args[1]), and c (args[2])
        # TODO: For invalid shape types, raise a ValueError with the message: "Invalid shape type: {shape_type}"
        shape_type_lowered = shape_type.lower()
        if shape_type_lowered == "circle":
            return Circle(args[0])
        elif shape_type_lowered == "rectangle":
            return Rectangle(args[0], args[1])
        elif shape_type_lowered == "triangle":
            return Triangle(args[0], args[1], args[2])
        else:
            raise ValueError(f"Invalid shape type: {shape_type}")
