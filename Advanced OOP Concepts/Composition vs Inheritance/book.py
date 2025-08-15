# TODO: Import the Media class from media.py
# Use format: from media import Media
from media import Media

class Book(Media):
    # TODO: No need to implement __init__ as it will use the parent class constructor
    
    def display_info(self):
        # TODO: Override the display_info method to return a formatted string
        # TODO: Format should be: "Book: {title} by {creator} ({year})"
        # Example: "Book: The Hobbit by J.R.R. Tolkien (1937)"
        return f"Book: {self.title} by {self.creator} ({self.year})"
