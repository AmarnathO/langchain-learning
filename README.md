# langchain

- Langchain is a Python framework for building applications with LLMs (Large Language Models).

- langchain gives us the ability to build application with 
    - memory : remember historical chat 
    - tools : functions that can be called
        - Search internet 
        - Query DB
        - Send Emails
    - knowledge intergation : Your data sources
    - Agents / Agency  : 3rd party tool that perform task on behalf of user like Search  
    - creating APIs 

- Example :
    - To connect to different model we have chat_model library 
    - Option to create template and dynamically inject the user input 
    - Pre define module for llm output StrOutputParser
    - Document loader to load differe type of documents 
        - langchain_community.document_loaders import NotionDirectoryLoader
        - langchain_community.document_loader import PyPDFLoader
        - langchain_community.document_loader import TextLoader
        - langchain_community.document_loaders import UnstructuredEmailLoader

- Sample Code 
    pdf_loader = PyPDFLoader("pdf-file.pdf")
    docs = pdf_loader.load() 

    email_loader = UnstructureEmailLoader("email-file.eml")
    email = email_loader.load() 

    notion_loader = NotionDirectoryLoader("notion-data")
    notion = notion_loader.load()    


# Prompt Template 
- Prompt is simply the text which we give as input to llm and llm process teh same and give us the output

- It consist of below component
    - Instructions
    - context 
    - input data
    - Output indicator 

- Example  : 
    Instructions : You are customer sentiment analysis expert. 
    You task is to analyze the customer sentiment based on the reviews given below
    
    Reviews : 
    Review1 : "This is a great product. Highly recommended!"
    Review2 : "The product is good, but the customer service is not up to the mark."
    Review3 : "I am very disappointed with the product. It is not as described."

    Output indicator : 
    sentiment : positive | negetive | neutral 





        





