
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser


import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv(override=True)
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")


template  = """
You are expert in Hindu mythlogy -  Your tasks is to explain any question {question} asked by user regarding
Mahabharat, Ramayan, Bhagwat Geeta and other Hindu religious text.  
- keep the language simple and easy to understand 
- keep the explanation concise and to the point 
- Give story and a bit of context around the same.

"""


prompt = PromptTemplate(
    input_variables=["question"],
    template=template,
)


# llm model

llm = init_chat_model(
    model=MODEL_NAME,
    model_provider=MODEL_PROVIDER
    )


# chain 
chain = prompt | llm | StrOutputParser()


st.set_page_config(page_title="Mythology Expert", layout="centered")
st.title("Sarthi")
st.subheader("Your guide in life from ancient scriptures.")
question = st.text_input("Ask your question")
submit = st.button("Submit")

if submit and question :
    with st.spinner("OM Namah Shivay")




# invoking chain
chain.invoke({
    ""
})