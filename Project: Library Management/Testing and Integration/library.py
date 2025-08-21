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
    
    def borrow_book(self, book_isbn, user_id):
        # Find the book and user
        book = next((book for book in self.books if book.isbn == book_isbn), None)
        user = next((user for user in self.users if user.user_id == user_id), None)
        
        # Check if book and user exist and book is available
        if not book:
            return "Book not found"
        if not user:
            return "User not found"
        if not book.available:
            return "Book is not available"
        
        # Update book and user
        book.available = False
        book.borrower = user
        user.books_borrowed.append(book)
        
        return "Book borrowed successfully"
    
    def return_book(self, book_isbn, user_id):
        # Find the book and user
        book = next((book for book in self.books if book.isbn == book_isbn), None)
        user = next((user for user in self.users if user.user_id == user_id), None)
        
        # Check if book and user exist and book was borrowed by this user
        if not book:
            return "Book not found"
        if not user:
            return "User not found"
        if book.available or book.borrower != user:
            return "This book was not borrowed by this user"
        
        # Update book and user
        book.available = True
        book.borrower = None
        user.books_borrowed.remove(book)
        
        return "Book returned successfully"
        
    def __str__(self):
        return f"{self.name} Library with {len(self.books)} books and {len(self.users)} users"
