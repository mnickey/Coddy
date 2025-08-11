from bank_account import BankAccount

# Comprehensive test case handler
test_case = input()

if test_case == "basic_test":
    # Basic functionality test
    account = BankAccount("John Doe", "12345")
    print(account.account_holder)  # Public attribute
    print(account.deposit(100))    # Public method
    print(account.get_balance())   # Public method

elif test_case == "transaction_count":
    # Testing protected attribute
    account = BankAccount("Jane Smith", "67890")
    account.deposit(50)
    account.deposit(100)
    account.deposit(200)
    print(account._transaction_count)  # Protected attribute
    print(account.get_balance())

elif test_case == "invalid_deposit":
    # Testing validation in deposit method
    account = BankAccount("Bob Johnson", "54321")
    print(account.deposit(-50))  # Should return None
    print(account.deposit(0))    # Should return None
    print(account.deposit(75))   # Should return 75
    print(account.get_balance())

elif test_case == "private_access":
    # Testing private attribute access
    account = BankAccount("Alice Brown", "98765")
    try:
        print(account.__balance)  # This will raise an AttributeError
    except AttributeError:
        pass
    
    try:
        print(account.__account_number)  # This will raise an AttributeError
    except AttributeError:
        pass
    
    print("Private attributes are not directly accessible")
    account.deposit(500)
    print(account.get_balance())  # Access through public method

elif test_case == "name_mangling":
    # Demonstrating name mangling for private attributes
    account = BankAccount("Charlie Green", "13579")
    print(account._BankAccount__balance)        # Accessing private attribute through name mangling
    print(account._BankAccount__account_number)  # Accessing private attribute through name mangling
    account.deposit(300)
    print(account._BankAccount__balance)  # Should show updated balance

elif test_case == "multiple_accounts":
    # Testing multiple accounts
    account1 = BankAccount("David White", "24680")
    account2 = BankAccount("Eva Black", "86420")
    account3 = BankAccount("Frank Red", "97531")
    
    account1.deposit(150)
    account2.deposit(250)
    account2.deposit(50)
    account3.deposit(500)
    account3.deposit(300)
    account3.deposit(200)
    
    print(f"{account1.account_holder}: {account1.get_balance()}")
    print(f"{account2.account_holder}: {account2.get_balance()}")
    print(f"{account3.account_holder}: {account3.get_balance()}")
    
    print(f"Account 1 transactions: {account1._transaction_count}")
    print(f"Account 2 transactions: {account2._transaction_count}")
    print(f"Account 3 transactions: {account3._transaction_count}")

elif test_case == "stress_test":
    # Performance test with many transactions
    account = BankAccount("Stress Tester", "11111")
    for _ in range(1000):
        account.deposit(1)
    print(f"Final balance: {account.get_balance()}")
    print(f"Transaction count: {account._transaction_count}")
