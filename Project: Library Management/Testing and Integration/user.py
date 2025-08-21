class User:
    def __init__(self, user_id, name):
        # TODO: Initialize the user with user_id and name parameters
        # TODO: Store user_id as self.user_id
        # TODO: Store name as self.name
        # TODO: Initialize self.books_borrowed as an empty list
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []
    
    def __str__(self):
        # TODO: Return a string in the format: "User: [name] (ID: [user_id]) - Books borrowed: [number of books]"
        # TODO: Use len(self.books_borrowed) to get the number of books
        return f"User: {self.name} (ID: {self.user_id}) - Books borrowed: {len(self.books_borrowed)}"
    
    def return_all_books(self, library):
        # TODO: Create a copy of self.books_borrowed to iterate over (use books_to_return = self.books_borrowed.copy())
        # TODO: Initialize a counter variable (return_count) to track the number of books returned
        # TODO: For each book in the copy:
        #       - Set book.available to True
        #       - Set book.borrower to None
        #       - Remove the book from self.books_borrowed
        #       - Increment the return_count
        # TODO: Return the return_count (number of books returned)
        books_to_return = self.books_borrowed.copy()
        return_count = 0
        for book in books_to_return:
            book.available = True
            book.borrower = None
            self.books_borrowed.remove(book)
            return_count += 1
        return return_count
