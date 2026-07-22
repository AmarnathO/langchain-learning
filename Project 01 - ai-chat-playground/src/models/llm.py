from langchain.chat_models import init_chat_model
from src.config.seetings import MODEL_NAME,MODEL_PROVIDER

llm_client = init_chat_model(
    model=MODEL_NAME,
    model_provider=MODEL_PROVIDER
)