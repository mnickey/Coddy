from file_manager import FileManager

# Comprehensive test case handler
test_case = input()

if test_case == "basic_test":
    # Create a FileManager instance
    manager = FileManager()
    # Call the read_file method
    print(manager.read_file("example.txt"))
    # Call the get_file_content method
    print(manager.get_file_content("example.txt"))

elif test_case == "protected_access":
    # Create a FileManager instance
    manager = FileManager()
    # Try to call the protected method
    # Protected methods are accessible but intended for internal use
    print(manager._check_permissions("example.txt"))
    print("Note: Protected methods are accessible but intended for internal use only")

elif test_case == "private_access":
    # Create a FileManager instance
    manager = FileManager()
    try:
        # Try to call the private method directly
        print(manager.__decrypt_content("some content"))
    except AttributeError as e:
        print(f"Error: {e}")
        print("Private methods are name-mangled and cannot be accessed directly")
    
    # Access using name-mangled form
    print(manager._FileManager__decrypt_content("some content"))
    print("Note: Accessed private method using name-mangled form")

elif test_case == "method_chaining":
    # Create a FileManager instance
    manager = FileManager()
    # Demonstrate how get_file_content internally calls both protected and private methods
    print("Calling get_file_content which internally uses protected and private methods:")
    print(manager.get_file_content("example.txt"))

elif test_case == "multiple_files":
    # Create a FileManager instance
    manager = FileManager()
    # Process multiple files
    files = ["document.txt", "image.jpg", "data.csv"]
    
    for file in files:
        print(f"\
Processing {file}:")
        print(manager.read_file(file))
        print(manager.get_file_content(file))

elif test_case == "name_mangling":
    # Create a FileManager instance
    manager = FileManager()
    # Demonstrate name mangling
    print("Python's name mangling for private methods:")
    print("Attempting direct access would fail with AttributeError")
    print("Using mangled name:")
    print(manager._FileManager__decrypt_content("private data"))
    print("\
Name mangling is Python's mechanism to prevent accidental access")
    print("It renames __method to _ClassName__method internally")
