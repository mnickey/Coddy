# TODO: Import the MediaItem class from mediaitem.py
# Use format: from mediaitem import MediaItem
from mediaitem import MediaItem

class MovieComposition:
    def __init__(self, title, director, year):
        # TODO: Create a MediaItem instance and store it as self.media
        # TODO: Pass title, director, and year to the MediaItem constructor
        self.media = MediaItem(title, director, year)
    
    def display_info(self):
        # TODO: Return a formatted string using the media object's attributes
        # TODO: Format should be: "Movie: {title} directed by {creator} ({year})"
        # Example: "Movie: Inception directed by Christopher Nolan (2010)"
        return f"Movie: {self.title} directed by {self.creator} ({self.year})"
