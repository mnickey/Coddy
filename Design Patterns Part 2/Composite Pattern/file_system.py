from directory import Directory

class FileSystem:
    """Represents the overall file system.
    
    This class serves as a facade for working with the file system components.
    """
    
    def __init__(self):
        self.root = Directory("root")
    
    def _get_directory_from_path(self, path):
        """Helper method to navigate to a directory from a path."""
        if not path or path == "/":
            return self.root
            
        path_parts = path.strip("/").split("/")
        current_dir = self.root
        
        # Navigate through the path except the last part
        for i in range(len(path_parts)):
            part = path_parts[i]
            if not part:  # Skip empty parts
                continue
                
            component = current_dir.get_component(part)
            if not component:
                raise ValueError(f"Path not found: {path}")
            if i == len(path_parts) - 1:  # If this is the last part
                return current_dir, component
            if not isinstance(component, Directory):
                raise ValueError(f"{part} is not a directory")
            current_dir = component
            
        return current_dir, None
    
    def add_to_path(self, path, component):
        """Adds a component at the specified path."""
        if not path or path == "/":
            self.root.add(component)
            return
            
        parent_path = "/".join(path.strip("/").split("/")[:-1])
        parent_dir, _ = self._get_directory_from_path(f"/{parent_path}")
        parent_dir.add(component)
    
    def remove_from_path(self, path):
        """Removes a component at the specified path."""
        if not path or path == "/":
            raise ValueError("Cannot remove root directory")
            
        parent_dir, component = self._get_directory_from_path(path)
        if component:
            parent_dir.remove(component)
        else:
            raise ValueError(f"Path not found: {path}")
    
    def get_from_path(self, path):
        """Retrieves a component at the specified path."""
        if not path or path == "/":
            return self.root
            
        _, component = self._get_directory_from_path(path)
        return component
    
    def display(self):
        """Displays the entire file system."""
        return self.root.display()
    
    def get_total_size(self):
        """Returns the total size of all files in the system."""
        return self.root.get_size()
