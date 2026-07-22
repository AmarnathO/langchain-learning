import os 
from dotenv import load_dotenv

# importing env variables
load_dotenv(override=True)

# LLM Configuration 
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")

