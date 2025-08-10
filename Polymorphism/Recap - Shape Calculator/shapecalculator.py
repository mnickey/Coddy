class ShapeCalculator:
    def process_shape(self, shape):
        # TODO: Implement the process_shape method that processes any shape
        # Step 1: Print "Processing: [shape]" using the shape's string representation
        # Step 2: Print the result of calling the shape's describe() method
        # Step 3: Return a dictionary with keys "area" and "perimeter" and their calculated values
        print(f"Processing: {shape}")
        print(shape.describe())
        result = {
            'area': shape.area(), 
            'perimeter': shape.perimeter()
            }
        return result
        
