#config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key is missing. Please set the 'OPENAI_API_KEY' environment variable.")

# Color codes and model name
WHITE = "\033[37m"
GREEN = "\033[32m"
RESET_COLOR = "\033[0m"
model_name = "gpt-3.5-turbo"

