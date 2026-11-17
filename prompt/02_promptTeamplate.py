
import os 
from dotenv import load_dotenv
import streamlit as st 

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate

load_dotenv(override=True)

llm = init_chat_model(
    model= os.getenv("MODEL_NAME"),
    model_provider=os.getenv("MODEL_PROVIDER")
)

poem_template = PromptTemplate(  
input_variables=["topic"],
template = """
# Role : You are a Poet who is well versed in writing poem related to any genere.
# Context : You wirte the poems for requested subject and emotion by customer 
# Task : Share poem on given topic {topic} requested by customer  
# constrain: 
- poem should be in rhyming format
- poem should not be more then 200 words 
- Avoid to share any poem that is objectfting anyone

# Output 
- Poem Title
- Poem Content 

""")

# making user msg whcich will send to llm 
#msg = poem_template.format(topic="Stars")


st.title("AI - Poem Writer")

user_topic = st.text_input("Poem Topic ")
submit = st.button ("Submit")

if submit and user_topic:
    with st.spinner("AI Writer is Thinking...."):
        response = llm.invoke(poem_template.format(topic=user_topic))
        st.write(response.content)