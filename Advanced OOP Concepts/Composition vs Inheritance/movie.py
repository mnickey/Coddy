# TODO: Import the Media class from media.py
# Use format: from media import Media
from media import Media

class Movie(Media):
    # TODO: No need to implement __init__ as it will use the parent class constructor
    
    def display_info(self):
        # TODO: Override the display_info method to return a formatted string
        # TODO: Format should be: "Movie: {title} directed by {creator} ({year})"
        # Example: "Movie: The Matrix directed by Wachowski Sisters (1999)"
        return f"Movie: {self.title} directed by {self.creator} ({self.year})"
