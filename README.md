# 🚀 Coding Assistant Chatbot

An AI-powered Coding Assistant that lets you:

- 📤 Upload PDFs  
- 🤖 Ask questions about the content  
- 🧠 Get LLM-powered answers (RAG + embeddings)  
- 📥 Download your chat history  
- 🧩 Use a clean Streamlit UI + FastAPI backend  

This project is built using **FastAPI**, **Streamlit**, **LangChain**, **Pinecone**, and **HuggingFace Embeddings**.

---

# 🎥 Demo (GIF)

Below is an AI-generated demonstration of how the app works:

![Demo GIF](A_GIF_demonstrates_an_AI-driven_Coding_Assistant_C.png)

---

# 🧠 Features

### ✅ Upload & process PDFs  
Documents are embedded and stored in Pinecone for semantic search.

### ✅ Chat with your documents  
Ask any question and get accurate answers powered by RAG (Retrieval-Augmented Generation).

### ✅ Streamlit UI  
Beautiful modular UI with uploader, chat component, and history downloader.

### ✅ FastAPI backend  
Handles PDF ingestion, vector DB updates, and real-time LLM inference.

### ✅ Chat history download  
Export your conversation as a text or JSON file.

---

# 📁 Project Structure

Project7/
│
├── client/ # Streamlit UI
│ ├── app.py # Streamlit entry point
│ ├── components/ # UI components (chat, upload, history)
│ ├── utils/ # API client helpers (requests)
│ └── config.py # API URL config
│
├── server/ # FastAPI backend
│ ├── main.py # FastAPI entry point
│ ├── modules/ # LLM, embeddings, loaders, handlers
│ ├── routes/ # API endpoints (/ask, /upload_pdfs)
│ └── middlewares/ # Exception handlers
│
├── .gitignore # Git ignored files
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

# 🛠️ Tech Stack

### **Frontend**
- Streamlit  
- Custom UI components  
- Clean and modular interface  

### **Backend**
- FastAPI  
- Pydantic  
- LangChain  
- Pinecone Vector DB  
- HuggingFace Embeddings  

### **AI**
- RAG (Retrieval-Augmented Generation)  
- Context-aware LLM responses  

---

# ▶️ Getting Started

## **1️⃣ Create virtual environment**

```bash
python -m venv venv

venv\Scripts\activate           # Windows

pip install -r requirements.txt # Install dependencies

cd server                       # Start FastAPI backend
uvicorn main:app --reload --port 8000

Uvicorn running on http://127.0.0.1:8000

