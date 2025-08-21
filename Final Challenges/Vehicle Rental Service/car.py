# TODO: Import the Vehicle class from vehicle.py
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, vin, make, model, daily_rate, passenger_capacity):
        # TODO: Call the parent class constructor with appropriate parameters
        # TODO: Store passenger_capacity as an instance attribute
        super().__init__(vin, make, model, daily_rate)
        self.passenger_capacity = passenger_capacity
    
    def __str__(self):
        # TODO: Call the parent class's __str__ method to get the base string representation
        # TODO: Return a formatted string that starts with "Car: " followed by the parent string
        #       and ends with " - Seats {passenger_capacity}"
        parent_str = super().__str__()
        return f"Car: {parent_str} - Seats {self.passenger_capacity}"
