from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=100)

response = llm.invoke("Write a poem about the sea.")
print(response.content)