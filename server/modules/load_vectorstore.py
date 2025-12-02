import os
import time
from pathlib import Path
from dotenv import load_dotenv
from tqdm.auto import tqdm
from pinecone import Pinecone, ServerlessSpec
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = "us-east-1"
PINECONE_INDEX_NAME = "codingindex"

UPLOAD_DIR = "./upload_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
spec = ServerlessSpec(cloud="aws", region=PINECONE_ENV)

# Create index if not exists
existing_indexes = [i["name"] for i in pc.list_indexes()]
if PINECONE_INDEX_NAME not in existing_indexes:
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=1024,          # MUST MATCH embedding size
        metric="dotproduct",
        spec=spec
    )
    while not pc.describe_index(PINECONE_INDEX_NAME).status["ready"]:
        time.sleep(1)

index = pc.Index(PINECONE_INDEX_NAME)


def load_vectorstore(uploaded_files):

    embed_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-large-en-v1.5"  # 1024 dimension
    )

    if not isinstance(uploaded_files, list):
        uploaded_files = [uploaded_files]

    all_texts = []
    all_metadata = []
    all_ids = []

    for file in uploaded_files:

        # Save PDF file
        save_path = Path(UPLOAD_DIR) / file.filename
        with open(save_path, "wb") as f:
            f.write(file.file.read())

        # Load & split
        loader = PyPDFLoader(str(save_path))
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )
        chunks = splitter.split_documents(docs)

        # Collect chunks
        for i, chunk in enumerate(chunks):
            all_texts.append(chunk.page_content)

            all_metadata.append({
                "text": chunk.page_content,
                "page": chunk.metadata.get("page", None),
                "source": str(save_path)
            })

            all_ids.append(f"{save_path.stem}-{i}")

    # ---- EMBED ----
    print(f"Embedding {len(all_texts)} chunks...")
    embeddings = embed_model.embed_documents(all_texts)

    # ---- UPSERT ----
    print("Upserting to Pinecone...")
    with tqdm(total=len(embeddings), desc="Uploading") as progress:

        index.upsert(
            vectors=zip(all_ids, embeddings, all_metadata)
        )
        progress.update(len(embeddings))

    print("Upload complete!")
