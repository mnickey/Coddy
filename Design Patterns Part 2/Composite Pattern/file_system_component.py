from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    """Abstract base class for all file system components.
    
    This class serves as the 'Component' in the Composite pattern.
    """
    
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @abstractmethod
    def get_size(self):
        """Returns the size of the component."""
        pass
    
    @abstractmethod
    def display(self, indent=0):
        """Displays the component with proper indentation."""
        pass
    
    @abstractmethod
    def add(self, component):
        """Adds a component to this component."""
        pass
    
    @abstractmethod
    def remove(self, component):
        """Removes a component from this component."""
        pass
    
    @abstractmethod
    def get_component(self, name):
        """Retrieves a component by name."""
        pass
