def create_person(**kwargs):
    # TODO: Create a dictionary from the kwargs
    # TODO: Print "Person created with properties:"
    # TODO: Loop through each key-value pair in the dictionary
    # TODO: Print each key-value pair on a new line in the format "key: value"
    details = kwargs
    print("Person created with properties:")
    for key, value in details.items():
        print(f"{key}: {value}")
