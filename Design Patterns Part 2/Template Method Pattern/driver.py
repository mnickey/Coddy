from template import Template

# Test case handler
test_case = input()

if test_case == "basic_test":
    # TODO: Create a Template object with name "Test Name"
    # TODO: Call the display_info() method on the object
    basic_test = Template("Test Name")
    basic_test.display_info()

elif test_case == "validation_test":
    # TODO: Create a Template object with name "Validation Test"
    # TODO: Print the name using the name property in format: "Name: {obj.name}"
    validation_test = Template("Validation Test")
    print(f"Name: {validation_test.name}")
