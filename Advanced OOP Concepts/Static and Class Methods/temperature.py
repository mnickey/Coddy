class Temperature:
    # TODO: Create a class variable 'celsius_readings' as an empty list
    celsius_readings = []
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        # TODO: Implement the static method that converts Celsius to Fahrenheit
        # TODO: Use the formula: F = C * 9/5 + 32
        fahrenheit = celsius * 9 / 5 + 32
        return fahrenheit
    
    @classmethod
    def add_reading(cls, celsius):
        # TODO: Implement the class method to add a Celsius temperature to the celsius_readings list
        # TODO: Use cls.celsius_readings.append() to add the reading
        cls.celsius_readings.append(celsius)
    
    @classmethod
    def average_reading(cls):
        # TODO: Implement the class method to calculate the average of all readings
        # TODO: Check if celsius_readings is empty, return 0 if it is
        # TODO: Calculate the average by dividing the sum of readings by the number of readings
        if len(cls.celsius_readings) > 0:
            return (sum(cls.celsius_readings) / len(cls.celsius_readings))
        else: 
            return 0
