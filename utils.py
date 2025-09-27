
"""
This module contains utility functions for CSV operations, file I/O,
and other helper functions used in the header analysis project.
"""

import pandas as pd
import os
from datetime import datetime


def load_csv_headers(csv_file_path):
    """
    Load the headers (column names) from a CSV file.
    
    Args:
        csv_file_path (str): Path to the CSV file
        
    Returns:
        list: List of header names, empty list if error
    """
    try:
        df = pd.read_csv(csv_file_path, nrows=0)
        headers = df.columns.tolist()
        print(f"✓ Successfully loaded {len(headers)} headers from {csv_file_path}")
        return headers
        
    except FileNotFoundError:
        print(f"✗ Error: CSV file '{csv_file_path}' not found.")
        return []
        
    except Exception as e:
        print(f"✗ Error reading CSV file: {e}")
        return []


def validate_csv_file(csv_file_path):
    """
    Validate that a CSV file exists and is readable.
    
    Args:
        csv_file_path (str): Path to the CSV file
        
    Returns:
        bool: True if file is valid, False otherwise
    """
    if not os.path.exists(csv_file_path):
        print(f"✗ CSV file '{csv_file_path}' does not exist.")
        return False
        
    if not csv_file_path.lower().endswith('.csv'):
        print(f"⚠ Warning: '{csv_file_path}' doesn't have a .csv extension.")
        
    try:
        with open(csv_file_path, 'r') as f:
            first_line = f.readline()
            if not first_line.strip():
                print(f"✗ CSV file '{csv_file_path}' appears to be empty.")
                return False
                
        return True
        
    except Exception as e:
        print(f"✗ Error validating CSV file '{csv_file_path}': {e}")
        return False


def save_results_to_file(results, output_file="output.txt"):
    """
    Save the analysis results to a text file.
    
    Args:
        results (dict): Dictionary of header descriptions
        output_file (str): Output file path
        
    Returns:
        bool: True if saved successfully, False otherwise
    """
    try:
        output_lines = []
        output_lines.append("CSV Header Analysis Results")
        output_lines.append("=" * 40)
        output_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        output_lines.append("")
        
        # Add results
        for header, description in results.items():
            line = f"• {header} → {description}"
            output_lines.append(line)
        
        output_lines.append("")
        output_lines.append("Analysis completed successfully!")
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines))
            
        print(f"💾 Results saved to '{output_file}'")
        return True
        
    except Exception as e:
        print(f"⚠ Warning: Could not save to file '{output_file}': {e}")
        return False


def display_results(results):
    """
    Display the analysis results on the console.
    
    Args:
        results (dict): Dictionary of header descriptions
    """
    if not results:
        print("❌ No results to display.")
        return
        
    print("\n📋 Analysis Results:")
    print("=" * 50)
    
    for header, description in results.items():
        line = f"• {header} → {description}"
        print(line)


def print_header(title, width=50):
    """
    Print a formatted header with decorative borders.
    
    Args:
        title (str): Title text to display
        width (int): Width of the header border
    """
    print(title)
    print("=" * width)


def print_success_message():
    """
    Print a success message when analysis is completed.
    """
    print("\n✅ Analysis completed successfully!")
    print("=" * 50)


def print_startup_message():
    """
    Print the application startup message.
    """
    print("🚀 CSV Header Analyzer Starting...")
    print("=" * 50)


def get_project_info():
    """
    Get basic project information.
    
    Returns:
        dict: Dictionary containing project metadata
    """
    return {
        "name": "CSV Header Analyzer",
        "version": "1.0.0",
        "description": "Analyzes CSV headers using AI to generate descriptive text",
        "author": "Internship Assignment",
        "created": "2024"
    }


def create_sample_csv(file_path="demo.csv"):
    """
    Create a sample CSV file for testing purposes.
    
    Args:
        file_path (str): Path where to create the sample CSV
        
    Returns:
        bool: True if created successfully, False otherwise
    """
    try:
        sample_data = {
            'Invoice_ID': ['INV-001', 'INV-002', 'INV-003', 'INV-004', 'INV-005'],
            'Vendor_Name': [
                'TechCorp Solutions', 
                'Office Supplies Plus', 
                'DataStream Analytics', 
                'CloudSync Services', 
                'Marketing Dynamics'
            ],
            'Amount': [2500.00, 450.75, 15000.00, 899.99, 3200.50],
            'Payment_Date': [
                '2024-01-15', 
                '2024-01-18', 
                '2024-01-22', 
                '2024-01-25', 
                '2024-02-01'
            ]
        }
        
        df = pd.DataFrame(sample_data)
        df.to_csv(file_path, index=False)
        print(f"✓ Sample CSV created: {file_path}")
        return True
        
    except Exception as e:
        print(f"✗ Error creating sample CSV: {e}")
        return False


def validate_output_path(output_path):
    """
    Validate that the output path is writable.
    
    Args:
        output_path (str): Path to validate
        
    Returns:
        bool: True if path is writable, False otherwise
    """
    try:
        test_content = "test"
        with open(output_path, 'w') as f:
            f.write(test_content)
        
        if os.path.exists(output_path):
            os.remove(output_path)
            
        return True
        
    except Exception as e:
        print(f"⚠ Warning: Cannot write to '{output_path}': {e}")
        return False


def format_results_for_display(results):
    """
    Format results dictionary for better display.
    
    Args:
        results (dict): Raw results dictionary
        
    Returns:
        list: List of formatted result strings
    """
    if not results:
        return ["No results available."]
        
    formatted_lines = []
    for header, description in results.items():
        formatted_lines.append(f"• {header} → {description}")
        
    return formatted_lines
