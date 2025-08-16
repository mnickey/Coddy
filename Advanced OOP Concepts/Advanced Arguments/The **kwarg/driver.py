from person_creator import create_person

# Comprehensive test case handler
test_case = input()

if test_case == "basic_test":
    create_person(name="John", age=25, occupation="Engineer")
    # Output:
    # Person created with properties:
    # name: John
    # age: 25
    # occupation: Engineer

elif test_case == "empty_test":
    create_person()
    # Output:
    # Person created with properties:
    # (no additional output since there are no properties)

elif test_case == "many_properties":
    create_person(name="Alice", age=30, occupation="Doctor", city="New York", 
                 country="USA", hobby="Reading", email="alice@example.com")
    # Output:
    # Person created with properties:
    # name: Alice
    # age: 30
    # occupation: Doctor
    # city: New York
    # country: USA
    # hobby: Reading
    # email: alice@example.com

elif test_case == "special_characters":
    create_person(name="Bob", email="bob@example.com", phone="123-456-7890")
    # Output:
    # Person created with properties:
    # name: Bob
    # email: bob@example.com
    # phone: 123-456-7890

elif test_case == "numeric_keys":
    create_person(name="Charlie", age=35, height=175, weight=70)
    # Output:
    # Person created with properties:
    # name: Charlie
    # age: 35
    # height: 175
    # weight: 70

elif test_case == "boolean_values":
    create_person(name="David", is_student=True, is_employed=False)
    # Output:
    # Person created with properties:
    # name: David
    # is_student: True
    # is_employed: False

elif test_case == "nested_structures":
    create_person(name="Eve", hobbies=["Reading", "Swimming", "Coding"], 
                 address={"city": "Boston", "state": "MA", "zip": "02108"})
    # Output:
    # Person created with properties:
    # name: Eve
    # hobbies: ['Reading', 'Swimming', 'Coding']
    # address: {'city': 'Boston', 'state': 'MA', 'zip': '02108'}

elif test_case == "unicode_characters":
    create_person(name="José", city="São Paulo", country="Brasil")
    # Output:
    # Person created with properties:
    # name: José
    # city: São Paulo
    # country: Brasil
