from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """Modern interface for data processing components."""
    
    @abstractmethod
    def process_data(self, data):
        """Process the provided data."""
        pass
        
    @abstractmethod
    def get_results(self):
        """Retrieve the processed results."""
        pass


class DataVisualizer(ABC):
    """Modern interface for data visualization components."""
    
    @abstractmethod
    def visualize(self, data):
        """Create a visualization of the data."""
        pass
        
    @abstractmethod
    def export_visualization(self, filename):
        """Export the visualization to a file."""
        pass
