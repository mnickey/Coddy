# TODO: Import the Library class from library.py
# Use format: from library import Library
from library import Library

# Comprehensive test case handler
test_case = input()

if test_case == "basic_library_creation":
    # TODO: Create a library with name "Test Library"
    # TODO: Print the library object (this will call the __str__ method)
    lib1 = Library("Test Library")
    print(lib1)
    
elif test_case == "library_attributes":
    # TODO: Create a library with name "Test Library"
    # TODO: Print the library's name attribute
    # TODO: Print the length of the books list
    # TODO: Print the length of the users list
    lib1 = Library("Test Library")
    print(f"Name: {lib1.name}")
    print(f"Books: {len(lib1.books)}")
    print(f"Users: {len(lib1.users)}")

elif test_case == "multiple_libraries":
    # TODO: Create two different libraries with names "Library 1" and "Library 2"
    # TODO: Print both library objects
    lib1 = Library("Library 1")
    lib2 = Library("Library 2")
    print(lib1)
    print(lib2)

elif test_case == "empty_name":
    # TODO: Create a library with an empty string as the name
    # TODO: Print the library object
    lib1 = Library("")
    print(lib1)

elif test_case == "special_characters":
    # TODO: Create a library with special characters in the name (e.g., "!@#$%^&*()")
    # TODO: Print the library object
    lib1 = Library("!@#$%^&*()")
    print(lib1)

elif test_case == "very_long_name":
    # TODO: Create a library with a very long name (100+ characters)
    # TODO: Print the library object
    lib1 = Library("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(lib1)

elif test_case == "add_books_users":
    # TODO: Create a library with name "Test Library"
    # TODO: Add some items to the books list (e.g., ["Book1", "Book2"])
    # TODO: Add some items to the users list (e.g., ["User1", "User2"])
    # TODO: Print the library object (should show updated counts)
    lib1 = Library("Test Library")
    lib1.books.append("Book1")
    lib1.books.append("Book2")
    lib1.users.append("User1")
    lib1.users.append("User2")
    lib1.books.append("Book3")
    print(lib1)

elif test_case == "empty_lists":
    # TODO: Create a library with name "Test Library"
    # TODO: Verify that books and users lists are empty by printing their lengths
    lib1 = Library("Test Library")
    print(f"Books length: {len(lib1.books)}")
    print(f"Users length: {len(lib1.users)}")

elif test_case == "type_validation":
    # TODO: Create a library with an integer as the name (e.g., 123)
    # TODO: Print the library object (should convert to string)
    lib1 = Library(123)
    print(lib1)
