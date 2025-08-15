from temperature import Temperature

# Test case handler for comprehensive testing
test_case = input()

if test_case == "default_test":
    # Test basic functionality
    Temperature.celsius_readings = []
    Temperature.add_reading(25)
    Temperature.add_reading(30)
    Temperature.add_reading(27)
    
    print(f"Average reading: {Temperature.average_reading()}")
    print(f"22°C is {Temperature.celsius_to_fahrenheit(22)}°F")

elif test_case == "empty_readings":
    # Test average_reading with no readings
    Temperature.celsius_readings = []
    print(f"Average reading: {Temperature.average_reading()}")

elif test_case == "single_reading":
    # Test with a single reading
    Temperature.celsius_readings = []
    Temperature.add_reading(100)
    print(f"Average reading: {Temperature.average_reading()}")

elif test_case == "negative_values":
    # Test with negative temperature values
    Temperature.celsius_readings = []
    Temperature.add_reading(-10)
    Temperature.add_reading(-20)
    Temperature.add_reading(-30)
    print(f"Average reading: {Temperature.average_reading()}")
    print(f"-15°C is {Temperature.celsius_to_fahrenheit(-15)}°F")

elif test_case == "zero_value":
    # Test with a reading of 0°C
    print(f"0°C is {Temperature.celsius_to_fahrenheit(0)}°F")

elif test_case == "extreme_values":
    # Test with extreme temperature values
    absolute_zero = -273.15  # absolute zero in Celsius
    sun_surface = 5500  # approximate sun surface temperature in Celsius
    
    print(f"{absolute_zero}°C is {Temperature.celsius_to_fahrenheit(absolute_zero)}°F")
    print(f"{sun_surface}°C is {Temperature.celsius_to_fahrenheit(sun_surface)}°F")

elif test_case == "reset_readings":
    # Test resetting the readings
    Temperature.celsius_readings = []
    Temperature.add_reading(10)
    Temperature.add_reading(20)
    Temperature.add_reading(30)
    print(f"Average reading before reset: {Temperature.average_reading()}")
    
    Temperature.celsius_readings = []
    print(f"Average reading after reset: {Temperature.average_reading()}")

elif test_case == "decimal_values":
    # Test with decimal values
    Temperature.celsius_readings = []
    Temperature.add_reading(36.5)  # Normal body temperature
    Temperature.add_reading(37.2)  # Slight fever
    Temperature.add_reading(36.9)  # Normal variation
    print(f"Average reading: {Temperature.average_reading()}")

elif test_case == "many_readings":
    # Test with many readings
    Temperature.celsius_readings = []
    for i in range(1, 101):
        Temperature.add_reading(i)
    print(f"Average reading with 100 values: {Temperature.average_reading()}")
