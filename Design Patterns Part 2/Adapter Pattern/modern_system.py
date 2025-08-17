from interfaces import DataProcessor, DataVisualizer

class AnalyticsSystem:
    """Modern analytics system that works with the new interfaces."""
    
    def __init__(self, data_processor: DataProcessor, data_visualizer: DataVisualizer):
        """Initialize with processor and visualizer components."""
        # TODO: Store data_processor as self.processor
        # TODO: Store data_visualizer as self.visualizer
        self.processor = data_processor
        self.visualizer = data_visualizer
        
    def analyze_and_visualize(self, data, output_file="output.png"):
        """Process data and create visualization."""
        # TODO: Use self.processor.process_data() to process the input data
        # TODO: Use self.processor.get_results() to get analysis results
        # TODO: Use self.visualizer.visualize() to create visualization of the data
        # TODO: Use self.visualizer.export_visualization() to save to output_file
        # TODO: Return a dictionary with keys "analysis_results" and "visualization_file"
        # TODO: "analysis_results" should contain the results from processor
        # TODO: "visualization_file" should contain the output_file parameter
        self.processor.process_data(data)
        analysis_results = self.processor.get_results()
        
        self.visualizer.visualize(data)
        self.visualizer.export_visualization(output_file)
        return {
            "analysis_results": analysis_results,
            "visualization_file": output_file
            }
        
    def get_analysis_summary(self):
        """Get a summary of the analysis results."""
        # TODO: Get results using self.processor.get_results()
        # TODO: If results is empty/None, return "No analysis results available"
        # TODO: Create a summary list by iterating through results items
        # TODO: For numeric values (int, float), format as "{key}: {value:.2f}"
        # TODO: For other values, format as "{key}: {value}"
        # TODO: Join all summary items with newline characters and return
        results = self.processor.get_results()
        if not results:
            return "No analysis results available"
        
        summary_list = []

        for key, value in results.items():
            if isinstance(value, (int, float)):
                summary_list.append(f"{key}: {value:.2f}")
            else:
                summary_list.append(f"{key}: {value}")
        
        return "\n".join(summary_list)
        
