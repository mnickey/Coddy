# TODO: Import the abstract base classes from playable.py
# Use format: from playable import Playable, MediaInfo
from playable import Playable, MediaInfo

class Video(Playable, MediaInfo):
    """
    Concrete implementation of a Video that implements both Playable and MediaInfo interfaces.
    """
    def __init__(self, title, resolution, duration):
        # TODO: Initialize the Video object with title, resolution, and duration attributes
        # Store these as instance attributes (self.title, self.resolution, self.duration)
        self.title = title
        self.resolution = resolution
        self.duration = duration
    
    def play(self):
        # TODO: Implement the play method from Playable interface
        # Return a string in the format: "Playing video: {title}"
        return f"Playing video: {self.title}"
    
    def pause(self):
        # TODO: Implement the pause method from Playable interface
        # Return a string in the format: "Paused video: {title}"
        return f"Paused video: {self.title}"
    
    def stop(self):
        # TODO: Implement the stop method from Playable interface
        # Return a string in the format: "Stopped video: {title}"
        return f"Stopped video: {self.title}"
    
    def get_title(self):
        # TODO: Implement the get_title method from MediaInfo interface
        # Return the title of the video
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
        # Return a string in the format: "Video: {title} ({resolution}) ({minutes}:{seconds:02d})"
        # Note: seconds should be zero-padded to two digits
        return f"Video: {self.title} ({self.resolution}) ({minutes}:{seconds:02d})"
