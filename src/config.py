import os
from dotenv import load_dotenv

# Config parameters 

load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")
