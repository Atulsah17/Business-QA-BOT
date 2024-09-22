import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the absolute path to the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project root to the sys.path
sys.path.append(project_root)

# Now you can import from backend
from backend.pinecone_utils import PineconeClient
from backend.cohere_utils import generate_answer
from backend.document_processing import extract_text_from_pdf, chunk_document, generate_embeddings
import streamlit as st
from sentence_transformers import SentenceTransformer

# Initialize API Clients using environment variables
pinecone_api_key = os.getenv("PINECONE_API_KEY")
cohere_api_key = os.getenv("COHERE_API_KEY")

# Check if the API keys are loaded correctly
if not pinecone_api_key or not cohere_api_key:
    st.error("API keys are missing! Please ensure they are set in the .env file.")
    sys.exit(1)

pinecone_client = PineconeClient(pinecone_api_key)

# Initialize Pinecone Index and Model
index_name = "document-index"
index = pinecone_client.create_index(index_name)
model = SentenceTransformer('all-mpnet-base-v2')

# Streamlit UI
st.title("Business QA Bot")

# File uploader for PDF
uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_file is not None:
    # Extract text from the uploaded PDF
    document_text = extract_text_from_pdf(uploaded_file)
    
    # Chunk the document into smaller parts
    document_chunks = chunk_document(document_text)
    
    # Generate embeddings for the document chunks
    document_embeddings = generate_embeddings(model, document_chunks)

    # Upsert the documents into Pinecone
    pinecone_client.upsert_documents(index, document_embeddings, document_chunks)

    # Take a query input from the user
    query = st.text_input("Ask a question based on the uploaded document:")
    
    if query:
        # Retrieve relevant context based on the query
        context = pinecone_client.retrieve_documents(query, model, index)

        if context:
            # Generate an answer using the retrieved context
            answer = generate_answer(cohere_api_key, query, context)
            
            # Display the answer and the relevant document segments
            st.write(f"**Answer**: {answer}")
            st.write(f"**Retrieved Document Segments**: {context}")
        else:
            st.write("No relevant documents found.")
