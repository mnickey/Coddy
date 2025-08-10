from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from unknownshape import UnknownShape
from shapecalculator import ShapeCalculator
import math

# Test case handler
test_case = input()

def test_basic_functionality():
    calculator = ShapeCalculator()
    
    # Test with Circle
    circle = Circle(5)
    print(f"Testing {circle}")
    results = calculator.process_shape(circle)
    print(f"Results: {results}")
    print()
    
    # Test with Rectangle
    rectangle = Rectangle(4, 6)
    print(f"Testing {rectangle}")
    results = calculator.process_shape(rectangle)
    print(f"Results: {results}")
    print()
    
    # Test with Triangle
    triangle = Triangle(3, 4, 5)
    print(f"Testing {triangle}")
    results = calculator.process_shape(triangle)
    print(f"Results: {results}")
    print()
    
    # Test with UnknownShape (duck typing)
    unknown = UnknownShape("Custom", 10)
    print(f"Testing {unknown}")
    results = calculator.process_shape(unknown)
    print(f"Results: {results}")

def test_edge_cases():
    calculator = ShapeCalculator()
    
    # Test with zero values
    print("Testing zero values:")
    circle = Circle(0)
    print(f"Circle(0) area: {circle.area()}, perimeter: {circle.perimeter()}")
    
    rectangle = Rectangle(0, 5)
    print(f"Rectangle(0, 5) area: {rectangle.area()}, perimeter: {rectangle.perimeter()}")
    
    # Test with very large values
    print("\
Testing large values:")
    large_circle = Circle(1000000)
    print(f"Circle(1000000) area: {large_circle.area():.2e}, perimeter: {large_circle.perimeter():.2e}")
    
    # Test with decimal values
    print("\
Testing decimal values:")
    decimal_circle = Circle(0.5)
    print(f"Circle(0.5) area: {decimal_circle.area()}, perimeter: {decimal_circle.perimeter()}")
    
    decimal_triangle = Triangle(2.5, 3.5, 4.5)
    print(f"Triangle(2.5, 3.5, 4.5) area: {decimal_triangle.area()}, perimeter: {decimal_triangle.perimeter()}")

def test_inheritance():
    # Create instances of each shape
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)
    unknown = UnknownShape("Custom", 10)
    
    # Test inheritance relationships
    from shape import Shape
    print(f"Circle is a Shape: {isinstance(circle, Shape)}")
    print(f"Rectangle is a Shape: {isinstance(rectangle, Shape)}")
    print(f"Triangle is a Shape: {isinstance(triangle, Shape)}")
    print(f"UnknownShape is a Shape: {isinstance(unknown, Shape)}")
    
    # Test method availability
    print("\
Method availability:")
    for shape_name, shape_obj in [("Circle", circle), ("Rectangle", rectangle), 
                                ("Triangle", triangle), ("UnknownShape", unknown)]:
        print(f"{shape_name} has area(): {hasattr(shape_obj, 'area')}")
        print(f"{shape_name} has perimeter(): {hasattr(shape_obj, 'perimeter')}")
        print(f"{shape_name} has describe(): {hasattr(shape_obj, 'describe')}")

def test_polymorphism():
    calculator = ShapeCalculator()
    
    # Create a list of different shapes
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5),
        UnknownShape("Custom", 10)
    ]
    
    print("Testing polymorphic behavior:")
    for i, shape in enumerate(shapes, 1):
        print(f"\
Shape {i}: {shape.__class__.__name__}")
        results = calculator.process_shape(shape)
        print(f"Results: {results}")

def test_duck_typing():
    calculator = ShapeCalculator()
    
    # Create a completely new class that has the required methods
    class CustomDuckShape:
        def __init__(self, name, factor):
            self.name = name
            self.factor = factor
        
        def area(self):
            return self.factor * 3
        
        def perimeter(self):
            return self.factor * 12
        
        def describe(self):
            return f"This is a {self.name} duck-typed shape with area {self.area()} and perimeter {self.perimeter()}"
        
        def __str__(self):
            return f"Custom {self.name} with factor {self.factor}"
    
    # Test with the custom duck-typed shape
    duck_shape = CustomDuckShape("DuckTyped", 5)
    print(f"Testing duck typing with: {duck_shape}")
    results = calculator.process_shape(duck_shape)
    print(f"Results: {results}")
    
    # Compare with a regular shape
    circle = Circle(5)
    print(f"\
Comparing with regular shape: {circle}")
    results = calculator.process_shape(circle)
    print(f"Results: {results}")

def test_invalid_inputs():
    calculator = ShapeCalculator()
    
    try:
        # Test with negative radius
        print("Testing Circle with negative radius:")
        negative_circle = Circle(-5)
        results = calculator.process_shape(negative_circle)
        print(f"Results: {results}")
    except Exception as e:
        print(f"Error with negative circle: {e}")
    
    try:
        # Test with invalid triangle (sides that can't form a triangle)
        print("\
Testing invalid Triangle (1, 1, 10):")
        invalid_triangle = Triangle(1, 1, 10)  # Violates triangle inequality
        results = calculator.process_shape(invalid_triangle)
        print(f"Results: {results}")
        # Check if area calculation gives a valid result
        area = invalid_triangle.area()
        if math.isnan(area) or not isinstance(area, float) or area <= 0:
            print(f"Invalid triangle area: {area}")
    except Exception as e:
        print(f"Error with invalid triangle: {e}")

# Run the appropriate test based on input
if test_case == "basic_functionality":
    test_basic_functionality()
elif test_case == "edge_cases":
    test_edge_cases()
elif test_case == "inheritance":
    test_inheritance()
elif test_case == "polymorphism":
    test_polymorphism()
elif test_case == "duck_typing":
    test_duck_typing()
elif test_case == "invalid_inputs":
    test_invalid_inputs()
else:
    # Default test case
    test_basic_functionality()
