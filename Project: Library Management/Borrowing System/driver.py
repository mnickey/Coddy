from book import Book
from user import User
from library import Library
import random

# Comprehensive test case handler
test_case = input()

# Basic functionality tests
if test_case == "borrow_success":
    library = Library("Community Library")
    
    # Add books and users
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456")
    library.add_book(book)
    
    user = User("U001", "Alice")
    library.add_user(user)
    
    # Borrow book
    result = library.borrow_book("123456", "U001")
    print(result)
    print(f"Book available: {book.available}")
    print(f"Books borrowed by user: {len(user.books_borrowed)}")

elif test_case == "book_not_found":
    library = Library("Community Library")
    user = User("U001", "Alice")
    library.add_user(user)
    
    result = library.borrow_book("nonexistent", "U001")
    print(result)

elif test_case == "user_not_found":
    library = Library("Community Library")
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456")
    library.add_book(book)
    
    result = library.borrow_book("123456", "nonexistent")
    print(result)
    
elif test_case == "book_not_available":
    library = Library("Community Library")
    
    # Add books and users
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456")
    book.available = False  # Book is already borrowed
    library.add_book(book)
    
    user = User("U001", "Alice")
    library.add_user(user)
    
    # Try to borrow unavailable book
    result = library.borrow_book("123456", "U001")
    print(result)

# Edge cases and additional tests
elif test_case == "multiple_books":
    library = Library("Community Library")
    user = User("U001", "Alice")
    library.add_user(user)
    
    # Create multiple books
    books = [
        Book("Book 1", "Author 1", "111"),
        Book("Book 2", "Author 2", "222"),
        Book("Book 3", "Author 3", "333")
    ]
    
    for book in books:
        library.add_book(book)
    
    # Borrow multiple books
    results = []
    for book in books:
        results.append(library.borrow_book(book.isbn, "U001"))
    
    for result in results:
        print(result)
    
    print(f"Total books borrowed: {len(user.books_borrowed)}")

elif test_case == "multiple_users":
    library = Library("Community Library")
    book = Book("Popular Book", "Famous Author", "999")
    library.add_book(book)
    
    # Create multiple users
    users = [
        User("U001", "Alice"),
        User("U002", "Bob"),
        User("U003", "Charlie")
    ]
    
    for user in users:
        library.add_user(user)
    
    # Try to borrow the same book with different users
    result1 = library.borrow_book("999", "U001")
    result2 = library.borrow_book("999", "U002")  # Should fail
    
    print(result1)
    print(result2)
    print(f"Book's borrower: {book.borrower.name}")

elif test_case == "return_book":
    library = Library("Community Library")
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456")
    library.add_book(book)
    
    user = User("U001", "Alice")
    library.add_user(user)
    
    # Borrow the book
    borrow_result = library.borrow_book("123456", "U001")
    print(borrow_result)
    
    # Verify book status
    print(f"Book available: {book.available}")
    print(f"Book borrower: {book.borrower.name}")
    print(f"User's borrowed books: {len(user.books_borrowed)}")
    print(f"First borrowed book title: {user.books_borrowed[0].title}")

elif test_case == "empty_library":
    library = Library("Empty Library")
    result = library.borrow_book("any_isbn", "any_user_id")
    print(result)

elif test_case == "stress_test":
    library = Library("Large Library")
    
    # Create and add 100 books
    for i in range(1, 101):
        book = Book(f"Book {i}", f"Author {i}", f"ISBN-{i}")
        library.add_book(book)
    
    # Create and add 50 users
    for i in range(1, 51):
        user = User(f"U{i:03d}", f"User {i}")
        library.add_user(user)
    
    # Perform 200 borrow operations
    successful = 0
    book_not_found = 0
    user_not_found = 0
    not_available = 0
    
    for _ in range(200):
        # Generate random ISBNs and user IDs (some valid, some invalid)
        isbn = f"ISBN-{random.randint(1, 120)}"  # Some will be invalid
        user_id = f"U{random.randint(1, 60):03d}"  # Some will be invalid
        
        result = library.borrow_book(isbn, user_id)
        
        if result == "Book borrowed successfully":
            successful += 1
        elif result == "Book not found":
            book_not_found += 1
        elif result == "User not found":
            user_not_found += 1
        elif result == "Book is not available":
            not_available += 1
    
    print(f"Successful borrows: {successful}")
    print(f"Book not found: {book_not_found}")
    print(f"User not found: {user_not_found}")
    print(f"Book not available: {not_available}")

elif test_case == "borrower_reference":
    library = Library("Community Library")
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456")
    library.add_book(book)
    
    user = User("U001", "Alice")
    library.add_user(user)
    
    # Borrow the book
    library.borrow_book("123456", "U001")
    
    # Verify references
    print(f"Book's borrower name: {book.borrower.name}")
    print(f"First book in user's borrowed list: {user.books_borrowed[0].title}")
