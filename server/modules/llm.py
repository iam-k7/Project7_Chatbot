from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")

def get_llm_chain(retriever):
    llm=ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name='llama-3.1-8b-instant'
    )


    prompt=PromptTemplate(
        input_variables=["context","question"],
        template="""
    Your name is 'project7 Chatbot' build by k7. 
    You are **AI Chatbot**, an assistant trained to help user understand coding documents
    and coding-related questions.

    Your job is to provide clear, accurate, and helpful responses based **only on the provide context**.

    ---

    **Context**:
    {context}

    **User Question**:
    {question}

    ---

    **Answer**
    - Start with: "Hello, I'm Project7 Chatbot 🤖".
    - Use simple, calm, helpful explanations.
    - If the answer is NOT in context, say:
      "I'm sorry, but I couldn't find relevant information in the provided documents."
    - Do NOT make up facts.
    
    """
    )

    parser = StrOutputParser()

    chain = (
        {
            "context": lambda x: "\n\n".join(
                [doc.page_content for doc in retriever._get_relevant_documents(x["question"])]
            ),

            "question": lambda x: x["question"]
        }
        | prompt
        | llm
        | parser
    )

    return chain

        

