class Money:
    def __init__(self, amount, currency):
        # TODO: Initialize the Money object with amount and currency parameters
        # TODO: Store amount as a float and currency as a string as instance attributes
        self.amount = float(amount)
        self.currency = str(currency)
    
    def __add__(self, other):
        # TODO: Implement addition of two Money objects
        # TODO: Check if currencies match - if not, raise ValueError with message "Cannot add different currencies"
        # TODO: If currencies match, return a new Money object with the sum of amounts and the same currency
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        new_amount = self.amount + other.amount
        return Money(new_amount, self.currency)
    
    def __mul__(self, scalar):
        # TODO: Implement multiplication of a Money object by a scalar (number)
        # TODO: Return a new Money object with the amount multiplied by the scalar and the same currency
        new_amount = self.amount * scalar
        return Money(new_amount, self.currency)
    
    def __eq__(self, other):
        # TODO: Implement equality comparison between Money objects
        # TODO: Two Money objects are equal if they have the same amount and currency
        # TODO: Return True if equal, False otherwise
        if self.amount == other.amount and self.currency == other.currency:
            return True
        else:
            return False
    
    def __str__(self):
        # TODO: Implement string representation of Money object
        # TODO: Return a string in the format "X.XX CUR" where X.XX is the amount with 2 decimal places
        # TODO: Example: "10.00 USD" for Money(10.0, "USD")
        return f"{self.amount:.2f} {self.currency}"
