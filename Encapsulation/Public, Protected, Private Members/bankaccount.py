class BankAccount:
    def __init__(self, account_holder, account_number):
        # TODO: Initialize the public attribute 'account_holder' with the provided parameter
        self.account_holder = account_holder
        # TODO: Initialize the protected attribute '_transaction_count' to 0
        self._transaction_count = 0
        # TODO: Initialize the private attribute '__balance' to 0
        # NOTE: Private attributes use double underscore prefix
        self.__balance = 0
        # TODO: Initialize the private attribute '__account_number' with the provided parameter
        self.__account_number = account_number
    
    # Public methods
    def deposit(self, amount):
        # TODO: Check if amount is greater than 0
        if amount > 0:
        # TODO: If valid, add amount to the private __balance attribute
            self.__balance += amount
        # TODO: Call the protected _update_transaction_count() method
            self._update_transaction_count()
        # TODO: Return the new balance
            return self.__balance
        # TODO: If amount is not valid, return None
        else:
            return None
    
    def get_balance(self):
        # TODO: Return the current value of the private __balance attribute
        return self.__balance
    
    # Protected method
    def _update_transaction_count(self):
        # TODO: Increment the protected _transaction_count attribute by 1
        self._transaction_count += 1
