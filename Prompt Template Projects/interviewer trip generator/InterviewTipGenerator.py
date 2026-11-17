from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv(override=True)

MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")

# define template 
interview_template = """
You are a expert in taking interview for Product, Developer, QA, leaddership roles for tech and business and help candidate
in preparing the interview based on shared company {company_name} Position {position_title} and Domain {domain}

Job Description: {job_des}

You should give the tips and suggestion based on the company description and job description and prepare the candidate for the interview
in below format

- business perspective 
- product persoective 
- tech perspective 
    app platform 
    web platform 
    infra related question 
    system design

- cultural fit  
 """


 # llm instance 
chat_model = init_chat_model(
    model=MODEL_NAME,
    model_provider=MODEL_PROVIDER
)


st.title("Interview Prep Buddy")
company_name = st.text_input("Company Name")
position_title = st.text_input("Position Title")
domain = st.text_input("Domain")
job_des = st.text_area("Job Description")
submit = st.button("Submit")

if submit:
    if company_name and position_title and domain and job_des:
        response = chat_model.stream(interview_template.format(
            company_name=company_name,
            position_title=position_title,
            domain=domain,
            job_des=job_des,
        ))
        # Use st.write_stream to render the streaming response beautifully
        st.write_stream(chunk.content for chunk in response)
    else:
        st.warning("⚠️ Please fill in all fields before submitting.")


