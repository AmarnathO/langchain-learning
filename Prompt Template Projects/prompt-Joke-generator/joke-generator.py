from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from langchain_core.globals import set_debug
from dotenv import load_dotenv
import os 
import streamlit as st

# Importing variables 
load_dotenv(override=True)

# Enable debug
set_debug(True)

# importing os env varibles 
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER")

print(MODEL_NAME)


context = """
You are a comedian just like name {name} in india act as him and tell a joke on given condtion {condtion}
please behave as close as possible to give character.

"""

template = PromptTemplate(
    input_variables=["name","condtion"],
    template=context
)

@st.cache_resource
def get_llm(model_name,model_provider):
    return init_chat_model(model=model_name, model_provider=model_provider)

llm = get_llm(MODEL_NAME,MODEL_PROVIDER)


# Streamlit 
st.title("Your AI Comedian")
comedian_name = st.text_input("Enter comedian name")
condtion = st.text_input("Enter  context")
submit = st.button("Submit")



if comedian_name and condtion and submit:
    with st.spinner("🚀 generating Jokes... This may take a moment..."):
        try:
            # All execution code MUST be indented inside the try block
            response = llm.stream(
                template.format(name=comedian_name, condtion=condtion)
            )

            metadata_holder = {}

            def stream_and_capture_metadata(stream):
                for chunk in stream:
                    if chunk.response_metadata:
                        metadata_holder.update(chunk.response_metadata)

                    if chunk.content:
                        yield chunk.content

            st.write_stream(stream_and_capture_metadata(response))
            exact_model = metadata_holder.get("model_name", MODEL_NAME)
            finish_reason = metadata_holder.get("finish_reason", "N/A")

            st.caption(
                f"⚡ **Model:** `{exact_model}` | **Reason:** `{finish_reason}`"
            )

        except Exception as ex:
            # except MUST align with try, and its body MUST be indented
            st.error(f"An error occurred while generating the plan: {ex}")



           