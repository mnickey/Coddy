# TODO: Import the Playable interface from playable.py
# Use format: from playable import Playable
from playable import Playable

class MediaPlayer:
    """
    Media player class that can work with any object implementing the Playable interface.
    """
    def __init__(self):
        # TODO: Initialize the MediaPlayer with a current_media attribute set to None
        self.current_media = None 
    
    def set_media(self, media):
        # TODO: Implement the set_media method to set the current_media attribute
        # This method should accept any object that implements the Playable interface
        self.current_media = media
    
    def play(self):
        # TODO: Implement the play method that delegates to the current media's play method
        # If current_media is None, return "No media set"
        # Otherwise, call and return the result of current_media.play()
        if self.current_media == None:
            return "No media set"
        else:
            return self.current_media.play()
    
    def pause(self):
        # TODO: Implement the pause method that delegates to the current media's pause method
        # If current_media is None, return "No media set"
        # Otherwise, call and return the result of current_media.pause()
        if self.current_media == None:
            return "No media set"
        else:
            return self.current_media.pause()
    
    def stop(self):
        # TODO: Implement the stop method that delegates to the current media's stop method
        # If current_media is None, return "No media set"
        # Otherwise, call and return the result of current_media.stop()
        if self.current_media == None:
            return "No media set"
        else:
            return self.current_media.stop()
