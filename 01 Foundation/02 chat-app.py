from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv 
import streamlit as st 

load_dotenv(override=True)

llm = init_chat_model(model="nvidia/nemotron-3-ultra-550b-a55b:free",model_provider="openrouter")

# streamlit 
st.title(" Nvidia Powerd Chat App ")

user_input = st.text_input("")
submit = st.button("Send")

if user_input and submit :
    resposne = llm.invoke(user_input)
    st.write(f"Nvidea Response : {resposne.content}")
    st.write(f"Input Token : {resposne.usage_metadata.get("input_tokens")}")
    st.write(f"Output Token : {resposne.usage_metadata.get("output_tokens")}")
    st.write(f"Total Token : {resposne.usage_metadata.get("total_tokens")}")