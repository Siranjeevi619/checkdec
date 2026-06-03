
from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    api_key = os.getenv("API_KEY")
    model_name = os.getenv("MODEL_NAME")
    embedding_model_name = os.getenv("EMBEDDING_MODEL_NAME")
    
config = Config()