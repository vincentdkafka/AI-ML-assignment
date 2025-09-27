
"""
This module handles all Hugging Face transformer model operations including
initialization and text generation for header analysis.
"""

from transformers import pipeline, set_seed
import warnings

warnings.filterwarnings("ignore")


class HeaderAnalysisModel:
    """
    A class to handle the AI model for generating header descriptions.
    """
    
    def __init__(self, model_name="distilgpt2"):
        """
        Initialize the Header Analysis Model.
        
        Args:
            model_name (str): Name of the Hugging Face model to use
        """
        self.model_name = model_name
        self.generator = None
        self.fallback_descriptions = {
            'invoice_id': 'likely a unique transaction identifier',
            'vendor_name': 'the supplier or vendor associated with the transaction', 
            'amount': 'monetary value of the transaction',
            'payment_date': 'date on which the payment was made',
            'id': 'a unique identifier for the record',
            'name': 'a descriptive label or title field',
            'date': 'a timestamp or calendar date field',
            'vendor': 'a supplier or service provider identifier',
            'invoice': 'a billing document or transaction record',
            'payment': 'a financial transaction or settlement record',
            'customer': 'client or buyer information',
            'total': 'sum or aggregate monetary value',
            'price': 'cost or monetary value',
            'quantity': 'count or amount of items',
            'status': 'current state or condition',
            'email': 'electronic mail address',
            'phone': 'telephone contact number',
            'address': 'physical location or mailing address',
            'description': 'detailed explanation or notes',
            'category': 'classification or grouping identifier'
        }
    
    def initialize_model(self):
        """
        Initialize the text generation model.
        
        Returns:
            bool: True if successful, False otherwise
        """
        print(f"🤖 Initializing local AI model ({self.model_name})...")
        try:
            set_seed(42)
            
            self.generator = pipeline(
                "text-generation",
                model=self.model_name,
                max_length=50,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=50256  
            )
            print("✓ Model initialized successfully!")
            return True
            
        except Exception as e:
            print(f" Error initializing model: {e}")
            return False
    
    def _get_fallback_description(self, header_name):
        """
        Get fallback description based on keyword matching.
        
        Args:
            header_name (str): The header name to analyze
            
        Returns:
            str: Fallback description if found, None otherwise
        """
        header_lower = header_name.lower()
        
        if header_lower in self.fallback_descriptions:
            return self.fallback_descriptions[header_lower]
        
        for keyword, description in self.fallback_descriptions.items():
            if keyword in header_lower:
                return description
                
        return None
    
    def _generate_ai_description(self, header_name):
        """
        Generate description using the AI model.
        
        Args:
            header_name (str): The header name to analyze
            
        Returns:
            str: Generated description or fallback
        """
        if not self.generator:
            return "a data field
        
        try:
            prompts = [
                f"The CSV column '{header_name}' contains",
                f"In a database, the field '{header_name}' typically stores",
                f"The data column '{header_name}' represents"
            ]
            
            for prompt in prompts:
                try:
                    result = self.generator(
                        prompt, 
                        max_length=25, 
                        num_return_sequences=1, 
                        truncation=True
                    )
                    generated_text = result[0]['generated_text']
                    
                    description = generated_text.replace(prompt, "").strip()
                    
                    if '.' in description:
                        description = description.split('.')[0]
                    if ',' in description:
                        description = description.split(',')[0]
                    
                    if 5 < len(description) < 50 and description not in prompt:
                        return description.strip()
                        
                except:
                    continue
            
            return "a data field"
            
        except Exception as e:
            print(f"⚠ Warning: Error generating AI description for '{header_name}': {e}")
            return "a data field"
    
    def generate_description(self, header_name):
        """
        Generate a descriptive text for a given header.
        
        This method first tries to use predefined fallbacks for common field types,
        then falls back to AI generation if no match is found.
        
        Args:
            header_name (str): The header name to analyze
            
        Returns:
            str: Generated description
        """
        fallback_desc = self._get_fallback_description(header_name)
        if fallback_desc:
            return fallback_desc
        
        return self._generate_ai_description(header_name)
    
    def analyze_headers(self, headers):
        """
        Analyze all headers and generate descriptions.
        
        Args:
            headers (list): List of header names
            
        Returns:
            dict: Dictionary mapping headers to descriptions
        """
        if not headers:
            return {}
        
        print(f"\n📊 Analyzing {len(headers)} headers...")
        results = {}
        
        for i, header in enumerate(headers, 1):
            print(f"   {i}/{len(headers)}: Processing '{header}'...")
            description = self.generate_description(header)
            results[header] = description
        
        return results
