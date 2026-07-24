from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model

import os 
from dotenv import load_dotenv
import streamlit as st


# loading env variables 
load_dotenv(override=True)

#importing variables 
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")


# initializing model 
chat_model = init_chat_model(model=MODEL_NAME, model_provider=MODEL_PROVIDER)


# Template 
city_crusine_template = """
You are a travel planner that helps user to plan their trip for requested city {city} and country {country}
you have to share  details in table format in requested language {language}

Place to visit in city | relevance short summary | best time to visit | Things to keep in mind

you also have to suggest the best crusines  and cafe in that {city} in below format

Cuisine | resturant | recomendation | average price for 2 | reviews 

"""


# making prompt for the user input 
prompt = PromptTemplate(
    input_variables=["city", "country","language"],
    template=city_crusine_template 
)


# streamlit 
st.title("AI Powered Travel Planner")
city = st.text_input("Enter Desitnation City")
country = st.text_input("Enter Country Name")
language = st.text_input("Input your language")
submit = st.button("Submit")



# calling llm 

if submit and city and country and language:
    with st.spinner("🚀 Analyzing Your trip this may take a moment... 🚀"):
        full_response = chat_model.invoke(
            prompt.format(city=city, country=country, language=language)
        )
        st.write(full_response.content)

