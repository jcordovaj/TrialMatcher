import os
from langchain_community.document_loaders import PyPDFLoader, JSONLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings # Or your preferred provider

# Setup persistence paths
CHROMA_PATH = "chroma_db"

class DocumentProcessor:
    """
    Handles the ingestion and vectorization of clinical assets.
    Ensures that data is persisted to avoid re-processing.
    """
    def __init__(self):
        # Initialize embeddings (ensure API Key is in env)
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.vector_db = Chroma(
            persist_directory=CHROMA_PATH, 
            embedding_function=self.embeddings
        )

    def process_pdf_protocol(self, file_path: str):
        """Processes raw PDF protocols into manageable clinical chunks."""
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        
        # Split logic: prevents context saturation
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200,
            add_start_index=True
        )
        chunks = text_splitter.split_documents(docs)
        
        # Add to persistent DB
        self.vector_db.add_documents(chunks)
        return f"Successfully vectorized {len(chunks)} protocol segments."

    def query_clinical_data(self, query: str):
        """Retrieves only the relevant context for the Assistant."""
        results = self.vector_db.similarity_search(query, k=3)
        return results