from book import Book
from user import User
from library import Library
import time

# Comprehensive test case handler
test_case = input()

if test_case == "search_match":
    library = Library("Community Library")
    
    # Add some books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "123456"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "789012"))
    library.add_book(Book("Great Expectations", "Charles Dickens", "345678"))
    
    # Search for books
    search_term = "great"
    found_books = library.search_by_title(search_term)
    
    print(f"Found {len(found_books)} books matching '{search_term}':")
    for book in found_books:
        print(f"- {book.title} by {book.author}")

elif test_case == "search_no_match":
    library = Library("Community Library")
    
    # Add some books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "123456"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "789012"))
    
    # Search for books
    search_term = "nonexistent"
    found_books = library.search_by_title(search_term)
    
    print(f"Found {len(found_books)} books matching '{search_term}'")

elif test_case == "case_insensitive":
    library = Library("Community Library")
    
    # Add some books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "123456"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "789012"))
    
    # Search with different cases
    search_terms = ["GREAT", "great", "Great", "gReAt"]
    
    for term in search_terms:
        found_books = library.search_by_title(term)
        print(f"Search for '{term}': {len(found_books)} book(s) found")

elif test_case == "empty_search":
    library = Library("Community Library")
    
    # Add some books
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "123456"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "789012"))
    library.add_book(Book("Great Expectations", "Charles Dickens", "345678"))
    
    # Search with empty string
    search_term = ""
    found_books = library.search_by_title(search_term)
    
    print(f"Empty search returned {len(found_books)} books (should be all books)")
    print(f"Library has {len(library.books)} total books")

elif test_case == "empty_library":
    library = Library("Empty Library")
    
    # Search in empty library
    search_term = "anything"
    found_books = library.search_by_title(search_term)
    
    print(f"Search in empty library returned {len(found_books)} books")

elif test_case == "special_characters":
    library = Library("Special Characters Library")
    
    # Add books with special characters
    library.add_book(Book("Harry Potter & the Sorcerer's Stone", "J.K. Rowling", "111111"))
    library.add_book(Book("The C++ Programming Language", "Bjarne Stroustrup", "222222"))
    library.add_book(Book("The !@#$%^& Book", "Special Author", "333333"))
    
    # Search for special characters
    special_terms = ["&", "++", "!@#"]
    
    for term in special_terms:
        found_books = library.search_by_title(term)
        print(f"Search for '{term}': {len(found_books)} book(s) found")
        for book in found_books:
            print(f"- {book.title}")

elif test_case == "performance_test":
    library = Library("Large Library")
    
    # Add many books (100 books)
    for i in range(1, 101):
        if i % 10 == 0:  # Every 10th book has "performance" in the title
            library.add_book(Book(f"Performance Book #{i}", f"Author {i}", str(i)))
        else:
            library.add_book(Book(f"Book #{i}", f"Author {i}", str(i)))
    
    # Measure search time
    start_time = time.time()
    search_term = "performance"
    found_books = library.search_by_title(search_term)
    end_time = time.time()
    
    print(f"Found {len(found_books)} books with '{search_term}' in the title")
    print(f"Search took {end_time - start_time:.6f} seconds")
    print(f"First matching book: {found_books[0].title if found_books else 'None'}")
