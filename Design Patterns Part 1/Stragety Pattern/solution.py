from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        
    def pay(self, amount):
        print(f"Paying ${amount} using Credit Card: {self.card_number}")
        return True

class PayPalPayment(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        
    def pay(self, amount):
        print(f"Paying ${amount} using PayPal account: {self.email}")
        return True

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
    
    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy
    
    def checkout(self):
        total = sum(item["price"] for item in self.items)
        if self.payment_strategy:
            return self.payment_strategy.pay(total)
        else:
            raise ValueError("No payment strategy set")

# Create your BitcoinPayment strategy class here
class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Paying ${amount} using Bitcoin wallet: {self.wallet_address}")
        return True   

# Create a main function to demonstrate the strategy pattern
def main():
    cart = ShoppingCart() # Creates the shopping cart

    cart.set_payment_strategy(BitcoinPayment) # Sets the payment strategy to Bitcoin 
    cart.add_item("laptop", 1200) # Adds item and price to cart
    cart.add_item("headphones", 100) # Adds item and price to cart

    bitcoin_strategy = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa") # assignes the BC wallet address to a variable
    cart.set_payment_strategy(bitcoin_strategy) # Sets the CARTS payment strategy
    cart.checkout() # Calls the checkout method

if __name__ == "__main__":
    main()
