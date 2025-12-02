from logger import logger

def query_chain(chain, question: str):
    try:
        return chain.invoke({"question": question})

    except Exception as e:
        logger.exception("Error runnning LLm chain")
        
        return {
            "success": False,
            "message": "Something went wrong while generating the answer.",
            "details": str(e)
        }