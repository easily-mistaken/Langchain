from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-2', temperature=0.5, max_tokens_to_sample=150)

response = model.invoke("Tell me a fun fact about space.")
print(response.content)