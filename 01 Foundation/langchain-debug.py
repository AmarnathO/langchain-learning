# this is to enable debug mode of langchain to see all detals of langchain.
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.globals import set_debug
import os 

# importing variables 
load_dotenv(override=True)

# Enabling debug for langchain
set_debug(True)

# importing the Env variabels 
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")


# instance of llm
llm = init_chat_model(model=MODEL_NAME, model_provider=MODEL_PROVIDER)

# taking user question 
question = input("Enter your question: \n")

#invoke llm call
response = llm.invoke(question)


# printing response 
print(response)
