import os 
from dotenv import load_dotenv
import streamlit as st 

from langchain.chat_models import init_chat_model

load_dotenv(override=True)

llm = init_chat_model(
    model=os.getenv("MODEL_NAME"),
    model_provider=os.getenv("MODEL_PROVIDER")
)

prompt = """
Role : You are a story teller who know all the stories related to mythology of all religon.
Context: you share  story with user based on given topic and region and give them learning out of that stories
Task : Answer the user with story based in given religion and query - insighrs and learning which they can implement in life
Input : Tell me about how thinking about myself only can be deangerous 
Constrain :  
- keep the repose under 500 rods 
- if you fon;t have any story - respond as We don;t have any Religion story around the topic
- Please share thr reference from where you have picked the story
- Do not invent any new story  or random story aleays have a reference for your shared story.

Output: The reponse should be in below format 
- Title 
- Story 
- Message of Story 
- Reference 

"""

st.title("Mythology Mystics By AI Guru")
with st.spinner(" Guru Ji Thinkling....."):
    resposne = llm.invoke(prompt)
    st.write(resposne.content)