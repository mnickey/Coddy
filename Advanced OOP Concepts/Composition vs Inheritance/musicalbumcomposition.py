# TODO: Import the MediaItem class from mediaitem.py
# Use format: from mediaitem import MediaItem
from mediaitem import MediaItem

class MusicAlbumComposition:
    def __init__(self, title, artist, year):
        # TODO: Create a MediaItem instance and store it as self.media
        # TODO: Pass title, artist, and year to the MediaItem constructor
        self.media = MediaItem(title, artist, year)
    
    def display_info(self):
        # TODO: Return a formatted string using the media object's attributes
        # TODO: Format should be: "Music Album: {title} by {creator} ({year})"
        # Example: "Music Album: Thriller by Michael Jackson (1982)"
        return f"Music Album: {self.title} by {self.creator} ({self.year})"
