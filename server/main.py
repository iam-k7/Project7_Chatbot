from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware
from routes.upload_pdfs import router as upload_router
from routes.ask_question import router as ask_router


app=FastAPI(
    title="Project7 API",
    description="API for AI project Assistant Chatbot"
)

@app.get("/")
def home():
    return {"message": "Project7 API is running!"}


#CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # allow all origins
    allow_credentials=["*"],   # must be false when using "*"
    allow_methods=["*"],
    allow_headers=["*"]
)


# middleware exception handlers
app.middleware("http")(catch_exception_middleware)

# routers

# 1. upload pdfs documents
app.include_router(upload_router)
# 2. asking query
app.include_router(ask_router)