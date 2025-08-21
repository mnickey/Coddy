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
    
    # TODO: Implement the get_statistics method that returns a dictionary with the following statistics:
    # - "total_books": the total number of books in the library
    # - "available_books": the number of books that are available for borrowing
    # - "borrowed_books": the number of books that are currently borrowed
    # - "total_users": the total number of users in the library
    # - "users_with_books": the number of users who have borrowed at least one book
    def get_statistics(self):
        # TODO: Calculate total_books as the length of the books list
        # TODO: Calculate available_books by counting books where available is True
        # TODO: Calculate borrowed_books as total_books minus available_books
        # TODO: Calculate total_users as the length of the users list
        # TODO: Calculate users_with_books by counting users with non-empty books_borrowed list
        # TODO: Return a dictionary with all these statistics
        total_books = len(self.books)
        available_books = sum(1 for book in self.books if book.available)
        borrowed_books = total_books - available_books
        total_users = len(self.users)
        users_with_books = sum(1 for user in self.users if user.books_borrowed)

        return {
            "total_books": total_books,
            "available_books": available_books,
            "borrowed_books": borrowed_books,
            "total_users": total_users,
            "users_with_books": users_with_books
        }
        
    def __str__(self):
        return f"{self.name} Library with {len(self.books)} books and {len(self.users)} users"
