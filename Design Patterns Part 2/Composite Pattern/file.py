from file_system_component import FileSystemComponent

class File(FileSystemComponent):
    """Represents a file in the file system.
    
    This class serves as the 'Leaf' in the Composite pattern.
    """
    
    def __init__(self, name, size):
        super().__init__(name)
        if size < 0:
            raise ValueError("Size cannot be negative")
        self._size = size
    
    def get_size(self):
        return self._size
    
    def display(self, indent=0):
        return " " * indent + f"File: {self.name} ({self.get_size()} KB)"
    
    def add(self, component):
        raise NotImplementedError("Cannot add components to a file")
    
    def remove(self, component):
        raise NotImplementedError("Cannot remove components from a file")
    
    def get_component(self, name):
        raise NotImplementedError("Files don't have components")
