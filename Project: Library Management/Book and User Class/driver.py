from book import Book
from library import Library

# Comprehensive test case handler
test_case = input()

if test_case == "create_book":
    library = Library("Community Library")
    title = "Title"
    author = "Author"
    isbn = "ISBN"
    
    book = Book(title, author, isbn)
    print(book)
    
elif test_case == "add_to_library":
    library = Library("Community Library")
    
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "123456")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "789012")
    
    library.add_book(book1)
    library.add_book(book2)
    
    print(f"Library has {len(library.books)} books")
    print(f"Book 1: {library.books[0]}")
    print(f"Book 2: {library.books[1]}")

elif test_case == "book_availability":
    book = Book("1984", "George Orwell", "345678")
    print(f"Initial availability: {book.available}")
    
    # Change availability
    book.available = False
    print(f"After change: {book.available}")
    print(book)  # Should show "Not Available"

elif test_case == "empty_values":
    book = Book("", "", "")
    print(book)
    library = Library("")
    library.add_book(book)
    print(library)

elif test_case == "special_characters":
    book = Book("Title with $#@!", "Author with &*^%", "ISBN-123!@#")
    print(book)

elif test_case == "multiple_books":
    library = Library("Public Library")
    
    books = [
        Book("Book 1", "Author 1", "111111"),
        Book("Book 2", "Author 2", "222222"),
        Book("Book 3", "Author 3", "333333"),
        Book("Book 4", "Author 4", "444444"),
        Book("Book 5", "Author 5", "555555")
    ]
    
    for book in books:
        library.add_book(book)
    
    print(library)
    for i, book in enumerate(library.books):
        print(f"Book {i+1}: {book}")

elif test_case == "borrower_assignment":
    book = Book("The Hobbit", "J.R.R. Tolkien", "987654")
    print(f"Initial borrower: {book.borrower}")
    
    book.borrower = "John Doe"
    book.available = False
    print(f"New borrower: {book.borrower}")
    print(book)

elif test_case == "attribute_access":
    book = Book("Pride and Prejudice", "Jane Austen", "246810")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"ISBN: {book.isbn}")
    print(f"Available: {book.available}")
    print(f"Borrower: {book.borrower}")
    
    # Modify attributes
    book.title = "Updated Title"
    book.author = "Updated Author"
    book.isbn = "999999"
    book.available = False
    book.borrower = "Jane Smith"
    
    print("\
After modifications:")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"ISBN: {book.isbn}")
    print(f"Available: {book.available}")
    print(f"Borrower: {book.borrower}")
