# Import the Command class from command.py
from command import Command

# Comprehensive test case handler
test_case = input()

if test_case == "basic_test":
    obj = Command("Test Name")
    obj.display_info()
elif test_case == "validation_test":
    obj = Command("Validation Test")
    print(f"Name: {obj.name}")
elif test_case == "empty_name_test":
    obj = Command("")
    obj.display_info()
    print(f"Empty name handled: {'Yes' if obj.name == '' else 'No'}")
elif test_case == "property_access_test":
    obj = Command("Property Test")
    original_name = obj.name
    try:
        # This should fail since name is a read-only property
        obj.name = "Modified Name"
        print("Property protection failed")
    except AttributeError:
        print("Property protected successfully")
    print(f"Name unchanged: {obj.name == original_name}")
elif test_case == "multiple_commands_test":
    commands = [
        Command("First Command"),
        Command("Second Command"),
        Command("Third Command")
    ]
    for cmd in commands:
        cmd.display_info()
elif test_case == "attribute_test":
    obj = Command("Attribute Test")
    has_private_name = hasattr(obj, "_name")
    print(f"Has _name attribute: {has_private_name}")
elif test_case == "special_chars_test":
    obj = Command("!@#$%^&*()_+{}[]|\\:;\"'<>,.?/")
    obj.display_info()
elif test_case == "long_name_test":
    long_name = "A" * 100
    obj = Command(long_name)
    obj.display_info()
    print(f"Name length: {len(obj.name)}")
