from abc import ABC, abstractmethod

class Playable(ABC):
    """
    Abstract base class defining the interface for playable media objects.
    All playable media must implement play, pause, and stop functionality.
    """
    @abstractmethod
    def play(self):
        # TODO: Define abstract method that returns a string in format: "Playing [media type]: [title]"
        # This is an abstract method that will be implemented by concrete classes
        pass
    
    @abstractmethod
    def pause(self):
        # TODO: Define abstract method that returns a string in format: "Paused [media type]: [title]"
        # This is an abstract method that will be implemented by concrete classes
        pass
    
    @abstractmethod
    def stop(self):
        # TODO: Define abstract method that returns a string in format: "Stopped [media type]: [title]"
        # This is an abstract method that will be implemented by concrete classes
        pass

class MediaInfo(ABC):
    """
    Abstract base class defining the interface for media information.
    All media objects must implement methods to retrieve title, duration, and formatted info.
    """
    @abstractmethod
    def get_title(self):
        # TODO: Define abstract method that returns the title of the media
        # This is an abstract method that will be implemented by concrete classes
        pass
    
    @abstractmethod
    def get_duration(self):
        # TODO: Define abstract method that returns the duration in seconds
        # This is an abstract method that will be implemented by concrete classes
        pass
    
    @abstractmethod
    def get_info(self):
        # TODO: Define abstract method that returns formatted information about the media
        # For Song: "Song: [title] by [artist] ([minutes]:[seconds])"
        # For Video: "Video: [title] ([resolution]) ([minutes]:[seconds])"
        # This is an abstract method that will be implemented by concrete classes
        pass 
        
