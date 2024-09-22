# backend/cohere_utils.py
import cohere

def initialize_cohere(api_key):
    return cohere.Client(api_key)

def generate_answer(api_key, query, context):
    cohere_client = initialize_cohere(api_key)
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    
    response = cohere_client.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.generations[0].text.strip()
