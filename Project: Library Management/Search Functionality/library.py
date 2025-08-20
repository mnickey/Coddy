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
    
    # TODO: Implement the search_by_title method that:
    # 1. Takes a title parameter (string to search for in book titles)
    # 2. Returns a list of all books whose titles contain the search term
    # 3. The search should be case-insensitive (e.g., "GREAT" matches "Great")
    # 4. The search should match partial titles (e.g., "great" matches "The Great Gatsby")
    # 5. Use a list comprehension to filter the books
    # 6. Convert both the search term and book titles to lowercase for comparison
    def search_by_title(self, title):
        search_term = title.lower()
        return [book for book in self.books if search_term in book.title.lower()]
        
    def __str__(self):
        return f"{self.name} Library with {len(self.books)} books and {len(self.users)} users"
