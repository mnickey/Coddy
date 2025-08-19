from state import State

# Comprehensive test case handler
test_case = input()

if test_case == "basic_test":
    obj = State("Test Name")
    obj.display_info()

elif test_case == "validation_test":
    obj = State("Validation Test")
    print(f"Name: {obj.name}")

elif test_case == "empty_name_test":
    obj = State("")
    obj.display_info()
    print(f"Name property: {obj.name}")

elif test_case == "special_chars_test":
    obj = State("Test@#$%")
    obj.display_info()
    print(f"Name property: {obj.name}")

elif test_case == "long_name_test":
    long_name = "A" * 100
    obj = State(long_name)
    obj.display_info()
    print(f"Name length: {len(obj.name)}")

elif test_case == "multiple_states_test":
    states = [
        State("California"),
        State("Texas"),
        State("New York"),
        State("Florida")
    ]
    
    for state in states:
        state.display_info()
        print(f"Name via property: {state.name}")

elif test_case == "attribute_access_test":
    obj = State("Access Test")
    # Direct access to private attribute (not recommended)
    print(f"Direct access (not recommended): {obj._name}")
    # Access via property (recommended)
    print(f"Property access (recommended): {obj.name}")

elif test_case == "property_behavior_test":
    obj = State("Original Name")
    print(f"Original name: {obj.name}")
    
    # Try to modify the name (will fail as there's no setter)
    try:
        obj.name = "New Name"
    except AttributeError as e:
        print(f"Error when trying to modify name: {e}")
    
    # Show name is unchanged
    print(f"Name after modification attempt: {obj.name}")
