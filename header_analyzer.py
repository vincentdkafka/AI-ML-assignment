
"""
This script reads headers from a CSV file and generates descriptive text for each header
using a local Hugging Face transformer model. The output is displayed on console and
saved to a text file.

This is the main entry point that coordinates between the model and utility modules.
"""


from model import HeaderAnalysisModel
from utils import (
    load_csv_headers,
    save_results_to_file,
    display_results,
    print_startup_message,
    print_success_message,
    validate_csv_file
)


def main():
    """
    Main execution function that coordinates the entire analysis process.
    
    This function:
    1. Loads CSV headers using utilities
    2. Initializes the AI model
    3. Analyzes headers using the model
    4. Displays and saves results using utilities
    """
    print_startup_message()
    
    
    csv_file = "demo.csv"
    output_file = "output.txt"
    
    if not validate_csv_file(csv_file):
        print("❌ Cannot proceed with invalid CSV file. Exiting.")
        return False
    
    headers = load_csv_headers(csv_file)
    if not headers:
        print("❌ Cannot proceed without valid headers. Exiting.")
        return False
    
    model = HeaderAnalysisModel()
    if not model.initialize_model():
        print("❌ Cannot proceed without model. Exiting.")
        return False

    results = model.analyze_headers(headers)
    
    if not results:
        print("❌ No analysis results generated. Exiting.")
        return False
    
    display_results(results)
    
    save_results_to_file(results, output_file)
    
    print_success_message()
    
    return True


if __name__ == "__main__":
    try:
        success = main()
        if not success:
            exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠ Analysis interrupted by user.")
        exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        exit(1)
