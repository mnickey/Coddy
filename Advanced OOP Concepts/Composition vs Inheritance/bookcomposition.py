# TODO: Import the MediaItem class from mediaitem.py
# Use format: from mediaitem import MediaItem
from mediaitem import MediaItem

class BookComposition:
    def __init__(self, title, author, year):
        # TODO: Create a MediaItem instance and store it as self.media
        # TODO: Pass title, author, and year to the MediaItem constructor
        self.media = MediaItem(title, author, year)
    
    def display_info(self):
        # TODO: Return a formatted string using the media object's attributes
        # TODO: Format should be: "Book: {title} by {creator} ({year})"
        # Example: "Book: Dune by Frank Herbert (1965)"
        return "Book: {self.title} by {self.creator} ({self.year})"
