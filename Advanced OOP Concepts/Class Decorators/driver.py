from calculator import Calculator

# Comprehensive test case handler
test_case = input()

if test_case == "basic_functionality":
    calc = Calculator()
    print(calc.add(5, 3))  # Should print 8
    print(calc.add(2, 7))  # Should print 9
    print(calc.subtract(10, 4))  # Should print 6
    print(calc.call_counts)  # Should print {'add': 2, 'subtract': 1}

elif test_case == "multiple_instances":
    calc1 = Calculator()
    calc2 = Calculator()
    
    print(calc1.add(5, 3))  # Should print 8
    print(calc2.add(2, 7))  # Should print 9
    print(calc1.subtract(10, 4))  # Should print 6
    
    # Both instances should share the same call_counts
    print(calc1.call_counts)  # Should print {'add': 2, 'subtract': 1}
    print(calc2.call_counts)  # Should print {'add': 2, 'subtract': 1}
    print(calc1.call_counts is calc2.call_counts)  # Should print True

elif test_case == "method_call_order":
    calc = Calculator()
    
    print(calc.add(1, 2))  # Should print 3
    print(calc.subtract(5, 2))  # Should print 3
    print(calc.add(10, 20))  # Should print 30
    print(calc.add(7, 3))  # Should print 10
    print(calc.call_counts)  # Should print {'add': 3, 'subtract': 1}

elif test_case == "large_values":
    calc = Calculator()
    
    print(calc.add(1000000, 2000000))  # Should print 3000000
    print(calc.subtract(5000000, 2000000))  # Should print 3000000
    print(calc.call_counts)  # Should print {'add': 1, 'subtract': 1}

elif test_case == "negative_values":
    calc = Calculator()
    
    print(calc.add(-5, -3))  # Should print -8
    print(calc.subtract(-10, -4))  # Should print -6
    print(calc.call_counts)  # Should print {'add': 1, 'subtract': 1}

elif test_case == "float_values":
    calc = Calculator()
    
    print(calc.add(5.5, 3.2))  # Should print 8.7
    print(calc.subtract(10.5, 4.2))  # Should print 6.3
    print(calc.call_counts)  # Should print {'add': 1, 'subtract': 1}

elif test_case == "zero_values":
    calc = Calculator()
    
    print(calc.add(0, 0))  # Should print 0
    print(calc.subtract(0, 0))  # Should print 0
    print(calc.call_counts)  # Should print {'add': 1, 'subtract': 1}

elif test_case == "counter_reset":
    calc = Calculator()
    
    print(calc.add(5, 3))  # Should print 8
    print(calc.call_counts)  # Should print {'add': 1, 'subtract': 0}
    
    # Reset the counter
    calc.call_counts = {"add": 0, "subtract": 0}
    
    print(calc.add(2, 7))  # Should print 9
    print(calc.call_counts)  # Should print {'add': 1, 'subtract': 0}

elif test_case == "counter_manipulation":
    calc = Calculator()
    
    print(calc.add(5, 3))  # Should print 8
    print(calc.call_counts)  # Should print {'add': 1, 'subtract': 0}
    
    # Manipulate the counter directly
    calc.call_counts["add"] = 100
    
    print(calc.add(2, 7))  # Should print 9
    print(calc.call_counts)  # Should print {'add': 101, 'subtract': 0}

elif test_case == "performance_test":
    calc = Calculator()
    
    # Perform 1000 add operations
    for i in range(1000):
        calc.add(i, i+1)
    
    # Perform 500 subtract operations
    for i in range(500):
        calc.subtract(i+10, i)
    
    print(calc.call_counts)  # Should print {'add': 1000, 'subtract': 500}
