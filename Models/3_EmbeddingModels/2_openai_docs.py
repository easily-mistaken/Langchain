from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Bangalore is the IT capital of India",
    "Chennai is the capital of Tamil Nadu",
    "Hyderabad is the capital of Telangana",
    "Ahmedabad is the capital of Gujarat",
    "Pune is the capital of Maharashtra",
    "Jaipur is the capital of Rajasthan",
    "Lucknow is the capital of Uttar Pradesh",
]

responses = embedding.embed_documents(documents)
print(str(responses))