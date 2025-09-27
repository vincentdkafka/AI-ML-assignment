# CSV Header Analyzer

A Python script that analyzes CSV file headers and generates descriptive explanations using a local AI model.

## Model Selection

This project uses **DistilGPT-2** from Hugging Face for text generation. DistilGPT-2 was chosen because it offers an excellent balance between performance and resource efficiency. It's a smaller, faster version of GPT-2 that runs entirely locally without requiring cloud API calls. The model is well-suited for generating short descriptive text and has good support for the types of field descriptions we need for database/CSV analysis.

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script:**
   ```bash
   python header_analyzer.py
   ```

The script will:
- Read headers from `demo.csv`
- Generate descriptions for each header using the AI model
- Display results on the console
- Save results to `output.txt`

## Files Included

- `header_analyzer.py` - Main script
- `demo.csv` - Sample invoice data for testing
- `requirements.txt` - Python dependencies
- `README.md` - This documentation
- `output.txt` - Generated results (created after running the script)

## Challenges Faced

The main challenge was balancing AI-generated content with reliability. Pure language model outputs can be inconsistent for technical field descriptions, so the script includes fallback logic that uses keyword matching for common database field patterns (ID, Name, Amount, Date). This hybrid approach ensures both creativity from the AI model and practical reliability for typical business data fields. Another consideration was keeping the model lightweight enough to run locally while still producing meaningful descriptions.
