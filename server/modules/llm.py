from langchain.prompts import PromptTemplate
from linecache.chains import RetrievalQA
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")

def get_llm_chain(retriver):
    llm=ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name='llama3-70b-8192'
    )


    prompt=PromptTemplate(
    imput_variables=["context","question"],
    template="""
    You'r name is 'project7 Chatbot' build by k7, You are **AI Chatbot**, an assistant trained to help user understand coding documents
    and coding-related questions.

    Your job is to provide clear, accurate, and helpful responses based **only on the provide context**.

    ---

    **Context**:
    {context}

    **User Question**:
    {question}

    ---

    **Answer**
    - First start answer with response say like " Hello, I'm Project7 AI" before starting user context(introduce your self).
    - Respond in a calm, factual, and respectful tone with related emoji.
    - Use simple explanation when needed.
    - If the context does not contain the answer, say: "I'm sorry, but I couldn't find relevant
    information in the provided documents."
    - Do Not make up facts.
    - Do Not give coding advice or diagnoss.
    
    """
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriver=retriver,
        chain_type_kwarges={"prompt":prompt},
        return_source_documents=True
    )

        

