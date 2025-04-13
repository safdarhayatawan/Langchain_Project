import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Test loading the environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')
huggingface_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

print("Environment Variables Test:")
print("-" * 30)
print(f"GOOGLE_API_KEY loaded: {'Yes' if google_api_key else 'No'}")
print(f"HUGGINGFACEHUB_API_TOKEN loaded: {'Yes' if huggingface_token else 'No'}") 