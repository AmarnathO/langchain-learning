# mutiple varibale GenAi App Spech Writer

from os import write
import os 
from dotenv import load_dotenv
import streamlit as st 

from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.globals import set_debug

load_dotenv(override=True)
set_debug(True)

Speech_template = """
Role :  You are a senior and experienced political speech writer.
Context: You write the political speech on topic and emotions given by the customer- Write speech that shows failure of eariler goverment and how we can improve.
Task: Write speech on topic {topic} in referece to given {emotion}.
Constrain : 
- Write the speech under 500 words only
- Write the speech conseding we do not harm any relogion or caste
- Only speak in referece to fact around the topic

Output :
- Topic 
- Speech
- plan of solving the problem

"""

speech_final_template = PromptTemplate(
    input_variables=["topic","emotions"],
    template= Speech_template
)

llm = init_chat_model(
    model=os.getenv("MODEL_NAME"),
    model_provider="ollama"
)

st.title("AI Political Writer")
topic = st.text_input("Topic : ")
emotions = st.text_input("Emotion : ")
submit = st.button("Submit")

if submit and topic and emotions:
    with st.spinner("Making Speech....."):
        response = llm.invoke(
            speech_final_template.format(
                topic="topic",
                emotion = "emotions"
                )
            )
    st.write(response.content)

    