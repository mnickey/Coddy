# TODO: Import the Media class from media.py
# Use format: from media import Media
from media import Media

class MusicAlbum(Media):
    # TODO: No need to implement __init__ as it will use the parent class constructor
    
    def display_info(self):
        # TODO: Override the display_info method to return a formatted string
        # TODO: Format should be: "Music Album: {title} by {creator} ({year})"
        # Example: "Music Album: Abbey Road by The Beatles (1969)"
        return f"Music Album: {self.title} by {self.creator} ({self.year})"
