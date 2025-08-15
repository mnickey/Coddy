from product import Product
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from printablemixin import PrintableMixin
from discountmixin import DiscountMixin
from shippablemixin import ShippableMixin

def test_basic_functionality():
    # Test basic functionality of all classes
    p = Product("Laptop", 1000)
    assert p.print_details() == "Product: Laptop, Price: $1000", f"Print details failed: {p.print_details()}"
    assert p.apply_discount(10) == 900, f"Discount calculation failed: {p.apply_discount(10)}"
    
    physical = PhysicalProduct("Desk", 500)
    physical.set_weight(30)
    assert physical.calculate_shipping() == 15, f"Shipping calculation failed: {physical.calculate_shipping()}"
    
    digital = DigitalProduct("Software", 200)
    assert digital.apply_discount(10) == 180, f"Digital discount failed: {digital.apply_discount(10)}"
    print("Basic functionality test passed!")

def test_edge_cases():
    # Test edge cases like zero and negative values
    p = Product("Free Item", 0)
    assert p.apply_discount(10) == 0, f"Zero price discount failed: {p.apply_discount(10)}"
    
    p_neg = Product("Negative Item", -100)
    assert p_neg.apply_discount(10) == -90, f"Negative price discount failed: {p_neg.apply_discount(10)}"
    
    physical = PhysicalProduct("Empty Box", 10)
    physical.set_weight(0)
    assert physical.calculate_shipping() == 0, f"Zero weight shipping failed: {physical.calculate_shipping()}"
    
    physical_neg = PhysicalProduct("Anti-Gravity Item", 10)
    physical_neg.set_weight(-5)
    assert physical_neg.calculate_shipping() == -2.5, f"Negative weight shipping failed: {physical_neg.calculate_shipping()}"
    print("Edge cases test passed!")

def test_large_values():
    # Test with very large values
    p = Product("Expensive Item", 1000000)
    assert p.apply_discount(10) == 900000, f"Large value discount failed: {p.apply_discount(10)}"
    
    physical = PhysicalProduct("Heavy Item", 500)
    physical.set_weight(1000)
    assert physical.calculate_shipping() == 500, f"Large weight shipping failed: {physical.calculate_shipping()}"
    print("Large values test passed!")

def test_inheritance():
    # Test inheritance relationships
    p = Product("Test", 100)
    physical = PhysicalProduct("Test", 100)
    digital = DigitalProduct("Test", 100)
    
    assert isinstance(p, PrintableMixin), "Product should inherit from PrintableMixin"
    assert isinstance(p, DiscountMixin), "Product should inherit from DiscountMixin"
    
    assert isinstance(physical, Product), "PhysicalProduct should inherit from Product"
    assert isinstance(physical, ShippableMixin), "PhysicalProduct should inherit from ShippableMixin"
    assert isinstance(physical, PrintableMixin), "PhysicalProduct should inherit from PrintableMixin through Product"
    assert isinstance(physical, DiscountMixin), "PhysicalProduct should inherit from DiscountMixin through Product"
    
    assert isinstance(digital, Product), "DigitalProduct should inherit from Product"
    assert isinstance(digital, PrintableMixin), "DigitalProduct should inherit from PrintableMixin through Product"
    assert isinstance(digital, DiscountMixin), "DigitalProduct should inherit from DiscountMixin through Product"
    print("Inheritance test passed!")

def test_method_overriding():
    # Test method overriding behavior
    p = Product("Regular Product", 100)
    digital = DigitalProduct("Digital Product", 100)
    
    # Same price, same discount percentage, different results
    assert p.apply_discount(20) == 80, f"Regular discount calculation failed: {p.apply_discount(20)}"
    assert digital.apply_discount(20) == 90, f"Digital fixed discount failed: {digital.apply_discount(20)}"
    
    # Digital product should always apply 10% discount regardless of parameter
    assert digital.apply_discount(0) == 90, "Digital product should apply 10% discount even with 0%"
    assert digital.apply_discount(50) == 90, "Digital product should apply 10% discount even with 50%"
    print("Method overriding test passed!")

def test_polymorphism():
    # Test polymorphic behavior with a list of different product types
    products = [
        Product("Regular", 100),
        PhysicalProduct("Physical", 100),
        DigitalProduct("Digital", 100)
    ]
    
    # Set weight for the physical product
    products[1].set_weight(10)
    
    # Expected results for apply_discount(20)
    expected_discounts = [80, 80, 90]
    
    for i, product in enumerate(products):
        # All should have print_details method
        assert "Product:" in product.print_details(), f"Polymorphic print_details failed for {type(product)}"
        
        # All should have apply_discount method but with different implementations
        assert product.apply_discount(20) == expected_discounts[i], f"Polymorphic apply_discount failed for {type(product)}"
    print("Polymorphism test passed!")

def test_attribute_access():
    # Test attribute access patterns
    p = Product("Test Product", 100)
    assert p.name == "Test Product", "Name attribute not properly set in Product"
    assert p.price == 100, "Price attribute not properly set in Product"
    
    physical = PhysicalProduct("Physical Product", 200)
    assert physical.name == "Physical Product", "Name attribute not properly set in PhysicalProduct"
    assert physical.price == 200, "Price attribute not properly set in PhysicalProduct"
    
    # Weight attribute should not exist before set_weight is called
    try:
        weight = physical.weight
        assert False, "Weight attribute should not exist before set_weight is called"
    except AttributeError:
        pass
    
    physical.set_weight(15)
    assert physical.weight == 15, "Weight attribute not properly set in PhysicalProduct"
    
    digital = DigitalProduct("Digital Product", 300)
    assert digital.name == "Digital Product", "Name attribute not properly set in DigitalProduct"
    assert digital.price == 300, "Price attribute not properly set in DigitalProduct"
    print("Attribute access test passed!")

# Main test runner
test_case = input()

if test_case == "basic_test":
    test_basic_functionality()
elif test_case == "edge_cases":
    test_edge_cases()
elif test_case == "large_values":
    test_large_values()
elif test_case == "inheritance":
    test_inheritance()
elif test_case == "method_overriding":
    test_method_overriding()
elif test_case == "polymorphism":
    test_polymorphism()
elif test_case == "attribute_access":
    test_attribute_access()
