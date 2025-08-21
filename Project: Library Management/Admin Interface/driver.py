from book import Book
from user import User
from library import Library

# Test case handler
test_case = input()

if test_case == "empty_library":
    library = Library("Empty Library")
    stats = library.get_statistics()
    
    print(f"Total Books: {stats['total_books']}")
    print(f"Available Books: {stats['available_books']}")
    print(f"Borrowed Books: {stats['borrowed_books']}")
    print(f"Total Users: {stats['total_users']}")
    print(f"Users with Books: {stats['users_with_books']}")

elif test_case == "with_borrowed_books":
    library = Library("Community Library")
    
    # Add books and users
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "123456"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "789012"))
    library.add_book(Book("1984", "George Orwell", "345678"))
    
    library.add_user(User("U001", "Alice"))
    library.add_user(User("U002", "Bob"))
    library.add_user(User("U003", "Charlie"))
    
    # Borrow some books
    library.borrow_book("123456", "U001")
    library.borrow_book("789012", "U001") # Alice borrows 2 books
    library.borrow_book("345678", "U002") # Bob borrows 1 book
    
    stats = library.get_statistics()
    print(f"Total Books: {stats['total_books']}")
    print(f"Available Books: {stats['available_books']}")
    print(f"Borrowed Books: {stats['borrowed_books']}")
    print(f"Total Users: {stats['total_users']}")
    print(f"Users with Books: {stats['users_with_books']}")

elif test_case == "return_books":
    library = Library("Return Test Library")
    
    # Add books and users
    library.add_book(Book("Python Programming", "John Smith", "111222"))
    library.add_book(Book("Data Structures", "Jane Doe", "333444"))
    
    library.add_user(User("U101", "David"))
    library.add_user(User("U102", "Emma"))
    
    # Borrow a book
    library.borrow_book("111222", "U101")
    
    # Get statistics before returning
    stats_before = library.get_statistics()
    print("Before returning:")
    print(f"Total Books: {stats_before['total_books']}")
    print(f"Available Books: {stats_before['available_books']}")
    print(f"Borrowed Books: {stats_before['borrowed_books']}")
    print(f"Users with Books: {stats_before['users_with_books']}")
    
    # Return book implementation (would be in Library class)
    book = next((book for book in library.books if book.isbn == "111222"), None)
    user = next((user for user in library.users if user.user_id == "U101"), None)
    
    if book and user:
        book.available = True
        book.borrower = None
        user.books_borrowed.remove(book)
        print("Book returned successfully")
    
    # Get statistics after returning
    stats_after = library.get_statistics()
    print("\
After returning:")
    print(f"Total Books: {stats_after['total_books']}")
    print(f"Available Books: {stats_after['available_books']}")
    print(f"Borrowed Books: {stats_after['borrowed_books']}")
    print(f"Users with Books: {stats_after['users_with_books']}")

elif test_case == "edge_cases":
    # Empty library
    empty_library = Library("Empty Library")
    empty_stats = empty_library.get_statistics()
    print("Empty library statistics:")
    print(f"Total Books: {empty_stats['total_books']}")
    print(f"Available Books: {empty_stats['available_books']}")
    print(f"Borrowed Books: {empty_stats['borrowed_books']}")
    print(f"Total Users: {empty_stats['total_users']}")
    print(f"Users with Books: {empty_stats['users_with_books']}")
    
    # Books but no users
    books_only = Library("Books Only")
    books_only.add_book(Book("Book 1", "Author 1", "B001"))
    books_only.add_book(Book("Book 2", "Author 2", "B002"))
    books_stats = books_only.get_statistics()
    print("\
Library with books but no users:")
    print(f"Total Books: {books_stats['total_books']}")
    print(f"Available Books: {books_stats['available_books']}")
    print(f"Total Users: {books_stats['total_users']}")
    print(f"Users with Books: {books_stats['users_with_books']}")
    
    # Users but no books
    users_only = Library("Users Only")
    users_only.add_user(User("U201", "User 1"))
    users_only.add_user(User("U202", "User 2"))
    users_stats = users_only.get_statistics()
    print("\
Library with users but no books:")
    print(f"Total Books: {users_stats['total_books']}")
    print(f"Available Books: {users_stats['available_books']}")
    print(f"Total Users: {users_stats['total_users']}")
    print(f"Users with Books: {users_stats['users_with_books']}")
    
    # Error cases
    error_library = Library("Error Test")
    error_library.add_book(Book("Error Book", "Error Author", "E001"))
    error_library.add_user(User("E101", "Error User"))
    
    print("\
Error cases:")
    print(f"Borrow non-existent book: {error_library.borrow_book('NONEXISTENT', 'E101')}")
    print(f"Borrow with non-existent user: {error_library.borrow_book('E001', 'NONEXISTENT')}")

