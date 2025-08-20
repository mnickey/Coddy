class Library:
    def __init__(self, name):
        # TODO: Initialize the Library class with the given name parameter
        # TODO: Store the name parameter as an instance attribute called 'name'
        # TODO: Initialize an empty list called 'books' as an instance attribute
        # TODO: Initialize an empty list called 'users' as an instance attribute
        self.name = name
        self.books = []
        self.users = []

        
    def __str__(self):
        # TODO: Implement the string representation method
        # TODO: Return a formatted string that includes:
        #       - The library name
        #       - The number of books (use len(self.books))
        #       - The number of users (use len(self.users))
        # TODO: Format should be: "[name] Library with [number of books] books and [number of users] users"
        return f"{self.name} Library with {len(self.books)} books and {len(self.users)} users"


        
