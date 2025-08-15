from media import Media
from book import Book
from movie import Movie
from musicalbum import MusicAlbum
from mediaitem import MediaItem
from bookcomposition import BookComposition
from moviecomposition import MovieComposition
from musicalbumcomposition import MusicAlbumComposition

# Comprehensive test case handler
test_case = input()

def test_inheritance_basic():
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    movie = Movie("The Matrix", "Wachowski Sisters", 1999)
    album = MusicAlbum("Abbey Road", "The Beatles", 1969)
    
    assert book.display_info() == "Book: The Hobbit by J.R.R. Tolkien (1937)"
    assert movie.display_info() == "Movie: The Matrix directed by Wachowski Sisters (1999)"
    assert album.display_info() == "Music Album: Abbey Road by The Beatles (1969)"

def test_composition_basic():
    book_comp = BookComposition("Dune", "Frank Herbert", 1965)
    movie_comp = MovieComposition("Inception", "Christopher Nolan", 2010)
    album_comp = MusicAlbumComposition("Thriller", "Michael Jackson", 1982)
    
    assert book_comp.display_info() == "Book: Dune by Frank Herbert (1965)"
    assert movie_comp.display_info() == "Movie: Inception directed by Christopher Nolan (2010)"
    assert album_comp.display_info() == "Music Album: Thriller by Michael Jackson (1982)"

def test_inheritance_relationships():
    book = Book("Test Book", "Test Author", 2000)
    movie = Movie("Test Movie", "Test Director", 2001)
    album = MusicAlbum("Test Album", "Test Artist", 2002)
    
    assert isinstance(book, Book)
    assert isinstance(book, Media)
    assert isinstance(movie, Movie)
    assert isinstance(movie, Media)
    assert isinstance(album, MusicAlbum)
    assert isinstance(album, Media)

def test_attribute_access():
    # Test inheritance approach
    book = Book("Test Book", "Test Author", 2000)
    assert book.title == "Test Book"
    assert book.creator == "Test Author"
    assert book.year == 2000
    
    # Test composition approach
    book_comp = BookComposition("Test Book", "Test Author", 2000)
    assert book_comp.media.title == "Test Book"
    assert book_comp.media.creator == "Test Author"
    assert book_comp.media.year == 2000

def test_polymorphism():
    media_list = [
        Book("Book1", "Author1", 2001),
        Movie("Movie1", "Director1", 2002),
        MusicAlbum("Album1", "Artist1", 2003)
    ]
    
    assert media_list[0].display_info() == "Book: Book1 by Author1 (2001)"
    assert media_list[1].display_info() == "Movie: Movie1 directed by Director1 (2002)"
    assert media_list[2].display_info() == "Music Album: Album1 by Artist1 (2003)"

def test_edge_cases():
    # Empty strings
    book = Book("", "", 0)
    assert book.display_info() == "Book:  by  (0)"
    
    # Special characters - fixed the syntax error here
    movie = Movie("Test\"Movie", "Test\\nDirector", -1)
    assert movie.display_info() == "Movie: Test\"Movie directed by Test\\nDirector (-1)"
    
    # Extreme years
    album = MusicAlbum("Test Album", "Test Artist", 9999)
    assert album.display_info() == "Music Album: Test Album by Test Artist (9999)"

def test_stress():
    # Create many media objects
    books = [Book(f"Book{i}", f"Author{i}", 2000+i) for i in range(100)]
    movies = [Movie(f"Movie{i}", f"Director{i}", 2000+i) for i in range(100)]
    albums = [MusicAlbum(f"Album{i}", f"Artist{i}", 2000+i) for i in range(100)]
    
    for i, book in enumerate(books):
        assert book.display_info() == f"Book: Book{i} by Author{i} ({2000+i})"
    
    for i, movie in enumerate(movies):
        assert movie.display_info() == f"Movie: Movie{i} directed by Director{i} ({2000+i})"
    
    for i, album in enumerate(albums):
        assert album.display_info() == f"Music Album: Album{i} by Artist{i} ({2000+i})"

# Run the appropriate test based on input
if test_case == "default_test" or test_case == "":
    test_inheritance_basic()
    test_composition_basic()
    print("All tests passed!")
elif test_case == "inheritance_test":
    test_inheritance_basic()
    test_inheritance_relationships()
    print("Inheritance tests passed!")
elif test_case == "composition_test":
    test_composition_basic()
    print("Composition tests passed!")
elif test_case == "polymorphism_test":
    test_polymorphism()
    print("Polymorphism tests passed!")
elif test_case == "attribute_test":
    test_attribute_access()
    print("Attribute tests passed!")
elif test_case == "edge_cases":
    test_edge_cases()
    print("Edge case tests passed!")
elif test_case == "stress_test":
    test_stress()
    print("Stress tests passed!")