elif test_case == "large_library":
    large_library = Library("Large Library")
    
    # Add 100 books
    for i in range(1, 101):
        large_library.add_book(Book(f"Book {i}", f"Author {i}", f"ISBN{i:06d}"))
    
    # Add 100 users
    for i in range(1, 101):
        large_library.add_user(User(f"U{i:03d}", f"User {i}"))
    
    # Have 50 users borrow books
    for i in range(1, 51):
        large_library.borrow_book(f"ISBN{i:06d}", f"U{i:03d}")
    
    # Have some users borrow multiple books
    for i in range(1, 11):
        large_library.borrow_book(f"ISBN{i+50:06d}", f"U{i:03d}")
    
    stats = large_library.get_statistics()
    print("Large library statistics:")
    print(f"Total Books: {stats['total_books']}")
    print(f"Available Books: {stats['available_books']}")
    print(f"Borrowed Books: {stats['borrowed_books']}")
    print(f"Total Users: {stats['total_users']}")
    print(f"Users with Books: {stats['users_with_books']}")
    
    # Verify calculations
    print("\
Verification:")
    print(f"Total books should be 100: {stats['total_books'] == 100}")
    print(f"Borrowed books should be 60: {stats['borrowed_books'] == 60}")
    print(f"Available books should be 40: {stats['available_books'] == 40}")
    print(f"Users with books should be 50: {stats['users_with_books'] == 50}")

elif test_case == "statistics_accuracy":
    accuracy_library = Library("Accuracy Test")
    
    # Add exactly 10 books
    for i in range(1, 11):
        accuracy_library.add_book(Book(f"Book {i}", f"Author {i}", f"A{i:03d}"))
    
    # Add exactly 5 users
    for i in range(1, 6):
        accuracy_library.add_user(User(f"AU{i}", f"Accuracy User {i}"))
    
    # No books borrowed yet
    stats1 = accuracy_library.get_statistics()
    print("Initial state:")
    print(f"Total Books: {stats1['total_books']} (Expected: 10)")
    print(f"Available Books: {stats1['available_books']} (Expected: 10)")
    print(f"Borrowed Books: {stats1['borrowed_books']} (Expected: 0)")
    print(f"Total Users: {stats1['total_users']} (Expected: 5)")
    print(f"Users with Books: {stats1['users_with_books']} (Expected: 0)")
    
    # Have 3 users borrow books
    accuracy_library.borrow_book("A001", "AU1")
    accuracy_library.borrow_book("A002", "AU1")  # User 1 borrows 2 books
    accuracy_library.borrow_book("A003", "AU2")  # User 2 borrows 1 book
    accuracy_library.borrow_book("A004", "AU3")  # User 3 borrows 1 book
    
    stats2 = accuracy_library.get_statistics()
    print("\
After borrowing:")
    print(f"Total Books: {stats2['total_books']} (Expected: 10)")
    print(f"Available Books: {stats2['available_books']} (Expected: 6)")
    print(f"Borrowed Books: {stats2['borrowed_books']} (Expected: 4)")
    print(f"Total Users: {stats2['total_users']} (Expected: 5)")
    print(f"Users with Books: {stats2['users_with_books']} (Expected: 3)")
