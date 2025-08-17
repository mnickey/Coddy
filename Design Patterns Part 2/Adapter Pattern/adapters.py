from interfaces import DataProcessor, DataVisualizer
from legacy_system import LegacyDataAnalyzer, LegacyChartGenerator

class LegacyDataAnalyzerAdapter(DataProcessor):
    """Adapter for LegacyDataAnalyzer to work with the DataProcessor interface."""
    
    def __init__(self):
        # TODO: Initialize the adapter with a LegacyDataAnalyzer instance
        # TODO: Create self.legacy_analyzer as a LegacyDataAnalyzer object
        self.legacy_analyzer = LegacyDataAnalyzer()
        
    def process_data(self, data):
        """Process data using the legacy analyzer."""
        # TODO: Implement data validation to ensure data is a list
        if not isinstance(data, list):
            raise ValueError("Data must be a list of numeric values")
        # TODO: Validate that all items in data are numeric (int or float)
        # TODO: Raise ValueError with appropriate message if validation fails
        for item in data:
            if not isinstance(item, int) and not isinstance(item, float):
                raise ValueError("All data items must be numeric")
        # TODO: Use legacy_analyzer.load_data() to load the data
        self.legacy_analyzer.load_data(data)
        # TODO: Use legacy_analyzer.run_analysis() to process the data
        self.legacy_analyzer.run_analysis()
        # TODO: Return True on successful processing
        return True
        
    def get_results(self):
        """Get results from the legacy analyzer."""
        # TODO: Use legacy_analyzer.fetch_results() to get results
        # TODO: Return empty dictionary {} if results is None
        # TODO: Otherwise return the results as received
        results = self.legacy_analyzer.fetch_results()
        if results is None:
            return {}
        else:
            return results

class LegacyChartGeneratorAdapter(DataVisualizer):
    """Adapter for LegacyChartGenerator to work with the DataVisualizer interface."""
    
    def __init__(self, chart_type="bar"):
        # TODO: Create self.legacy_chart_generator as a LegacyChartGenerator instance
        # TODO: Store chart_type as self.chart_type
        # TODO: Initialize the legacy chart generator with the chart_type
        self.legacy_chart_generator = LegacyChartGenerator()
        self.chart_type = chart_type
        self.legacy_chart_generator.initialize_chart(self.chart_type)
        
    def visualize(self, data):
        """Create visualization using the legacy chart generator."""
        # TODO: Implement data validation to ensure data is a list
        # TODO: Validate that all items in data are numeric (int or float)
        if not isinstance(data, list):
            raise ValueError("Data must be a list of numeric values")
        
        for item in data:
            if not isinstance(item, (int, float)):
                raise ValueError("All data items must be numeric")
        # TODO: Raise ValueError with appropriate message if validation fails
        # TODO: Use legacy_chart_generator.add_data_series() to add data
        # TODO: Use legacy_chart_generator.render() to create the chart
        # TODO: Return the success status from render()
        self.legacy_chart_generator.add_data_series(data)
        success = self.legacy_chart_generator.render()
        return success
        
    def export_visualization(self, filename):
        """Export the visualization to a file using the legacy chart generator."""
        # TODO: Check if filename ends with '.png', '.jpg', or '.pdf'
        allowed_extensions = ('.png', '.jpg', '.pdf')
        if not filename.lower().endswith(allowed_extensions):
            filename += ".png"
        # TODO: If no valid extension, append '.png' as default
        # TODO: Use legacy_chart_generator.save_chart() to save the file
        # TODO: Return the success status from save_chart()
        return self.legacy_chart_generator.save_chart(filename)
