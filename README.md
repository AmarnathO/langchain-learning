**langchain**

- Langchain is a Python framework for building applications with LLMs (Large Language Models).

- langchain is a workflow that connect mutiple compoents to make a sequence here out of one chain become input for other chain.

- chain : Means differenct stages lined up in a sequence 

- langchain gives us the ability to build application with 
    - memory : remember historical chat 
    - tools : functions that can be called
        - Search internet 
        - Query DB
        - Send Emails
    - knowledge intergation : Your data sources
    - Agents / Agency  : 3rd party tool that perform task on behalf of user like Search  
    - creating APIs 

- We need langchain To avoid rewriting common AI application patterns and provide a unified execution model.

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


**Prompt Template** 
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


**Types of Prompt Templates**
**PromptTemplate** : Used for text-based prompts.
Example  - Summarize the following text:{text}

**ChatPromptTemplate** : Used for chat models.
Example - 
System:You are an AI Architect.
Human: Explain Kubernetes.

**Architecture** 
Variables
      │
      ▼
PromptTemplate
      │
      ▼
Formatted Prompt
      │
      ▼
Messages
      │
      ▼
Chat Model

 **Model** : A component responsible for generating responses from input.

**Chat Model** : A model that operates on structured messages instead of plain text.

**Message** : A role-based communication object exchanged between the application and the model.

**Standardization** :  LangChain abstracts provider-specific APIs behind a common interface, enabling provider-agnostic application development.



# Fundamental Questions 
**What problem does LangChain solve?**
Without LangChain, you'd have to implement:
    Prompt management
    Streaming
    Retry
    Tool calling
    Memory
    Logging
    Tracing
    Model switching
    Async execution
    Parallel execution
    Output parsing
    Structured outputs
    RAG orchestration

That's a significant engineering effort before you've even built your product.

LangChain gives you these building blocks so you can focus on solving the business problem instead of recreating infrastructure.

**Why isn't the OpenAI SDK alone enough for many production applications?**

The OpenAI SDK is designed to interact with OpenAI's models, not to orchestrate complete AI applications. Production AI systems require capabilities such as prompt management, retrieval (RAG), tool integration, memory, structured outputs, model switching, streaming, retries, observability, and workflow orchestration. LangChain provides standardized abstractions for these concerns, enabling developers to build scalable, provider-agnostic, and maintainable AI applications.

**What does "composable framework" mean?**
    Small, independent components that can be connected in different combinations to create larger systems.

**Why is LangChain centered around execution pipelines rather than just model objects?**

"LangChain is centered around execution pipelines because an LLM is only one component of a production AI application. Real-world AI systems involve prompt construction, retrieval, tool execution, memory, parsing, validation, and model invocation. LangChain abstracts each of these as Runnable components with a common execution interface, allowing them to be composed into flexible, reusable, and provider-agnostic pipelines. This design enables features like streaming, batching, parallel execution, retries, and observability to work consistently across the entire workflow."

**What is the difference between a simple LLM call and a LangChain pipeline?**
A simple LLM call sends a prompt directly to a model and returns a response, making it suitable for basic use cases. A LangChain pipeline orchestrates the complete AI workflow by composing multiple executable components—such as prompt templates, retrievers, tools, memory, parsers, and the LLM—into a reusable, configurable, and production-ready execution flow. The LLM becomes one step in the pipeline rather than the entire application.

**What is the difference between an LLM and a Chat Model?**

An LLM accepts plain text as input and generates plain text as output. A Chat Model accepts a sequence of structured messages (System, Human, AI, Tool) and generates a conversational response while preserving role-based context. Modern production applications primarily use Chat Models because they support multi-turn conversations, tool calling, and structured interactions.


**Why does LangChain use Messages instead of plain strings?**

Messages preserve conversational context by assigning roles such as System, Human, AI, and Tool. This enables role-based prompting, multi-turn conversations, tool calling, and provider-independent communication, making AI applications more structured and maintainable than using plain text prompts.

**How does LangChain support multiple LLM providers using the same code?**

LangChain provides a standardized model interface and internally translates its message abstractions into the provider-specific request format. This allows developers to switch between providers such as OpenAI, Anthropic, Ollama, or OpenRouter with minimal code changes while keeping the application logic unchanged.

**Why are Chat Models preferred over traditional LLMs?**
Chat Models support structured, role-based interactions, multi-turn conversations, tool calling, and system instructions, making them better suited for production AI applications than traditional text-completion LLMs.

**Why does LangChain use Messages instead of strings?**
Messages provide explicit role separation and a standardized conversation structure, enabling consistent behavior across providers and advanced capabilities such as tool calling and conversation history.

**What problem does model abstraction solve?**
Model abstraction decouples application logic from model providers, allowing developers to switch between providers with minimal code changes while keeping the rest of the application unchanged.

**How does LangChain make switching providers easier?**
LangChain exposes a common model interface and internally translates standardized message objects into provider-specific request formats, enabling provider-agnostic AI applications


**Message Types** 

You only need to know these four initially:

**BaseMessage**
BaseMessage is the abstract parent class for all message types in LangChain. It defines the common structure shared by SystemMessage, HumanMessage, AIMessage, and ToolMessage.

**HumanMessage** : Represents the user's input.

**SystemMessage** : Defines the model's behavior and instructions.
Example: "You are a senior software architect."

**AIMessage**: Represents the model's response.

**ToolMessage** : Represents the output returned by a tool.

from langchain_core.messages import (HumanMessage,SystemMessage,AIMessage,ToolMessage)


**Runnables**
- Before runnable every component in langchain have it own exection method like
    - llm.predict()
    - prompt.format()
    - retriver.get_documents()
    - parser.parse
- Every component has differebnt API this makes composable of component diffcult
- Runnable intriduce to have common execution contract across all component
- by having common execution every component llm / prompt / retriver / parser
  and chains to be compomse / reuse and orchitrated together. while supporting streaming / batching / async all together.
  
**A Runnable is any LangChain component that accepts an input, performs an operation, and returns an output through a standardized execution interface**

**core method**
| Method      | Purpose                 |
| ----------- | ----------------------- |
| `invoke()`  | Execute one input       |
| `batch()`   | Execute multiple inputs |
| `stream()`  | Stream output           |
| `ainvoke()` | Async single execution  |
| `abatch()`  | Async batch execution   |
| `astream()` | Async streaming         |
