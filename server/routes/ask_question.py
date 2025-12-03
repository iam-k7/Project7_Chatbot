from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from modules.llm import get_llm_chain
from modules.query_handlers import query_chain
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import Pinecone
from pydantic import Field, BaseModel
from typing import List, Optional
from logger import logger
import os

router=APIRouter()

class AskRequest(BaseModel):
    question: str

@router.post("/ask/")
async def ask_question(payload: AskRequest):
    try:
        question = payload.question
        logger.info(f"User query:{question}")

        # embed model + pinecone setup 
        pc=Pinecone(api_key=os.environ["PINECONE_API_KEY"])
        index=pc.Index(os.environ["PINECONE_INDEX_NAME"])

        embed_model = HuggingFaceEmbeddings(
            model_name="BAAI/bge-large-en-v1.5"
        )
        embedded_query=embed_model.embed_query(question)

        res=index.query(
            vector=embedded_query,
            top_k=3,
            include_metadata=True
        )

        docs = []
        for match in res["matches"]:
            page_text = match["metadata"].get("text", "")
            metadata = match["metadata"]

            docs.append(
                Document(
                    page_content=page_text,
                    metadata=metadata
                )
            )
        class SimpleRetriever(BaseRetriever):
            tags: Optional[list[str]] = Field(default_factory=list)
            metadata: Optional[dict] = Field(default_factory=dict)

            def __init__(self, documents: List[Document]):
                super().__init__()
                self.__docs__ = documents

            def _get_relevant_documents(self, query: str):
                return self.__docs__
            
        retriever=SimpleRetriever(docs)
        chain=get_llm_chain(retriever)
        result = chain.invoke({"question": question})

        logger.info("Query success")
        result = chain.invoke({"question": question})
        return {"response": result}

    except Exception as e:
        logger.exception("Error processing question")
        return JSONResponse(status_code=500,content={"error":str(e)})
    
