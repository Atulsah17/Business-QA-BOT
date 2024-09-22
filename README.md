# Business QA Bot

The **Business QA Bot** allows users to upload business-related documents, ask questions about the content, and receive contextually relevant answers. The bot leverages **Streamlit** for the frontend, **Pinecone** for document retrieval, and **Cohere** for generating responses.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Jupyter Notebook](#jupyter-notebook)
  - [Docker Setup](#docker-setup)
- [Usage](#usage)

---

## Features

- Upload business-related PDFs.
- Ask questions based on the uploaded content.
- Receive accurate, context-aware answers.
- View relevant document sections used to generate the answer.

---

## Project Structure

```bash
QA-Bot/
│
├── frontend/
│   └── app.py                # Main Streamlit app
│
└── backend/
    ├── __init__.py           # Module initialization file
    ├── pinecone_utils.py      # Pinecone utility functions
    ├── cohere_utils.py        # Cohere utility functions
    └── document_processing.py # Text extraction and document chunking
├── QA_Bot.ipynb              # Jupyter Notebook for prototyping
├── Dockerfile                # Docker setup
├── README.md                 # Project documentation
└── requirements.txt          # Python package dependencies

File Descriptions
frontend/app.py: The main Streamlit web application where users upload documents and ask questions.
backend/pinecone_utils.py: Pinecone utility functions for managing the index, document embedding, and retrieval.
backend/cohere_utils.py: Cohere integration for generating natural language responses.
backend/document_processing.py: Handles PDF processing, chunking documents into sections, and generating embeddings.
QA_Bot.ipynb: A Jupyter Notebook to interactively test and prototype the Business QA Bot.
Dockerfile: Docker configuration for running the app in a container.

Requirements
To run the project locally, ensure you have the following installed:

Python 3.8 or higher
Streamlit
Pinecone
Cohere
Sentence-Transformers
PyPDF2
Python Packages
Install all required Python packages using the requirements.txt file:

pip install -r requirements.txt

Installation
Running the Streamlit App Locally
1Clone the repository: 
git clone https://github.com/Atulsah17/Business-QA-Chatbot.git
cd business-qa-bot

2. Install dependencies: 
pip install -r requirements.txt

3. Set up API keys: Add your Pinecone and Cohere API keys in frontend/app.py or set them using environment variables.

4. Run the Streamlit app:
streamlit run frontend/app.py


Jupyter Notebook
You can test the bot’s functionality interactively using the provided Jupyter Notebook:

1. Install Jupyter:
pip install notebook

2. Run the notebook:
jupyter notebook

3. Open QA_Bot.ipynb and test various functionalities like document uploading, querying, and response generation.


Docker Setup
You can containerize the application using the provided Dockerfile to ensure consistency across environments.

Steps to Run with Docker
1. Build the Docker image:
docker build -t business-qa-bot .

2. Run the Docker container:
docker run -p 8501:8501 business-qa-bot
The app will now be running at http://localhost:8501.


Usage

Basic Interaction Flow
1. Upload a PDF: You can upload a business-related PDF document using the file uploader.
2. Ask a Question: Once the document is processed, enter your query in the text input field.
3. Get a Response: The bot will retrieve relevant document segments and generate an accurate response.

Frontend Overview
The Streamlit application consists of:

File Uploader: For uploading PDF documents.
Query Input: A text input field for asking questions based on the document content.
Response Display: Shows the generated answer and retrieved document sections.

