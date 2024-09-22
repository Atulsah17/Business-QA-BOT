# backend/pinecone_utils.py
import pinecone
from pinecone import ServerlessSpec

class PineconeClient:
    def __init__(self, api_key, environment='us-east-1-aws'):
        # Create an instance of the Pinecone class
        self.pinecone_instance = pinecone.Pinecone(api_key=api_key)
        self.index = None

    def create_index(self, index_name, dimension=768, metric='cosine'):
        # Check if the index already exists
        if index_name not in self.pinecone_instance.list_indexes().names():
            # Create the index with serverless specification
            self.pinecone_instance.create_index(
                name=index_name,
                dimension=dimension,
                metric=metric,
                spec=ServerlessSpec(cloud='aws', region='us-east-1')
            )
        # Connect to the index
        self.index = self.pinecone_instance.Index(index_name)
        return self.index

    def upsert_documents(self, index, embeddings, documents):
        # Upsert documents with embeddings and metadata
        for i, embedding in enumerate(embeddings):
            index.upsert([{
                'id': f'doc-{i}',
                'values': embedding.tolist(),
                'metadata': {'text': documents[i]}
            }])

    def retrieve_documents(self, query, model, index, top_k=3):
        # Encode the query using the model and get the embedding
        query_embedding = model.encode([query])[0]
        # Query Pinecone for the top-k similar documents
        result = index.query(vector=query_embedding.tolist(), top_k=top_k, include_metadata=True)
        # Extract text from the retrieved metadata and combine into context
        context = " ".join([match['metadata']['text'] for match in result['matches']])
        return context
