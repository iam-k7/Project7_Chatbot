# 🚀 Project7_Chatbot

An AI-powered chatbot application that allows users to upload PDFs, ask questions about the content, and receive context-aware answers using Retrieval-Augmented Generation (RAG).  
This project uses **FastAPI** for the backend, **Streamlit** for the frontend, and **LangChain + vector embeddings** for intelligent document querying.

---

# ✨ Features

### 📄 PDF Upload  
Upload one or multiple PDF files for processing.

### 🧠 Document-Aware Q&A  
Ask questions about your PDFs and get accurate answers using embeddings + vector search.

### ⚡ FastAPI Backend  
Handles ingestion, embeddings, Pinecone/vector-db operations, and question answering.

### 🎨 Streamlit Frontend  
A clean, modular UI with components for chat, upload, and history management.

### 💾 Download Chat History  
Export your entire chatbot conversation with one click.

---

# 🧱 Project Structure

Project7_Chatbot/

Project7_Chatbot/
├── client/               # Streamlit frontend
│   ├── app.py
│   ├── components/
│   ├── utils/
│   └── config.py
│
├── server/               # FastAPI backend
│   ├── main.py
│   ├── routes/
│   ├── modules/
│   └── middlewares/
│
├── .gitignore
├── requirements.txt
└── README.md


yaml
Copy code

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

    ```bash
    git clone https://github.com/iam-k7/Project7_Chatbot.git
    cd Project7_Chatbot
    
## 2️⃣ Create & Activate Virtual Environment

bash
Copy code
python -m venv venv
Windows
bash
Copy code
venv\Scripts\activate
macOS/Linux
bash
Copy code
source venv/bin/activate

## 3️⃣ Install Dependencies

bash
Copy code
pip install -r requirements.txt
🖥️ Run the Application

## 4️⃣ Start the FastAPI Backend

bash
Copy code
cd server
uvicorn main:app --reload --port 8000
Backend runs at:
👉 http://127.0.0.1:8000

Interactive API docs:
👉 http://127.0.0.1:8000/docs

## 5️⃣ Start the Streamlit Frontend

bash
Copy code
cd ../client
streamlit run app.py
Frontend runs at:
👉 http://localhost:8501


---


## ⚙️ Configuration

client/config.py
Set the API base URL:

python
Copy code
API_URL = "http://127.0.0.1:8000"
Modify only if your backend uses a different port.

## 📦 .gitignore

Includes:

__pycache__

Virtual environments (.venv, venv/)

.env files (API keys, secrets)

Build / compiled artifacts

IDE files

Ensures clean commits with no sensitive information.

## 🤝 Contributing

Contributions are welcome!

Fork this repository

Create a new feature branch

Commit changes with clear messages

Open a Pull Request

## ⭐ Support the Project
If you found this helpful, please give the repo a star ⭐ on GitHub — it motivates future improvements!

## 📜 License

This project is open-source and free to use.
You may add a LICENSE file (MIT recommended).

Thanks for checking out Project7_Chatbot!
Happy building 🎉

yaml
Copy code

