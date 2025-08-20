from book import Book
from user import User

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def add_user(self, user):
        self.users.append(user)
    
    # TODO: Implement the borrow_book method that takes book_isbn and user_id parameters
    def borrow_book(self, book_isbn, user_id):
        # TODO: Find the book with matching ISBN using next() and generator expression
        # Hint: book = next((book for book in self.books if book.isbn == book_isbn), None)
        book = next((book for book in self.books if book.isbn == book_isbn), None)

        # TODO: Find the user with matching user_id using next() and generator expression
        # Hint: user = next((user for user in self.users if user.user_id == user_id), None)
        user = next((user for user in self.users if user.user_id == user_id), None)

        # TODO: Check if book exists, if not return "Book not found"
        if not book:
            return f"Book not found"
        # TODO: Check if user exists, if not return "User not found"
        if not user:
            return f"User not found"
        # TODO: Check if book is available, if not return "Book is not available"
        if not book.available:
            return f"Book is not available"
        # TODO: Update book's available status to False
        book.available = False
        # TODO: Set book's borrower to the user
        book.borrower = user
        # TODO: Add the book to user's books_borrowed list
        user.books_borrowed.append(book)
        # TODO: Return "Book borrowed successfully"
        return f"Book borrowed successfully"
        
    def __str__(self):
        return f"{self.name} Library with {len(self.books)} books and {len(self.users)} users"
