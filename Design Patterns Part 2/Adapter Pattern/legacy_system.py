# This file simulates a legacy system with incompatible interfaces
# DO NOT MODIFY THIS FILE - it represents code you cannot change

class LegacyDataAnalyzer:
    """Legacy class for data analysis with incompatible interface."""
    
    def __init__(self):
        self.data = None
        self.analysis_complete = False
        self.results = {}
    
    def load_data(self, data_points):
        """Load data into the analyzer."""
        self.data = data_points
        print("Legacy analyzer: Data loaded successfully")
        return True
    
    def run_analysis(self):
        """Run the analysis process."""
        if not self.data:
            print("Legacy analyzer: No data to analyze")
            return False
            
        # Simulate analysis
        self.results = {
            'mean': sum(self.data) / len(self.data),
            'max': max(self.data),
            'min': min(self.data)
        }
        self.analysis_complete = True
        print("Legacy analyzer: Analysis complete")
        return True
    
    def fetch_results(self):
        """Get the analysis results."""
        if not self.analysis_complete:
            print("Legacy analyzer: Analysis not yet complete")
            return None
        return self.results


class LegacyChartGenerator:
    """Legacy class for chart generation with incompatible interface."""
    
    def __init__(self):
        self.chart_data = None
        self.chart_type = None
        self.chart_created = False
    
    def initialize_chart(self, chart_type):
        """Set up the chart with a specific type."""
        self.chart_type = chart_type
        self.chart_created = False
        print(f"Legacy chart generator: Initialized {chart_type} chart")
    
    def add_data_series(self, data):
        """Add data to the chart."""
        self.chart_data = data
        print("Legacy chart generator: Data series added")
    
    def render(self):
        """Generate the chart."""
        if not self.chart_type or self.chart_data is None:
            print("Legacy chart generator: Cannot render without chart type and data")
            return False
            
        self.chart_created = True
        print(f"Legacy chart generator: {self.chart_type} chart rendered with {len(self.chart_data)} data points")
        return True
    
    def save_chart(self, file_path):
        """Save the chart to a file."""
        if not self.chart_created:
            print("Legacy chart generator: No chart to save")
            return False
            
        print(f"Legacy chart generator: Chart saved to {file_path}")
        return True
