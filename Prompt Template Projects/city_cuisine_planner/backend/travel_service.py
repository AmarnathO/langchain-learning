import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model

# Load environment variables
load_dotenv(override=True)

class TravelService:
    def __init__(self):
        self.model_name = os.getenv("MODEL_NAME")
        self.model_provider = os.getenv("MODEL_PROVIDER")
        
        # Initialize model
        self.chat_model = init_chat_model(
            model=self.model_name, 
            model_provider=self.model_provider
        )
        
        # Define Prompt Template
        self.template = """
You are an expert travel planner that helps users plan their trip to the requested city {city} and country {country}.
You have to share details in a markdown table format in the requested language {language}.

Format requirements:
- Places to Visit section:
Place to visit in city | relevance short summary | best time to visit | Things to keep in mind

- Cuisine & Cafes section:
Cuisine | resturant | recomendation | average price for 2 | reviews 

Important:
- Avoid giving information about fictional places.
- If the place is not in the real world, just return the exact message: "I don't have information about this place."
- Output clear, beautiful markdown tables.
"""
        self.prompt = PromptTemplate(
            input_variables=["city", "country", "language"],
            template=self.template
        )
        
        # Build runnable chain
        self.chain = self.prompt | self.chat_model

    def generate_plan(self, city: str, country: str, language: str) -> str:
        """Invokes the LangChain model to generate the travel plan."""
        response = self.chain.invoke({
            "city": city,
            "country": country,
            "language": language
        })
        return response.content
