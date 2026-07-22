import sys 
from pathlib import Path 

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.prompts.chat_prompt import prompt
from src.models.llm import llm_client
import streamlit as st 


def ask_question(question: str):
    answer_chain = prompt | llm_client
    response = answer_chain.invoke(input={
        "question": question
    })
    return response

st.title("Ask Anything")
question = st.text_input("Enter your question here")
submit_button = st.button("Send")
if question and submit_button:
    answer = ask_question(question=question)
    st.write(f"AI Response : {answer.content}")

    
