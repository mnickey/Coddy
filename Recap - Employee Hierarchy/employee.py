# TODO: Import the Person class from person.py
# Use format: from person import Person
from person import Person

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        # TODO: Call the parent class constructor with name and age using super()
        # TODO: Store employee_id and salary as instance attributes
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary
    
    def introduce(self):
        # TODO: Override the introduce method to include employee information
        # TODO: Call the parent's introduce method using super() and add employee ID info
        # TODO: Format: parent's introduction + " I work with employee ID [employee_id]."
        parent_intro = super().introduce()
        return f"{parent_intro} I work with employee ID {self.employee_id}."

        # Simpler version of what I wrote
        # return super().introduce() + f" I work with employee ID {self.employee_id}."
    
    def calculate_paycheck(self):
        # TODO: Calculate and return the monthly salary (salary ÷ 12)
        return (self.salary / 12)
