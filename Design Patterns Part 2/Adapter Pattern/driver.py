# Import all necessary classes
from adapters import LegacyDataAnalyzerAdapter, LegacyChartGeneratorAdapter
from modern_system import AnalyticsSystem

# Comprehensive test case handler
test_case = input()

if test_case == "basic_adapter_test":
    # Test basic adapter functionality
    processor = LegacyDataAnalyzerAdapter()
    data = [1, 2, 3, 4, 5]
    processor.process_data(data)
    results = processor.get_results()
    print(f"Results: {results}")

elif test_case == "visualizer_adapter_test":
    # Test visualizer adapter
    visualizer = LegacyChartGeneratorAdapter("bar")
    data = [10, 20, 30, 40, 50]
    success = visualizer.visualize(data)
    if success:
        export_success = visualizer.export_visualization("test_chart.png")
        print(f"Visualization exported: {export_success}")

elif test_case == "analytics_system_test":
    # Test complete analytics system
    processor = LegacyDataAnalyzerAdapter()
    visualizer = LegacyChartGeneratorAdapter("line")
    system = AnalyticsSystem(processor, visualizer)
    
    data = [15, 25, 35, 45, 55]
    result = system.analyze_and_visualize(data, "analytics_output.png")
    print(f"System result: {result}")

elif test_case == "validation_error_test":
    # Test validation errors
    processor = LegacyDataAnalyzerAdapter()
    try:
        processor.process_data("invalid_data")
        print("Validation failed - should have raised ValueError")
    except ValueError as e:
        print(f"Validation error caught: {e}")

elif test_case == "empty_data_test":
    # Test with empty data
    processor = LegacyDataAnalyzerAdapter()
    try:
        processor.process_data([])
        results = processor.get_results()
        print(f"Empty data results: {results}")
    except Exception as e:
        print(f"Empty data error: {e}")

elif test_case == "chart_types_test":
    # Test different chart types
    chart_types = ["bar", "line", "pie"]
    data = [5, 15, 25, 35]
    
    for chart_type in chart_types:
        visualizer = LegacyChartGeneratorAdapter(chart_type)
        success = visualizer.visualize(data)
        print(f"{chart_type} chart created: {success}")

elif test_case == "file_extension_test":
    # Test file extension handling
    visualizer = LegacyChartGeneratorAdapter()
    data = [1, 2, 3, 4]
    visualizer.visualize(data)
    
    # Test various filename formats
    filenames = ["test", "test.jpg", "test.pdf", "test.png"]
    for filename in filenames:
        success = visualizer.export_visualization(filename)
        print(f"Export '{filename}': {success}")

elif test_case == "summary_test":
    # Test analysis summary
    processor = LegacyDataAnalyzerAdapter()
    visualizer = LegacyChartGeneratorAdapter()
    system = AnalyticsSystem(processor, visualizer)
    
    data = [10, 20, 30, 40, 50, 60]
    system.analyze_and_visualize(data)
    summary = system.get_analysis_summary()
    print("Analysis Summary:")
    print(summary)

elif test_case == "mixed_data_test":
    # Test with mixed numeric data
    processor = LegacyDataAnalyzerAdapter()
    data = [1.5, 2, 3.7, 4, 5.2]
    processor.process_data(data)
    results = processor.get_results()
    print(f"Mixed data results: {results}")

elif test_case == "invalid_numeric_test":
    # Test with invalid numeric data
    processor = LegacyDataAnalyzerAdapter()
    try:
        processor.process_data([1, 2, "three", 4, 5])
        print("Validation failed - should have raised ValueError")
    except ValueError as e:
        print(f"Invalid numeric data error: {e}")

elif test_case == "no_results_summary_test":
    # Test summary with no results
    processor = LegacyDataAnalyzerAdapter()
    visualizer = LegacyChartGeneratorAdapter()
    system = AnalyticsSystem(processor, visualizer)
    
    summary = system.get_analysis_summary()
    print(f"No results summary: {summary}")

elif test_case == "large_dataset_test":
    # Test with larger dataset
    processor = LegacyDataAnalyzerAdapter()
    data = list(range(1, 101))  # 1 to 100
    processor.process_data(data)
    results = processor.get_results()
    print(f"Large dataset - Mean: {results.get('mean', 'N/A'):.2f}")
    print(f"Large dataset - Min: {results.get('min', 'N/A')}")
    print(f"Large dataset - Max: {results.get('max', 'N/A')}")

elif test_case == "complete_workflow_test":
    # Test complete workflow with multiple operations
    processor = LegacyDataAnalyzerAdapter()
    bar_visualizer = LegacyChartGeneratorAdapter("bar")
    line_visualizer = LegacyChartGeneratorAdapter("line")
    
    data = [12, 18, 25, 32, 28, 35, 42]
    
    # Create analytics systems with different visualizers
    bar_system = AnalyticsSystem(processor, bar_visualizer)
    line_system = AnalyticsSystem(LegacyDataAnalyzerAdapter(), line_visualizer)
    
    # Run analyses
    bar_result = bar_system.analyze_and_visualize(data, "bar_chart.png")
    line_result = line_system.analyze_and_visualize(data, "line_chart.png")
    
    print("Complete workflow test completed")
    print(f"Bar chart result: {bar_result['visualization_file']}")
    print(f"Line chart result: {line_result['visualization_file']}")
    
    # Get summaries
    print("Bar system summary:")
    print(bar_system.get_analysis_summary())
    print("Line system summary:")
    print(line_system.get_analysis_summary())
