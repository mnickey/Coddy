class CoffeeShop:
    """
    A class that manages coffee orders and inventory.
    """
    def __init__(self):
        # TODO: Initialize an empty list to store orders
        # TODO: This list will hold beverage objects (both plain and decorated)
        pass
    
    def add_order(self, beverage):
        # TODO: Add the beverage to the orders list
        # TODO: Return the total number of orders after adding this one
        # TODO: Use len() to get the count after appending
        pass
    
    def get_total_cost(self):
        # TODO: Calculate and return the total cost of all orders
        # TODO: Use sum() with a generator expression
        # TODO: Call the cost() method on each beverage in self.orders
        pass
    
    def print_orders(self):
        # TODO: Create a formatted string showing all orders
        # TODO: Initialize an empty result list
        # TODO: Loop through orders with enumerate() starting at 1
        # TODO: For each order, format as "Order #X: description - $cost"
        # TODO: Use beverage.get_description() and beverage.cost() 
        # TODO: Format cost to 2 decimal places using :.2f
        # TODO: Join all order strings with newlines and return
        pass
    
    def clear_orders(self):
        # TODO: Remove all orders from the orders list
        # TODO: Reset self.orders to an empty list
        pass
    
    def get_order_count(self):
        # TODO: Return the number of orders currently in the shop
        # TODO: Use len() on the orders list
        pass
