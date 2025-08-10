# TODO: Import the abstract base classes from playable.py
# Use format: from playable import Playable, MediaInfo
from playable import Playable, MediaInfo

class Song(Playable, MediaInfo):
    """
    Concrete implementation of a Song that implements both Playable and MediaInfo interfaces.
    """
    def __init__(self, title, artist, duration):
        # TODO: Initialize the Song object with title, artist, and duration attributes
        # Store these as instance attributes (self.title, self.artist, self.duration)
        self.title = title
        self.artist = artist
        self.duration = duration
    
    def play(self):
        # TODO: Implement the play method from Playable interface
        # Return a string in the format: "Playing song: {title}"
        return f"Playing song: {self.title}"
    
    def pause(self):
        # TODO: Implement the pause method from Playable interface
        # Return a string in the format: "Paused song: {title}"
        return f"Paused song: {self.title}"
    
    def stop(self):
        # TODO: Implement the stop method from Playable interface
        # Return a string in the format: "Stopped song: {title}"
        return f"Stopped song: {self.title}"
    
    def get_title(self):
        # TODO: Implement the get_title method from MediaInfo interface
        # Return the title of the song
        return self.title
    
    def get_duration(self):
        # TODO: Implement the get_duration method from MediaInfo interface
        # Return the duration in seconds
        return self.duration
    
    def get_info(self):
        # TODO: Implement the get_info method from MediaInfo interface
        # Calculate minutes and seconds from duration (minutes = duration // 60, seconds = duration % 60)
        minutes = self.duration // 60
        seconds = self.duration % 60
        # Return a string in the format: "Song: {title} by {artist} ({minutes}:{seconds:02d})"
        # Note: seconds should be zero-padded to two digits
        return f"Song: {self.title} by {self.artist} ({minutes}:{seconds:02d})"
