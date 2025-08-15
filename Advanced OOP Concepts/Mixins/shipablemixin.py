class ShippableMixin:
    def set_weight(self, weight):
        # TODO: Implement the set_weight method that stores the weight as an attribute
        # TODO: Set self.weight = weight
        self.weight = weight
    
    def calculate_shipping(self):
        # TODO: Implement the calculate_shipping method that calculates shipping cost
        # TODO: Calculate shipping cost using the formula: weight * 0.5 ($0.50 per pound)
        # TODO: This method should access self.weight attribute set by set_weight method
        # TODO: Return the calculated shipping cost
        return self.weight * 0.50
