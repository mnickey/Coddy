from timer import Timer
import time

# Test case handler
test_case = input()

if test_case == "basic_test":
    # Basic functionality test
    with Timer():
        # Simulate some work
        time.sleep(2)  # This makes the program wait for 2 seconds

elif test_case == "nested_contexts":
    # Test nested context managers
    with Timer():
        time.sleep(1)
        with Timer():
            time.sleep(1)

elif test_case == "exception_handling":
    # Test exception handling within context
    try:
        with Timer():
            time.sleep(1)
            raise ValueError("Test exception")
    except ValueError as e:
        print(f"Caught exception: {e}")

elif test_case == "zero_sleep":
    # Test with minimal sleep
    with Timer():
        time.sleep(0.001)

elif test_case == "multiple_timers":
    # Test multiple timers in sequence
    with Timer():
        time.sleep(1)
    
    with Timer():
        time.sleep(0.5)
    
    with Timer():
        time.sleep(2)

elif test_case == "as_decorator":
    # Test timer in a function context
    def timed_function():
        with Timer():
            time.sleep(2)
    
    timed_function()

else:
    # Default test - basic functionality
    with Timer():
        # Simulate some work
        time.sleep(2)  # This makes the program wait for 2 seconds
