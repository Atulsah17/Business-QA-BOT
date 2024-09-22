import PyPDF2

# Extract text from PDF
def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)  # Use PdfReader instead of PdfFileReader
    text = ""
    for page in reader.pages:  
        text += page.extract_text()  
    return text

# Split document into chunks (you can adjust chunk size based on the length of the document)
def chunk_document(document_text, chunk_size=500):
    document_chunks = [document_text[i:i + chunk_size] for i in range(0, len(document_text), chunk_size)]
    return document_chunks

# Generate embeddings using the model
def generate_embeddings(model, document_chunks):
    embeddings = model.encode(document_chunks)
    return embeddings
