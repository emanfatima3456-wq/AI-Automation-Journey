from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/auto"
)

# Prompt Template banana
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful business assistant."),
    ("human", "Analyze this lead: Name={name}, Budget=${budget}, Requirements={requirements}")
])

# Chain banana — Prompt + LLM
chain = prompt | llm

# Run karo
response = chain.invoke({
    "name": "Ahmed Khan",
    "budget": "50000",
    "requirements": "Need a CRM system"
})

print("AI Response:")
print(response.content)