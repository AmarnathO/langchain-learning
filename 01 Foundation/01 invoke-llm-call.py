from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv 

load_dotenv(override=True)

llm = init_chat_model(model="nvidia/nemotron-3-ultra-550b-a55b:free",model_provider="openrouter")

resposne = llm.invoke("Tell me about yourself")

print(resposne.content)
