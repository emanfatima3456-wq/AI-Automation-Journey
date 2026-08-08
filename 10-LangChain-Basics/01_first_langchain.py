from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

# OpenRouter se free model use karein
llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/auto"
)

# Pehla AI call!
response = llm.invoke([
    HumanMessage(content="What is LangChain? Explain in 3 lines.")
])

print("AI Response:")
print(response.content)